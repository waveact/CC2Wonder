import bpy

class CC2WonderPanel(bpy.types.Panel):
    bl_label = "CC2Wonder"
    bl_idname = "CC_PT_cc2wonder_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'CC2Wonder'
    #bl_context = "object"

    def draw(self, context):
        layout = self.layout
        #layout.label("Save")
        #layout.operator("object.cc2wonder_action", text="Save black.jpg")
        #box = layout.box()
        #box.label(text="Importing", icon="IMPORT")
        row = layout.row()
        #row.scale_y = 2
        #op = row.operator("cc3.importer", icon="OUTLINER_OB_ARMATURE", text="Import Character")
        op = row.operator("object.cc2wonder_action", text="Export to Wonder")
        #op.param = "IMPORT"

def register():
    bpy.utils.register_class(CC2WonderPanel)

def unregister():
    bpy.utils.unregister_class(CC2WonderPanel)
    