import bpy
from bpy.types import Panel

class FEMUR_PT_Landmark_assignment(Panel):
    """ """
    bl_label = "Landmarks & axes"
    bl_idname = "femur_PT_landmarkassignment"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Femur"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("object.hipcenter")
        row.operator("object.femurcenter")
        row = layout.row()
        row.operator("object.mechanicalaxis")
        
        row = layout.row()
        row.operator("object.medialepicondyle")
        row.operator("object.lateralepicondyle")
        row = layout.row()
        row.operator("object.transepicondylaraxis")

        row = layout.row()
        row.operator("object.neckcenter")
        row = layout.row()
        row.operator("object.neckline")

        row = layout.row()
        row.operator("object.greatertrochaner")
        row = layout.row()
        row.operator("object.midshaftfemurcenter")

        row = layout.row()
        row.operator("object.coronalplane")
        row = layout.row()
        row.operator("object.sagittalplane")
        row = layout.row()
        row.operator("object.distalplane")

        row = layout.row()
        row.operator("object.medialdistalpoint")
        row.operator("object.lateraldistalpoint")
        row = layout.row()
        row.operator("object.distaljointline")
        
        row = layout.row()
        row.operator("object.posteriormedialpoint")
        row.operator("object.posteriorlateralpoint")
        row = layout.row()
        row.operator("object.posterircondylaraxis")

        
        row = layout.row()
        row.operator("object.anatomicalpoint")
        row = layout.row()
        row.operator("object.anatomicalaxis")

        row = layout.row()
        row.operator("object.coronalathip")
        row = layout.row()
        row.operator("object.sagittalathip")
        row = layout.row()
        row.operator("object.coronalatmidshaft")
        row = layout.row()
        row.operator("object.sagittalatmidshaft")

