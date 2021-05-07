import bpy
from bpy.types import Operator
from .myPackage.Femur_functions import copy_object, join_obj, make_axis, join_obj, vertex_group, save_orientation_InEditMode, shrinkwrap_obj, cursor_to_obj, add_plane, delete_obj, move_to_collection, transform_to_orientation, unhide_list, check_obj_list

class FEMUR_OT_ValgusAngle(Operator):
    """ """
    bl_label = "Valgus Angle"
    bl_idname = "object.valgusangle"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        unhide_list(["Valgus Angle", 'Anatomical Point P:Cor', 'Hip Center', 'Femur Center'])
        
        try:
            delete_obj(bpy.data.objects["Valgus Angle"])
        except:
            pass

        check_list = check_obj_list(['Anatomical Point P:Cor', 'Hip Center', 'Femur Center'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Anatomical Point P:Cor'], 'Anatomical Point P:Cor for valgus angle')
            copy_object(bpy.data.objects['Hip Center'], 'Hip Center for valgus angle')
            copy_object(bpy.data.objects['Femur Center'], 'Femur Center for valgus angle')

            join_obj([bpy.data.objects["Anatomical Point P:Cor for valgus angle"], bpy.data.objects["Hip Center for valgus angle"], bpy.data.objects["Femur Center for valgus angle"]], "Valgus Angle")
        
            move_to_collection("Measurements", bpy.data.objects["Valgus Angle"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class FEMUR_OT_NSACoronal(Operator):
    """ """
    bl_label = "NSA in Coronal Plane"
    bl_idname = "object.nsacoronal"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):

        unhide_list(["NSA in Coronal Plane", 'Hip Center', 'Neck Center P:Cor', 'GT P:Cor', 'Femur Center'])
         
        try:
            delete_obj(bpy.data.objects["NSA in Coronal Plane"])
        except:
            pass
        
        check_list = check_obj_list(['Hip Center', 'Neck Center P:Cor', 'GT P:Cor', 'Femur Center'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Hip Center'], 'Hip Center for NSACoronal L1')
            copy_object(bpy.data.objects['Neck Center P:Cor'], 'Neck Center P:Cor for NSACoronal L1')
        

            copy_object(bpy.data.objects['GT P:Cor'], 'GT P:Cor for NSACoronal L2')
            copy_object(bpy.data.objects['Femur Center'], 'Femur Center for NSACoronal L2')
        
            make_axis([bpy.data.objects['Hip Center for NSACoronal L1'], bpy.data.objects['Neck Center P:Cor for NSACoronal L1']],  "NSACoronal Line1")
            make_axis([bpy.data.objects['GT P:Cor for NSACoronal L2'], bpy.data.objects['Femur Center for NSACoronal L2']],  "NSACoronal Line2")
        
            join_obj([bpy.data.objects["NSACoronal Line1"], bpy.data.objects["NSACoronal Line2"]], "NSA in Coronal Plane")

            vertex_group(bpy.data.objects['NSA in Coronal Plane'])
        
            copy_object(bpy.data.objects['Hip Center'], 'Hip Center for NSAcoronal')
            copy_object(bpy.data.objects['Femur Center'], 'Femur Center for NSAcoronal')
            join_obj([bpy.data.objects["NSA in Coronal Plane"], bpy.data.objects["Hip Center for NSAcoronal"], bpy.data.objects["Femur Center for NSAcoronal"]], "NSA in Coronal Plane")

            move_to_collection("Measurements", bpy.data.objects["NSA in Coronal Plane"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}

    
class FEMUR_OT_NSASagittal(Operator):
    """ """
    bl_label = "NSA in Sagittal Plane"
    bl_idname = "object.nsasagittal"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        unhide_list(["NSA in Sagittal Plane", 'Hip Center', 'Neck Center P:Sag', 'Femur Center', 'GT P:Sag'])
          
        try:
            delete_obj(bpy.data.objects["NSA in Sagittal Plane"])
        except:
            pass

        check_list = check_obj_list(['Hip Center', 'Neck Center P:Sag', 'Femur Center', 'GT P:Sag'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Hip Center'], 'Hip Center for NSASagittal L1')
            copy_object(bpy.data.objects['Neck Center P:Sag'], 'Neck Center P:Sag for NSASagittal L1')

            copy_object(bpy.data.objects['Femur Center'], 'Femur Center for NSASagittal L2')
            copy_object(bpy.data.objects['GT P:Sag'], 'GT P:Sag for NSASagittal L2')

            make_axis([bpy.data.objects['Hip Center for NSASagittal L1'] , bpy.data.objects['Neck Center P:Sag for NSASagittal L1']], "NSASagittal L1")
            make_axis([bpy.data.objects['Femur Center for NSASagittal L2'] , bpy.data.objects['GT P:Sag for NSASagittal L2']], "NSASagittal L2")
       
            join_obj([bpy.data.objects['NSASagittal L1'], bpy.data.objects['NSASagittal L2']], "NSA in Sagittal Plane")
        
            vertex_group(bpy.data.objects['NSA in Sagittal Plane'])

            copy_object(bpy.data.objects['Hip Center'], 'Hip Center for NSASagittal')
            copy_object(bpy.data.objects['GT P:Sag'], 'GT P:Sag for NSASagittal')
            join_obj([bpy.data.objects["NSA in Sagittal Plane"], bpy.data.objects['Hip Center for NSASagittal'], bpy.data.objects['GT P:Sag for NSASagittal']], "NSA in Sagittal Plane")
        
            move_to_collection("Measurements", bpy.data.objects["NSA in Sagittal Plane"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class FEMUR_OT_mLDFA(Operator):
    """ """
    bl_label = "mLDFA"
    bl_idname = "object.mldfa"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        try:
            unhide_list(["mLDFA", 'Lateral Distal P:Cor', 'Medial Distal P:Cor', 'Mechanical Axis'])
        except:
            pass  
        
        try:
            delete_obj(bpy.data.objects["mLDFA"])
        except:
            pass
        
        check_list = check_obj_list(['Lateral Distal P:Cor', 'Medial Distal P:Cor', 'Mechanical Axis'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Lateral Distal P:Cor'], 'Lateral Distal P:Cor for mLDFA L1')
            copy_object(bpy.data.objects['Medial Distal P:Cor'], 'Medial Distal P:Cor for mLDFA L1')

            make_axis([bpy.data.objects['Lateral Distal P:Cor for mLDFA L1'], bpy.data.objects['Medial Distal P:Cor for mLDFA L1']], "mLDFA Line1")
        
            copy_object(bpy.data.objects['Mechanical Axis'], 'Mechanical Axis for mLDFA L2')
            join_obj([bpy.data.objects['mLDFA Line1'], bpy.data.objects['Mechanical Axis for mLDFA L2']], "mLDFA")
        
            vertex_group(bpy.data.objects['mLDFA'])
        
            copy_object(bpy.data.objects['Hip Center'], 'Hip Center for mLDFA')
            copy_object(bpy.data.objects['Medial Distal P:Cor'], 'Medial Distal P:Cor for mLDFA')
            join_obj([bpy.data.objects["mLDFA"], bpy.data.objects['Hip Center for mLDFA'], bpy.data.objects['Medial Distal P:Cor for mLDFA']], "mLDFA")
        
            move_to_collection("Measurements", bpy.data.objects["mLDFA"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class FEMUR_OT_mLPFA(Operator):
    """ """
    bl_label = "mLPFA"
    bl_idname = "object.mlpfa"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        unhide_list(['mLPFA', 'GT P:Cor', 'Hip Center', 'Femur Center'])
        
        try:
            delete_obj(bpy.data.objects['mLPFA'])
        except:
            pass

        check_list = check_obj_list(['GT P:Cor', 'Hip Center','Femur Center'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['GT P:Cor'], 'GT P:Cor for mLPFA')
            copy_object(bpy.data.objects['Hip Center'], 'Hip Center for mLPFA')
            copy_object(bpy.data.objects['Femur Center'], 'Femur Center for mLPFA')
        
            join_obj([bpy.data.objects['GT P:Cor for mLPFA'], bpy.data.objects['Hip Center for mLPFA'], bpy.data.objects['Femur Center for mLPFA']], "mLPFA")
        
            move_to_collection("Measurements", bpy.data.objects['mLPFA'])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class FEMUR_OT_aMPFA(Operator):
    """ """
    bl_label = "aMPFA"
    bl_idname = "object.ampfa"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        try:
            unhide_list(['aMPFA', 'Hip Center', 'GT P:Cor', 'Femur Center', 'Anatomical Point P:Cor'])
        except:
            pass
        
        try:
            delete_obj(bpy.data.objects['aMPFA'])
        except:
            pass
        
        check_list = check_obj_list(['Hip Center', 'GT P:Cor', 'Femur Center', 'Anatomical Point P:Cor'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Hip Center'], 'Hip Center for aMPFA L1')
            copy_object(bpy.data.objects['GT P:Cor'], 'GT P:Cor for aMPFA L1')
            make_axis([bpy.data.objects['Hip Center for aMPFA L1'], bpy.data.objects['GT P:Cor for aMPFA L1']], "aMPFA Line1")
        
            copy_object(bpy.data.objects['Femur Center'], 'Femur Center for aMPFA L2')
            copy_object(bpy.data.objects['Anatomical Point P:Cor'], 'Anatomical Point P:Cor for aMPFA L2')
            make_axis([bpy.data.objects['Femur Center for aMPFA L2'], bpy.data.objects['Anatomical Point P:Cor for aMPFA L2']], "aMPFA Line2")
        
            join_obj([bpy.data.objects['aMPFA Line1'], bpy.data.objects['aMPFA Line2']], "aMPFA")
        
            vertex_group(bpy.data.objects['aMPFA'])
        
            copy_object(bpy.data.objects['Hip Center'], 'Hip Center for aMPFA')
            copy_object(bpy.data.objects['Femur Center'], 'Femur Center for aMPFA')
            join_obj([bpy.data.objects['aMPFA'], bpy.data.objects['Hip Center for aMPFA'], bpy.data.objects['Femur Center for aMPFA']], 'aMPFA')
        
            move_to_collection("Measurements", bpy.data.objects['aMPFA'])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class FEMUR_OT_aLDFA(Operator):
    """ """
    bl_label = "aLDFA"
    bl_idname = "object.aldfa"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
       
        unhide_list(['aLDFA', 'Medial Distal P:Cor', 'Lateral Distal P:Cor', 'Anatomical Point P:Cor', 'Femur Center'])
        
        try:
            delete_obj(bpy.data.objects['aLDFA'])
        except:
            pass

        check_list = check_obj_list(['Medial Distal P:Cor', 'Lateral Distal P:Cor', 'Anatomical Point P:Cor', 'Femur Center'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Medial Distal P:Cor'],'Medial Distal P:Cor for aLDFA L1')
            copy_object(bpy.data.objects['Lateral Distal P:Cor'], 'Lateral Distal P:Cor for aLDFA L1')
            make_axis([bpy.data.objects['Medial Distal P:Cor for aLDFA L1'], bpy.data.objects['Lateral Distal P:Cor for aLDFA L1']], "aLDFA L1")

            copy_object(bpy.data.objects['Anatomical Point P:Cor'], 'Anatomical Point P:Cor for aLDFA L2')
            copy_object(bpy.data.objects['Femur Center'], 'Femur Center for aLDFA L2')
            make_axis([bpy.data.objects['Anatomical Point P:Cor for aLDFA L2'], bpy.data.objects['Femur Center for aLDFA L2']], "aLDFA L2")

            join_obj([bpy.data.objects["aLDFA L1"],bpy.data.objects["aLDFA L2"]], "aLDFA") 
            vertex_group(bpy.data.objects['aLDFA'])
        
            copy_object(bpy.data.objects['Anatomical Point P:Cor'], 'Anatomical Point P:Cor for aLDFA')
            copy_object(bpy.data.objects['Medial Distal P:Cor'], 'Medial Distal P:Cor for aLDFA')
            join_obj([bpy.data.objects["aLDFA"], bpy.data.objects['Anatomical Point P:Cor for aLDFA'], bpy.data.objects['Medial Distal P:Cor for aLDFA']],"aLDFA")

            move_to_collection("Measurements", bpy.data.objects['aLDFA'])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class FEMUR_OT_MidshaftVarusInCoronalPlane(Operator):
    """ """
    bl_label = "Midshaft Varus Coronal Plane"
    bl_idname = "object.midshaftvaruscoronalplane"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):

        unhide_list(["Midshaft Varus Coronal Plane", 'GT P:Cor', 'Midshaft Femur Center P:Cor', 'Femur Center'])
        
        try:
            delete_obj(bpy.data.objects["Midshaft Varus Coronal Plane"])
        except:
            pass

        check_list = check_obj_list(['GT P:Cor', 'Midshaft Femur Center P:Cor', 'Femur Center'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['GT P:Cor'], 'GT P:Cor for MidshaftVarusInCoronalPlane')
            copy_object(bpy.data.objects['Midshaft Femur Center P:Cor'], 'Midshaft Femur Center P:Cor for MidshaftVarusInCoronalPlane')
            copy_object(bpy.data.objects['Femur Center'], 'Femur Center for MidshaftVarusInCoronalPlane')

            join_obj([bpy.data.objects['GT P:Cor for MidshaftVarusInCoronalPlane'], bpy.data.objects['Midshaft Femur Center P:Cor for MidshaftVarusInCoronalPlane'], bpy.data.objects['Femur Center for MidshaftVarusInCoronalPlane']], "Midshaft Varus Coronal Plane")
        
            move_to_collection("Measurements", bpy.data.objects["Midshaft Varus Coronal Plane"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class FEMUR_OT_MidshaftBowInSagittalPlane(Operator):
    """ """
    bl_label = "Midshaft Bow Sagittal Plane"
    bl_idname = "object.midshaftbowsagittalplane"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        unhide_list(["Midshaft Bow Sagittal Plane", 'GT P:Sag', 'Midshaft Femur Center P:Sag', 'Femur Center'])
        
        try:
            delete_obj(bpy.data.objects["Midshaft Bow Sagittal Plane"])
        except:
            pass

        check_list = check_obj_list(['GT P:Sag', 'Midshaft Femur Center P:Sag', 'Femur Center'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['GT P:Sag'], 'GT P:Sag for MidshaftBowInSagittalPlane')
            copy_object(bpy.data.objects['Midshaft Femur Center P:Sag'], 'Midshaft Femur Center P:Sag for MidshaftBowInSagittalPlane')
            copy_object(bpy.data.objects['Femur Center'], 'Femur Center for MidshaftBowInSagittalPlane')

            join_obj([bpy.data.objects['GT P:Sag for MidshaftBowInSagittalPlane'], bpy.data.objects['Midshaft Femur Center P:Sag for MidshaftBowInSagittalPlane'], bpy.data.objects['Femur Center for MidshaftBowInSagittalPlane']], "Midshaft Bow Sagittal Plane")
        
            move_to_collection("Measurements", bpy.data.objects["Midshaft Bow Sagittal Plane"]) 
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class FEMUR_OT_DistalFemurValgusCoronalPlane(Operator):
    """ """
    bl_label = "Distal Femur Valgus Coronal Plane"
    bl_idname = "object.distalfemurvalguscoronalplane"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        try:
            unhide_list(["Distal Femur Valgus Coronal Plane", 'Midshaft Femur Center P:Cor', 'Femur Center', 'Hip Center'])
        except:
            pass
        
        try:
            delete_obj(bpy.data.objects["Distal Femur Valgus Coronal Plane"])
        except:
            pass

        check_list = check_obj_list(['Midshaft Femur Center P:Cor', 'Femur Center', 'Hip Center'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Midshaft Femur Center P:Cor'], 'Midshaft Femur Center P:Cor for DistalFemurValgusCoronalPlane')
            copy_object(bpy.data.objects['Femur Center'], 'Femur Center for DistalFemurValgusCoronalPlane')
            copy_object(bpy.data.objects['Hip Center'], 'Hip Center for DistalFemurValgusCoronalPlane')

            join_obj([bpy.data.objects['Midshaft Femur Center P:Cor for DistalFemurValgusCoronalPlane'], bpy.data.objects['Femur Center for DistalFemurValgusCoronalPlane'], bpy.data.objects['Hip Center for DistalFemurValgusCoronalPlane']], "Distal Femur Valgus Coronal Plane")
        
            move_to_collection("Measurements", bpy.data.objects["Distal Femur Valgus Coronal Plane"]) 
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class FEMUR_OT_DistalFemurFlexionSagittalPlane(Operator):
    """ """
    bl_label = "Distal Femur Flexion Sagittal Plane"
    bl_idname = "object.distalfemurflexionsagittalplane"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
       
        unhide_list(["Distal Femur Flexion Sagittal Plane", 'Midshaft Femur Center P:Sag', 'Femur Center', 'Hip Center'])
       
        try:
            delete_obj(bpy.data.objects["Distal Femur Flexion Sagittal Plane"])
        except:
            pass

        check_list = check_obj_list(['Midshaft Femur Center P:Sag', 'Femur Center', 'Hip Center'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Midshaft Femur Center P:Sag'], 'Midshaft Femur Center P:Sag for DistalFemurFlexionSagittalPlane')
            copy_object(bpy.data.objects['Femur Center'], 'Femur Center for DistalFemurFlexionSagittalPlane')
            copy_object(bpy.data.objects['Hip Center'], 'Hip Center for DistalFemurFlexionSagittalPlane')

            join_obj([bpy.data.objects['Midshaft Femur Center P:Sag for DistalFemurFlexionSagittalPlane'], bpy.data.objects['Femur Center for DistalFemurFlexionSagittalPlane'], bpy.data.objects['Hip Center for DistalFemurFlexionSagittalPlane']], "Distal Femur Flexion Sagittal Plane")
    
            move_to_collection("Measurements", bpy.data.objects["Distal Femur Flexion Sagittal Plane"]) 
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class FEMUR_OT_ProximalFemurVarusCoronalPlane(Operator):
    """ """
    bl_label = "Proximal Femur Varus Coronal Plane"
    bl_idname = "object.proximalfemurvaruscoronalplane"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        unhide_list(["Proximal Femur Varus Coronal Plane", 'Midshaft Femur Center P:Cor', 'GT P:Cor', 'Neck Center P:Cor', 'Hip Center'])
        
        try:
            delete_obj(bpy.data.objects["Proximal Femur Varus Coronal Plane"])
        except:
            pass

        check_list = check_obj_list(['Midshaft Femur Center P:Cor', 'GT P:Cor', 'Neck Center P:Cor', 'Hip Center'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Midshaft Femur Center P:Cor'], 'Midshaft Femur Center P:Cor for ProximalVarusCoronalPlane L1')
            copy_object(bpy.data.objects['GT P:Cor'],'GT P:Cor for ProximalVarusCoronalPlane L1' )
            make_axis([bpy.data.objects['Midshaft Femur Center P:Cor for ProximalVarusCoronalPlane L1'], bpy.data.objects['GT P:Cor for ProximalVarusCoronalPlane L1']], "ProximalVarusCoronalPlane L1")
        
            copy_object(bpy.data.objects['Neck Center P:Cor'], 'Neck Center P:Cor for ProximalVarusCoronalPlane L2')
            copy_object(bpy.data.objects['Hip Center'], 'Hip Center for ProximalVarusCoronalPlane L2')
            make_axis([bpy.data.objects['Neck Center P:Cor for ProximalVarusCoronalPlane L2'], bpy.data.objects['Hip Center for ProximalVarusCoronalPlane L2']], "ProximalVarusCoronalPlane L2")
        
            join_obj([bpy.data.objects["ProximalVarusCoronalPlane L1"], bpy.data.objects["ProximalVarusCoronalPlane L2"]], "Proximal Femur Varus Coronal Plane")
        
            vertex_group( bpy.data.objects["Proximal Femur Varus Coronal Plane"])
        
            copy_object(bpy.data.objects['Hip Center'], 'Hip Center ProximalVarusCoronalPlane')
            copy_object(bpy.data.objects['Midshaft Femur Center P:Cor'], 'Midshaft Femur Center P:Cor ProximalVarusCoronal')

            join_obj([bpy.data.objects["Proximal Femur Varus Coronal Plane"], bpy.data.objects['Hip Center ProximalVarusCoronalPlane'], bpy.data.objects['Midshaft Femur Center P:Cor ProximalVarusCoronal']], "Proximal Femur Varus Coronal Plane")

            move_to_collection("Measurements", bpy.data.objects["Proximal Femur Varus Coronal Plane"]) 
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class FEMUR_OT_ProximalFemurFlexionSagittalPlane(Operator):
    """ """
    bl_label = "Proximal Femur Flexion Sagittal Plane"
    bl_idname = "object.proximalfemurflexionsagittalplane"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        unhide_list(["Proximal Femur Flexion Sagittal Plane", 'Midshaft Femur Center P:Sag', 'GT P:Sag', 'Neck Center P:Sag', 'Hip Center'])
        
        try:
            delete_obj(bpy.data.objects["Proximal Femur Flexion Sagittal Plane"])
        except:
            pass

        check_list = check_obj_list(['Midshaft Femur Center P:Sag', 'GT P:Sag', 'Neck Center P:Sag', 'Hip Center'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Midshaft Femur Center P:Sag'], 'Midshaft Femur Center P:Sag ProximalFlexionSagittalPlane L1')
            copy_object(bpy.data.objects['GT P:Sag'], 'GT P:Sag ProximalFlexionSagittalPlane L1')
            make_axis([bpy.data.objects['Midshaft Femur Center P:Sag ProximalFlexionSagittalPlane L1'], bpy.data.objects['GT P:Sag ProximalFlexionSagittalPlane L1']], "Proximal Femur Flexion Sagittal Plane L1")
        
            copy_object(bpy.data.objects['Neck Center P:Sag'], 'Neck Center P:Sag for ProximalFemurFlexionSagittalPlane L2')
            copy_object(bpy.data.objects['Hip Center'], 'Hip Center for ProximalFemurFlexionSagittalPlane L2')
            make_axis([bpy.data.objects['Neck Center P:Sag for ProximalFemurFlexionSagittalPlane L2'], bpy.data.objects['Hip Center for ProximalFemurFlexionSagittalPlane L2']], "Proximal Femur Flexion Sagittal Plane L2")
        
            join_obj([bpy.data.objects["Proximal Femur Flexion Sagittal Plane L1"], bpy.data.objects["Proximal Femur Flexion Sagittal Plane L2"]], "Proximal Femur Flexion Sagittal Plane")
        
            vertex_group(bpy.data.objects['Proximal Femur Flexion Sagittal Plane'])
        
            copy_object(bpy.data.objects['Hip Center'], 'Hip Center for ProximalFemurFlexionSagittalPlane')
            copy_object(bpy.data.objects['GT P:Sag'], 'GT P:Sag for ProximalFemurFlexionSagittalPlane')

            join_obj([bpy.data.objects["Proximal Femur Flexion Sagittal Plane"], bpy.data.objects['Hip Center for ProximalFemurFlexionSagittalPlane'], bpy.data.objects['GT P:Sag for ProximalFemurFlexionSagittalPlane']], "Proximal Femur Flexion Sagittal Plane")
        
            move_to_collection("Measurements", bpy.data.objects["Proximal Femur Flexion Sagittal Plane"]) 
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class FEMUR_OT_CondylarDifferenceCoronalPlane(Operator):
    """ """
    bl_label = "Condylar difference of knee in coronal plane"
    bl_idname = "object.condylardifferencecoronalplane"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        unhide_list(["Condylar difference in coronal plane", 'Lateral Distal P:Cor', "Sagittal Plane", 'Medial Distal P:Cor'])
        
        try:
            delete_obj(bpy.data.objects["Condylar difference in coronal plane"])
        except:
            pass
        
        check_list = check_obj_list(['Lateral Distal P:Cor', "Sagittal Plane", 'Medial Distal P:Cor'])
        if len(check_list) == 0:
            save_orientation_InEditMode(bpy.data.objects['Distal Plane'], "FACE")

            copy_object(bpy.data.objects['Lateral Distal P:Cor'], "Lateral Distal P:Cor_Sag")
            shrinkwrap_obj(bpy.data.objects["Lateral Distal P:Cor_Sag"], bpy.data.objects["Sagittal Plane"])
        
            cursor_to_obj(bpy.data.objects['Lateral Distal P:Cor_Sag'])
            add_plane("CondylarDifferenceCoronalPlane P1")
            transform_to_orientation()

            copy_object(bpy.data.objects['Medial Distal P:Cor'], "Medial Distal P:Cor_Sag")
            shrinkwrap_obj(bpy.data.objects["Medial Distal P:Cor_Sag"], bpy.data.objects["Sagittal Plane"])
        
            cursor_to_obj(bpy.data.objects["Medial Distal P:Cor_Sag"])
            add_plane("CondylarDifferenceCoronalPlane P2")
            transform_to_orientation()
        
            join_obj([bpy.data.objects["CondylarDifferenceCoronalPlane P1"], bpy.data.objects["CondylarDifferenceCoronalPlane P2"]], "Condylar difference in coronal plane")
        
            delete_obj(bpy.data.objects['Lateral Distal P:Cor_Sag'])
            delete_obj(bpy.data.objects['Medial Distal P:Cor_Sag'])
    
            move_to_collection("Measurements", bpy.data.objects["Condylar difference in coronal plane"]) 
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class FEMUR_OT_CondylarDifferenceTransversePlane(Operator):
    """ """
    bl_label = "Posterior Condylar difference in transverse plane"
    bl_idname = "object.condylardifferencetransverseplane"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        unhide_list(["Posterior Condylar difference in transverse plane", 'Posterior Medial Point P:Dis', 'Posterior Lateral Point P:Dis', "Sagittal Plane"])
        
        try:
            delete_obj(bpy.data.objects["Posterior Condylar difference in transverse plane"])
        except:
            pass

        check_list = check_obj_list(['Posterior Medial Point P:Dis', 'Posterior Lateral Point P:Dis', "Sagittal Plane"])
        if len(check_list) == 0:
            save_orientation_InEditMode(bpy.data.objects['Coronal Plane'], "FACE")

            copy_object(bpy.data.objects['Posterior Medial Point P:Dis'], "Posterior Medial Point P:Cor_Sag")
            shrinkwrap_obj(bpy.data.objects["Posterior Medial Point P:Cor_Sag"], bpy.data.objects["Sagittal Plane"])
        
            cursor_to_obj(bpy.data.objects["Posterior Medial Point P:Cor_Sag"])
            add_plane("Posterior Condylar difference in transverse plane P1")
            transform_to_orientation()

            copy_object(bpy.data.objects['Posterior Lateral Point P:Dis'], "Posterior Lateral Point P:Dis_Sag")
            shrinkwrap_obj(bpy.data.objects["Posterior Lateral Point P:Dis_Sag"], bpy.data.objects["Sagittal Plane"])
        
            cursor_to_obj(bpy.data.objects["Posterior Lateral Point P:Dis_Sag"])
            add_plane("Posterior Condylar difference in transverse plane P2")
            transform_to_orientation()
        
            join_obj([bpy.data.objects["Posterior Condylar difference in transverse plane P1"], bpy.data.objects["Posterior Condylar difference in transverse plane P2"]], "Posterior Condylar difference in transverse plane")
        
            delete_obj(bpy.data.objects['Posterior Medial Point P:Cor_Sag'])
            delete_obj(bpy.data.objects['Posterior Lateral Point P:Dis_Sag'])
    
            move_to_collection("Measurements", bpy.data.objects["Posterior Condylar difference in transverse plane"]) 
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class FEMUR_OT_RotationalAngle(Operator):
    """ """
    bl_label = "Rotational Angle"
    bl_idname = "object.rotationalangle"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context): 
      
        unhide_list(["Rotational Angle", 'Medial Epicondyle P:Dis', 'Lateral Epicondyle P:Dis', 'Posterior Medial Point P:Dis', 'Posterior Lateral Point P:Dis'])
        
        try:
            delete_obj(bpy.data.objects["Rotational Angle"])
        except:
            pass

        check_list = check_obj_list(['Medial Epicondyle P:Dis', 'Lateral Epicondyle P:Dis', 'Posterior Medial Point P:Dis', 'Posterior Lateral Point P:Dis'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Medial Epicondyle P:Dis'], 'Medial Epicondyle P:Dis for RotationalAngle L1')
            copy_object(bpy.data.objects['Lateral Epicondyle P:Dis'], 'Lateral Epicondyle P:Dis for RotationalAngle L1')
            make_axis([bpy.data.objects['Medial Epicondyle P:Dis for RotationalAngle L1'], bpy.data.objects['Lateral Epicondyle P:Dis for RotationalAngle L1']], "RotationalAngle L1")
        
            copy_object(bpy.data.objects['Posterior Medial Point P:Dis'], 'Posterior Medial Point P:Dis for RotationalAngle L2')
            copy_object(bpy.data.objects['Posterior Lateral Point P:Dis'], 'Posterior Lateral Point P:Dis for RotationalAngle L2')
            make_axis([bpy.data.objects['Posterior Medial Point P:Dis for RotationalAngle L2'], bpy.data.objects['Posterior Lateral Point P:Dis for RotationalAngle L2']], "RotationalAngle L2")

            join_obj([bpy.data.objects["RotationalAngle L1"], bpy.data.objects["RotationalAngle L2"]], "Rotational Angle")
        
            vertex_group(bpy.data.objects["Rotational Angle"])
        
            copy_object(bpy.data.objects['Posterior Medial Point P:Dis'], 'Posterior Medial Point P:Dis for RotationalAngle')
            copy_object(bpy.data.objects['Medial Epicondyle P:Dis'], 'Medial Epicondyle P:Dis for RotationalAngle')
        
            join_obj([bpy.data.objects["Rotational Angle"], bpy.data.objects['Posterior Medial Point P:Dis for RotationalAngle'], bpy.data.objects['Medial Epicondyle P:Dis for RotationalAngle']], "Rotational Angle")

            move_to_collection("Measurements", bpy.data.objects["Rotational Angle"]) 
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class FEMUR_OT_FemurTorsionalAngle(Operator):
    """ """
    bl_label = "Femur torsional angle"
    bl_idname = "object.femurtorsionalangle"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context): 
        
        unhide_list(['Femur torsional angle', 'Hip Center P:Dis', 'Neck Center P:Dis', 'Posterior Medial Point P:Dis', 'Posterior Lateral Point P:Dis'])
        
        try:
            delete_obj(bpy.data.objects['Femur torsional angle'])
        except:
            pass

        check_list = check_obj_list(['Hip Center P:Dis', 'Neck Center P:Dis', 'Posterior Medial Point P:Dis', 'Posterior Lateral Point P:Dis'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Hip Center P:Dis'], 'Hip Center P:Dis for FemurTorsionalAngle L1')
            copy_object(bpy.data.objects['Neck Center P:Dis'], 'Neck Center P:Dis for FemurTorsionalAngle L1')
            make_axis([bpy.data.objects['Hip Center P:Dis for FemurTorsionalAngle L1'], bpy.data.objects['Neck Center P:Dis for FemurTorsionalAngle L1']],"FemurTorsionalAngle L1")

            copy_object(bpy.data.objects['Posterior Medial Point P:Dis'], 'Posterior Medial Point P:Dis for FemurTorsionalAngle L2')
            copy_object(bpy.data.objects['Posterior Lateral Point P:Dis'], 'Posterior Lateral Point P:Dis for FemurTorsionalAngle L2')
            make_axis([bpy.data.objects['Posterior Medial Point P:Dis for FemurTorsionalAngle L2'], bpy.data.objects['Posterior Lateral Point P:Dis for FemurTorsionalAngle L2']],"FemurTorsionalAngle L2")
        
            join_obj([bpy.data.objects["FemurTorsionalAngle L1"], bpy.data.objects["FemurTorsionalAngle L2"]], 'Femur torsional angle') 
       
            vertex_group(bpy.data.objects['Femur torsional angle'])
        
            copy_object(bpy.data.objects['Hip Center P:Dis'], 'Hip Center P:Dis for FemurTorsionalAngle')
            copy_object(bpy.data.objects['Posterior Medial Point P:Dis'], 'Posterior Medial Point P:Dis for FemurTorsionalAngle')
            join_obj([bpy.data.objects['Femur torsional angle'], bpy.data.objects['Hip Center P:Dis for FemurTorsionalAngle'], bpy.data.objects['Posterior Medial Point P:Dis for FemurTorsionalAngle']], "Femur torsional angle")

            move_to_collection("Measurements", bpy.data.objects['Femur torsional angle']) 
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}