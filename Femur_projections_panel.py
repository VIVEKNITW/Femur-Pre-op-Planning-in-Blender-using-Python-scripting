import bpy
from bpy.types import Panel

class FEMUR_PT_Projections(Panel):
    """ """
    bl_label = "Projections"
    bl_idname = "femur_PT_projections"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Femur"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("object.projections")