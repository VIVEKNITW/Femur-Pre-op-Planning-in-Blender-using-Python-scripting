import bpy
from bpy.types import Operator
from .myPackage.Femur_functions import copy_object, join_obj, make_axis, join_obj, vertex_group, save_orientation_InEditMode, shrinkwrap_obj, cursor_to_obj, add_plane, delete_obj, move_to_collection, transform_to_orientation, unhide_list, check_obj_list, check_create_collection, remove_doubles, get_coordinates
from .myPackage.Femur_finding_angle import angle_triangle
class FEMUR_OT_ValgusAngle(Operator):
    """ """
    bl_label = "Valgus Angle"
    bl_idname = "object.valgusangle"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        check_create_collection(["Landmarks", "Axes", "Planes", "Projections", "Measurements"])
        unhide_list(["Valgus Angle", 'Anatomical Point P:Cor', 'Hip Center', 'Femur Center'])
        
        try:
            delete_obj(bpy.data.objects["Valgus Angle"])
        except:
            pass

        check_list = check_obj_list(['Anatomical Point P:Cor', 'Femur Center', "Mechanical Axis", 'Hip Center'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Anatomical Point P:Cor'], 'Anatomical Point P:Cor for valgus angle')
            copy_object(bpy.data.objects['Femur Center'], 'Femur Center for valgus angle')
            make_axis([bpy.data.objects['Anatomical Point P:Cor for valgus angle'], bpy.data.objects['Femur Center for valgus angle']], "Valgus angle L1")
            copy_object(bpy.data.objects["Mechanical Axis"], 'Mechanical Axis for valgus angle')

            # coord_values = get_coordinates(['Anatomical Point P:Cor', 'Femur Center', 'Hip Center'])
            # angle = angle_triangle(coord_values[0], coord_values[1], coord_values[2], coord_values[3], coord_values[4], coord_values[5], coord_values[6], coord_values[7], coord_values[8])
            # print("valgus angle = " + angle) 
            
            join_obj([bpy.data.objects['Mechanical Axis for valgus angle'], bpy.data.objects["Valgus angle L1"]], "Valgus Angle")
            remove_doubles(bpy.data.objects["Valgus Angle"])
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

        check_create_collection(["Landmarks", "Axes", "Planes", "Projections", "Measurements"])
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
        
            join_obj([bpy.data.objects["NSACoronal Line1"], bpy.data.objects["NSACoronal Line2"]], "NSAcoronal point")

            vertex_group(bpy.data.objects["NSAcoronal point"])
            copy_object(bpy.data.objects["NSAcoronal point"], "NSAcoronal point copy")
        
            copy_object(bpy.data.objects['Hip Center'], 'Hip Center for NSAcoronal')
            copy_object(bpy.data.objects['Femur Center'], 'Femur Center for NSAcoronal')

            make_axis([bpy.data.objects['Hip Center for NSAcoronal'], bpy.data.objects["NSAcoronal point"]], "NSA in Coronal Plane 1")
            make_axis([bpy.data.objects['Femur Center for NSAcoronal'], bpy.data.objects["NSAcoronal point copy"]], "NSA in Coronal Plane 2")
            join_obj([bpy.data.objects["NSA in Coronal Plane 1"], bpy.data.objects["NSA in Coronal Plane 2"]], "NSA in Coronal Plane")
            remove_doubles(bpy.data.objects["NSA in Coronal Plane"])

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
        
        check_create_collection(["Landmarks", "Axes", "Planes", "Projections", "Measurements"])
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
       
            join_obj([bpy.data.objects['NSASagittal L1'], bpy.data.objects['NSASagittal L2']], "NSASagittal point")
        
            vertex_group(bpy.data.objects["NSASagittal point"])
            copy_object(bpy.data.objects["NSASagittal point"], "NSASagittal point copy")

            copy_object(bpy.data.objects['Hip Center'], 'Hip Center for NSASagittal')
            copy_object(bpy.data.objects['GT P:Sag'], 'GT P:Sag for NSASagittal')
            make_axis([bpy.data.objects["NSASagittal point"], bpy.data.objects['Hip Center for NSASagittal']], "NSA in Sagittal Plane 1")
            make_axis([bpy.data.objects["NSASagittal point copy"], bpy.data.objects['GT P:Sag for NSASagittal']], "NSA in Sagittal Plane 2")
            join_obj([bpy.data.objects["NSA in Sagittal Plane 1"], bpy.data.objects["NSA in Sagittal Plane 2"]], "NSA in Sagittal Plane")
            remove_doubles(bpy.data.objects["NSA in Sagittal Plane"])

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

        check_create_collection(["Landmarks", "Axes", "Planes", "Projections", "Measurements"])
        unhide_list(["mLDFA", 'Lateral Distal P:Cor', 'Medial Distal P:Cor', 'Mechanical Axis'])  
        
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
            join_obj([bpy.data.objects['mLDFA Line1'], bpy.data.objects['Mechanical Axis for mLDFA L2']], "mLDFA point")
        
            vertex_group(bpy.data.objects["mLDFA point"])
            copy_object(bpy.data.objects["mLDFA point"], "mLDFA point copy")
        
            copy_object(bpy.data.objects['Hip Center'], 'Hip Center for mLDFA')
            copy_object(bpy.data.objects['Medial Distal P:Cor'], 'Medial Distal P:Cor for mLDFA')
            make_axis([bpy.data.objects["mLDFA point"], bpy.data.objects['Hip Center for mLDFA']], "mLDFA 1")
            make_axis([bpy.data.objects["mLDFA point copy"], bpy.data.objects['Medial Distal P:Cor for mLDFA']], "mLDFA 2")
            join_obj([bpy.data.objects["mLDFA 1"], bpy.data.objects["mLDFA 2"]], "mLDFA")
            remove_doubles(bpy.data.objects["mLDFA"])

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
        
        check_create_collection(["Landmarks", "Axes", "Planes", "Projections", "Measurements"])
        unhide_list(['mLPFA', 'GT P:Cor', 'Hip Center', 'Femur Center'])
        
        try:
            delete_obj(bpy.data.objects['mLPFA'])
        except:
            pass

        check_list = check_obj_list(['GT P:Cor', 'Hip Center','Femur Center'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['GT P:Cor'], 'GT P:Cor for mLPFA')
            copy_object(bpy.data.objects['Hip Center'], 'Hip Center for mLPFA 1')
            copy_object(bpy.data.objects['Hip Center'], 'Hip Center for mLPFA 2')
            copy_object(bpy.data.objects['Femur Center'], 'Femur Center for mLPFA')

            make_axis([bpy.data.objects['GT P:Cor for mLPFA'], bpy.data.objects['Hip Center for mLPFA 1']], "mLPFA 1")
            make_axis([bpy.data.objects['Femur Center for mLPFA'], bpy.data.objects['Hip Center for mLPFA 2']], "mLPFA 2")
            join_obj([bpy.data.objects["mLPFA 1"], bpy.data.objects["mLPFA 2"]], "mLPFA")
            remove_doubles(bpy.data.objects["mLPFA"])

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

        check_create_collection(["Landmarks", "Axes", "Planes", "Projections", "Measurements"])
        unhide_list(['aMPFA', 'Hip Center', 'GT P:Cor', 'Femur Center', 'Anatomical Point P:Cor'])
        
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
        
            join_obj([bpy.data.objects['aMPFA Line1'], bpy.data.objects['aMPFA Line2']], "aMPFA point")
        
            vertex_group(bpy.data.objects["aMPFA point"])
            copy_object(bpy.data.objects["aMPFA point"], "aMPFA point copy")
        
            copy_object(bpy.data.objects['Hip Center'], 'Hip Center for aMPFA')
            copy_object(bpy.data.objects['Femur Center'], 'Femur Center for aMPFA')
            make_axis([bpy.data.objects["aMPFA point"], bpy.data.objects['Hip Center for aMPFA']], 'aMPFA 1')
            make_axis([bpy.data.objects["aMPFA point copy"], bpy.data.objects['Femur Center for aMPFA']], 'aMPFA 2')
            join_obj([bpy.data.objects['aMPFA 1'], bpy.data.objects['aMPFA 2']], 'aMPFA')
            remove_doubles(bpy.data.objects['aMPFA'])

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
       
        check_create_collection(["Landmarks", "Axes", "Planes", "Projections", "Measurements"])
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

            join_obj([bpy.data.objects["aLDFA L1"],bpy.data.objects["aLDFA L2"]], "aLDFA point") 
            vertex_group(bpy.data.objects["aLDFA point"])
            copy_object(bpy.data.objects["aLDFA point"], "aLDFA point copy")
        
            copy_object(bpy.data.objects['Anatomical Point P:Cor'], 'Anatomical Point P:Cor for aLDFA')
            copy_object(bpy.data.objects['Medial Distal P:Cor'], 'Medial Distal P:Cor for aLDFA')
            make_axis([bpy.data.objects["aLDFA point"], bpy.data.objects['Anatomical Point P:Cor for aLDFA']],"aLDFA 1")
            make_axis([bpy.data.objects["aLDFA point copy"], bpy.data.objects['Medial Distal P:Cor for aLDFA']],"aLDFA 2")
            join_obj([bpy.data.objects["aLDFA 1"], bpy.data.objects["aLDFA 2"]], "aLDFA")
            remove_doubles(bpy.data.objects["aLDFA"])

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

        check_create_collection(["Landmarks", "Axes", "Planes", "Projections", "Measurements"])
        unhide_list(["Midshaft Varus Coronal Plane", 'GT P:Cor', 'Midshaft Femur Center P:Cor', 'Femur Center'])
        
        try:
            delete_obj(bpy.data.objects["Midshaft Varus Coronal Plane"])
        except:
            pass

        check_list = check_obj_list(['GT P:Cor', 'Midshaft Femur Center P:Cor', 'Femur Center'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['GT P:Cor'], 'GT P:Cor for MidshaftVarusInCoronalPlane')
            copy_object(bpy.data.objects['Midshaft Femur Center P:Cor'], 'Midshaft Center P:Cor for MidshaftVarusInCoronalPlane 1')
            copy_object(bpy.data.objects['Midshaft Femur Center P:Cor'], 'Midshaft Center P:Cor for MidshaftVarusInCoronalPlane 2')
            copy_object(bpy.data.objects['Femur Center'], 'Femur Center for MidshaftVarusInCoronalPlane')

            make_axis([bpy.data.objects['GT P:Cor for MidshaftVarusInCoronalPlane'], bpy.data.objects['Midshaft Center P:Cor for MidshaftVarusInCoronalPlane 1']], "MidshaftVarusInCoronalPlane 1")
            make_axis([bpy.data.objects['Femur Center for MidshaftVarusInCoronalPlane'], bpy.data.objects['Midshaft Center P:Cor for MidshaftVarusInCoronalPlane 2']], "MidshaftVarusInCoronalPlane 2")
            join_obj([bpy.data.objects["MidshaftVarusInCoronalPlane 1"], bpy.data.objects["MidshaftVarusInCoronalPlane 2"]], "Midshaft Varus Coronal Plane")
            remove_doubles(bpy.data.objects["Midshaft Varus Coronal Plane"])

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
        
        check_create_collection(["Landmarks", "Axes", "Planes", "Projections", "Measurements"])
        unhide_list(["Midshaft Bow Sagittal Plane", 'GT P:Sag', 'Midshaft Femur Center P:Sag', 'Femur Center'])
        
        try:
            delete_obj(bpy.data.objects["Midshaft Bow Sagittal Plane"])
        except:
            pass

        check_list = check_obj_list(['GT P:Sag', 'Midshaft Femur Center P:Sag', 'Femur Center'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['GT P:Sag'], 'GT P:Sag for MidshaftBowInSagittalPlane')
            copy_object(bpy.data.objects['Midshaft Femur Center P:Sag'], 'Midshaft Center P:Sag for MidshaftBowInSagittalPlane 1')
            copy_object(bpy.data.objects['Midshaft Femur Center P:Sag'], 'Midshaft Center P:Sag for MidshaftBowInSagittalPlane 2')
            copy_object(bpy.data.objects['Femur Center'], 'Femur Center for MidshaftBowInSagittalPlane')

            make_axis([bpy.data.objects['GT P:Sag for MidshaftBowInSagittalPlane'], bpy.data.objects['Midshaft Center P:Sag for MidshaftBowInSagittalPlane 1']], "Midshaft Bow Sagittal Plane 1")
            make_axis([bpy.data.objects['Femur Center for MidshaftBowInSagittalPlane'], bpy.data.objects['Midshaft Center P:Sag for MidshaftBowInSagittalPlane 2']], "Midshaft Bow Sagittal Plane 2")
            join_obj([bpy.data.objects["Midshaft Bow Sagittal Plane 1"], bpy.data.objects["Midshaft Bow Sagittal Plane 2"]], "Midshaft Bow Sagittal Plane")
            remove_doubles(bpy.data.objects["Midshaft Bow Sagittal Plane"])

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

        check_create_collection(["Landmarks", "Axes", "Planes", "Projections", "Measurements"])
        unhide_list(["Distal Femur Valgus Coronal Plane", 'Midshaft Femur Center P:Cor', 'Femur Center', 'Hip Center'])
        
        try:
            delete_obj(bpy.data.objects["Distal Femur Valgus Coronal Plane"])
        except:
            pass

        check_list = check_obj_list(['Midshaft Femur Center P:Cor', 'Femur Center', 'Hip Center'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Midshaft Femur Center P:Cor'], 'Midshaft Center P:Cor for DistalValgusCoronalPlane')
            copy_object(bpy.data.objects['Femur Center'], 'Femur Center for DistalFemurValgusCoronalPlane 1')
            copy_object(bpy.data.objects['Femur Center'], 'Femur Center for DistalFemurValgusCoronalPlane 2')
            copy_object(bpy.data.objects['Hip Center'], 'Hip Center for DistalFemurValgusCoronalPlane')

            make_axis([bpy.data.objects['Femur Center for DistalFemurValgusCoronalPlane 1'], bpy.data.objects['Midshaft Center P:Cor for DistalValgusCoronalPlane']], "DistalFemurValgusCoronalPlane 1")
            make_axis([bpy.data.objects['Femur Center for DistalFemurValgusCoronalPlane 2'], bpy.data.objects['Hip Center for DistalFemurValgusCoronalPlane']], "DistalFemurValgusCoronalPlane 2")
            join_obj([bpy.data.objects["DistalFemurValgusCoronalPlane 1"], bpy.data.objects["DistalFemurValgusCoronalPlane 2"]], "Distal Femur Valgus Coronal Plane")
            remove_doubles(bpy.data.objects["Distal Femur Valgus Coronal Plane"])

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
       
        check_create_collection(["Landmarks", "Axes", "Planes", "Projections", "Measurements"])
        unhide_list(["Distal Femur Flexion Sagittal Plane", 'Midshaft Femur Center P:Sag', 'Femur Center', 'Hip Center'])
       
        try:
            delete_obj(bpy.data.objects["Distal Femur Flexion Sagittal Plane"])
        except:
            pass

        check_list = check_obj_list(['Midshaft Femur Center P:Sag', 'Femur Center', 'Hip Center'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Midshaft Femur Center P:Sag'], 'Midshaft Center P:Sag for DistalFlexionSagittalPlane')
            copy_object(bpy.data.objects['Femur Center'], 'Femur Center for DistalFemurFlexionSagittalPlane 1')
            copy_object(bpy.data.objects['Femur Center'], 'Femur Center for DistalFemurFlexionSagittalPlane 2')
            copy_object(bpy.data.objects['Hip Center'], 'Hip Center for DistalFemurFlexionSagittalPlane')

            make_axis([bpy.data.objects['Femur Center for DistalFemurFlexionSagittalPlane 1'], bpy.data.objects['Midshaft Center P:Sag for DistalFlexionSagittalPlane']], "Distal Femur Flexion Sagittal Plane 1")
            make_axis([bpy.data.objects['Femur Center for DistalFemurFlexionSagittalPlane 2'], bpy.data.objects['Hip Center for DistalFemurFlexionSagittalPlane']], "Distal Femur Flexion Sagittal Plane 2")
            join_obj([bpy.data.objects["Distal Femur Flexion Sagittal Plane 1"], bpy.data.objects["Distal Femur Flexion Sagittal Plane 2"]], "Distal Femur Flexion Sagittal Plane")
            remove_doubles(bpy.data.objects["Distal Femur Flexion Sagittal Plane"])

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
        
        check_create_collection(["Landmarks", "Axes", "Planes", "Projections", "Measurements"])
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
        
            join_obj([bpy.data.objects["ProximalVarusCoronalPlane L1"], bpy.data.objects["ProximalVarusCoronalPlane L2"]], "Proximal Femur Varus Coronal Plane point")
        
            vertex_group(bpy.data.objects["Proximal Femur Varus Coronal Plane point"])
            copy_object(bpy.data.objects["Proximal Femur Varus Coronal Plane point"], "Proximal Femur Varus Coronal Plane point copy")
        
            copy_object(bpy.data.objects['Hip Center'], 'Hip Center ProximalVarusCoronalPlane')
            copy_object(bpy.data.objects['Midshaft Femur Center P:Cor'], 'Midshaft Femur Center P:Cor ProximalVarusCoronal')

            make_axis([bpy.data.objects["Proximal Femur Varus Coronal Plane point"], bpy.data.objects['Hip Center ProximalVarusCoronalPlane']], "ProximalFemurVarusCoronalPlane 1")
            make_axis([bpy.data.objects["Proximal Femur Varus Coronal Plane point copy"], bpy.data.objects['Midshaft Femur Center P:Cor ProximalVarusCoronal']], "ProximalFemurVarusCoronalPlane 2")
            join_obj([bpy.data.objects["ProximalFemurVarusCoronalPlane 1"], bpy.data.objects["ProximalFemurVarusCoronalPlane 2"]], "Proximal Femur Varus Coronal Plane")
            remove_doubles(bpy.data.objects["Proximal Femur Varus Coronal Plane"])
                        
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
        
        check_create_collection(["Landmarks", "Axes", "Planes", "Projections", "Measurements"])
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
        
            join_obj([bpy.data.objects["Proximal Femur Flexion Sagittal Plane L1"], bpy.data.objects["Proximal Femur Flexion Sagittal Plane L2"]], "Proximal Femur Flexion Sagittal Plane point")
        
            vertex_group(bpy.data.objects['Proximal Femur Flexion Sagittal Plane point'])
            copy_object(bpy.data.objects['Proximal Femur Flexion Sagittal Plane point'], 'Proximal Femur Flexion Sagittal Plane point copy')
        
            copy_object(bpy.data.objects['Hip Center'], 'Hip Center for ProximalFemurFlexionSagittalPlane')
            copy_object(bpy.data.objects['GT P:Sag'], 'GT P:Sag for ProximalFemurFlexionSagittalPlane')

            make_axis([bpy.data.objects['Proximal Femur Flexion Sagittal Plane point'], bpy.data.objects['Hip Center for ProximalFemurFlexionSagittalPlane']], "ProximalFemurFlexionSagittalPlane 1")
            make_axis([bpy.data.objects['Proximal Femur Flexion Sagittal Plane point copy'], bpy.data.objects['GT P:Sag for ProximalFemurFlexionSagittalPlane']], "ProximalFemurFlexionSagittalPlane 2")
            join_obj([bpy.data.objects["ProximalFemurFlexionSagittalPlane 1"], bpy.data.objects["ProximalFemurFlexionSagittalPlane 2"]], "Proximal Femur Flexion Sagittal Plane")
            remove_doubles(bpy.data.objects["Proximal Femur Flexion Sagittal Plane"])

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
        
        check_create_collection(["Landmarks", "Axes", "Planes", "Projections", "Measurements"])
        unhide_list(["Condylar difference in coronal plane", 'Lateral Distal P:Cor', "Sagittal Plane", 'Medial Distal P:Cor', 'Distal Plane'])
        
        try:
            delete_obj(bpy.data.objects["Condylar difference in coronal plane"])
        except:
            pass
        
        check_list = check_obj_list(['Lateral Distal P:Cor', "Sagittal Plane", 'Medial Distal P:Cor', 'Distal Plane'])
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
        
        check_create_collection(["Landmarks", "Axes", "Planes", "Projections", "Measurements"])
        unhide_list(["Posterior Condylar difference in transverse plane", 'Posterior Medial Point P:Dis', 'Posterior Lateral Point P:Dis', "Sagittal Plane",'Coronal Plane'])
        
        try:
            delete_obj(bpy.data.objects["Posterior Condylar difference in transverse plane"])
        except:
            pass

        check_list = check_obj_list(['Posterior Medial Point P:Dis', 'Posterior Lateral Point P:Dis', "Sagittal Plane", 'Coronal Plane'])
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
      
        check_create_collection(["Landmarks", "Axes", "Planes", "Projections", "Measurements"])
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

            join_obj([bpy.data.objects["RotationalAngle L1"], bpy.data.objects["RotationalAngle L2"]], "Rotational Angle point")
        
            vertex_group(bpy.data.objects["Rotational Angle point"])
            copy_object(bpy.data.objects["Rotational Angle point"], "Rotational Angle point copy")
        
            copy_object(bpy.data.objects['Posterior Medial Point P:Dis'], 'Posterior Medial Point P:Dis for RotationalAngle')
            copy_object(bpy.data.objects['Medial Epicondyle P:Dis'], 'Medial Epicondyle P:Dis for RotationalAngle')

            make_axis([bpy.data.objects["Rotational Angle point"], bpy.data.objects['Posterior Medial Point P:Dis for RotationalAngle']], "RotationalAngle 1")
            make_axis([bpy.data.objects["Rotational Angle point copy"], bpy.data.objects['Medial Epicondyle P:Dis for RotationalAngle']], "RotationalAngle 2")
            join_obj([bpy.data.objects["RotationalAngle 1"], bpy.data.objects["RotationalAngle 2"]], "Rotational Angle")
            remove_doubles(bpy.data.objects["Rotational Angle"])

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
        
        check_create_collection(["Landmarks", "Axes", "Planes", "Projections", "Measurements"])
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
        
            join_obj([bpy.data.objects["FemurTorsionalAngle L1"], bpy.data.objects["FemurTorsionalAngle L2"]], 'Femur torsional angle point') 
       
            vertex_group(bpy.data.objects['Femur torsional angle point'])
            copy_object(bpy.data.objects['Femur torsional angle point'], 'Femur torsional angle point copy')
        
            copy_object(bpy.data.objects['Hip Center P:Dis'], 'Hip Center P:Dis for FemurTorsionalAngle')
            copy_object(bpy.data.objects['Posterior Medial Point P:Dis'], 'Posterior Medial Point P:Dis for FemurTorsionalAngle')
            make_axis([bpy.data.objects['Femur torsional angle point'], bpy.data.objects['Hip Center P:Dis for FemurTorsionalAngle']], "FemurTorsionalAngle 1")
            make_axis([bpy.data.objects['Femur torsional angle point copy'], bpy.data.objects['Posterior Medial Point P:Dis for FemurTorsionalAngle']], "FemurTorsionalAngle 2")
            join_obj([bpy.data.objects["FemurTorsionalAngle 1"], bpy.data.objects["FemurTorsionalAngle 2"]], "Femur torsional angle")
            remove_doubles(bpy.data.objects['Femur torsional angle'])

            move_to_collection("Measurements", bpy.data.objects['Femur torsional angle']) 
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}