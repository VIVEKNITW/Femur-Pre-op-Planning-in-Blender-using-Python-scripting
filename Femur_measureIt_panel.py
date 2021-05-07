import bpy
from bpy.types import Panel

class MyProperty(bpy.types.PropertyGroup):
    my_bool : bpy.props.BoolProperty(
        name="Enable or Disable",
        description="For measureIt enbling/disabling",
        default = False
        )

class FEMUR_PT_MeasureIt(Panel):
    """ """
    bl_label = "Measurit"
    bl_idname = "femur_PT_measureit"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Femur"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        row = layout.row()
        layout.prop(mytool, "my_bool", text="Tick box")
        row = layout.row()
        row.operator("object.enabledisablemeasureit", text = "Enable/Disable Measureit")
        row = layout.row()
        row.operator("measureit.addangle", text = "Angle")
        row = layout.row()
        row.operator("measureit.addsegment",text = "Distance")
        row = layout.row()
        row.operator("measureit.runopengl", text = "Show/Hide")
        row = layout.row()
        row.operator("measureit.deleteallsegment", text = "Delete")
        