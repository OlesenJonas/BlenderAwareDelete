'''
This will add CTRL SHIFT X as keybind for instant deletion of
whatever is selected (keybind can be changed in line 47)
'''
 
bl_info = {
    "name": "Selection Aware Delete",
    "description": "Deletes vertices,faces,edges depending on what selection mode youre in",
    "author": "OlesenJonas",
    "category": "Edit",
    "blender": (2, 80, 0)
}
 
import bpy
 
 
class AwareDelete(bpy.types.Operator):
    """Selection Aware Delete"""
    bl_idname = "object.work_macro"
    bl_label = "Selection Aware Delete"
    bl_options = {'REGISTER', 'UNDO'}
 
 
    def execute(self, context):
 
        scn = bpy.context.scene
 
        if tuple(scn.tool_settings.mesh_select_mode)[0] == True:
            bpy.ops.mesh.delete(type="VERT")
        elif tuple(scn.tool_settings.mesh_select_mode)[1] == True:
            bpy.ops.mesh.delete(type="EDGE")
        elif tuple(scn.tool_settings.mesh_select_mode)[2] == True:
            bpy.ops.mesh.delete(type="FACE")
   
        return {'FINISHED'}
 
 
addon_keymaps = []
 
 
def register():
    bpy.utils.register_class(AwareDelete)
 
    #add to keymap
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Mesh', space_type='EMPTY')
    kmi = km.keymap_items.new(AwareDelete.bl_idname, 'X', 'PRESS', ctrl=True, shift=True)
    addon_keymaps.append(km)
 
def unregister():
    bpy.utils.unregister_class(AwareDelete)
 
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        wm.keyconfigs.addon.keymaps.remove(km)
    # delete Keymap
    del addon_keymaps[:]
 
 
if __name__ == "__main__":
    register()
