import bpy
from bpy.types import Panel

class FEMUR_PT_Angles(Panel):
    """ """
    bl_label = "Angles"
    bl_idname = "femur_PT_angles"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Femur"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("object.valgusangle")
        row = layout.row()
        row.operator("object.nsacoronal")
        row = layout.row()
        row.operator("object.nsasagittal")
        row = layout.row()
        row.operator("object.mldfa")
        row = layout.row()
        row.operator("object.mlpfa")
        row = layout.row()
        row.operator("object.ampfa")
        row = layout.row()
        row.operator("object.aldfa")
        row = layout.row()
        row.operator("object.midshaftvaruscoronalplane")
        row = layout.row()
        row.operator("object.midshaftbowsagittalplane")
        row = layout.row()
        row.operator("object.distalfemurvalguscoronalplane")
        row = layout.row()
        row.operator("object.distalfemurflexionsagittalplane")
        row = layout.row()
        row.operator("object.proximalfemurvaruscoronalplane")
        row = layout.row()
        row.operator("object.proximalfemurflexionsagittalplane")
        row = layout.row()
        row.operator("object.condylardifferencecoronalplane")
        row = layout.row()
        row.operator("object.condylardifferencetransverseplane")
        row = layout.row()
        row.operator("object.rotationalangle")
        row = layout.row()
        row.operator("object.femurtorsionalangle")