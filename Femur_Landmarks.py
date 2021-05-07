import bpy 
from bpy.types import Operator
from .myPackage.Femur_functions import unhide, select_activate , move_to_collection, get_collection_pos, coll_list, delete_obj

class FEMUR_OT_HipCenter(Operator):
    """ """
    bl_label = "Hip Center"
    bl_idname = "object.hipcenter"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):    
        try:
            unhide(bpy.data.objects["Hip Center"])
            delete_obj(bpy.data.objects["Hip Center"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "Hip Center"
        
        move_to_collection("Landmarks", bpy.data.objects["Hip Center"])
        return {'FINISHED'}


class FEMUR_OT_FemurCenter(Operator):
    """ """
    bl_label = "Femur Center"
    bl_idname = "object.femurcenter"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        try:
            unhide(bpy.data.objects["Femur Center"])
            delete_obj(bpy.data.objects["Femur Center"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "Femur Center"

        move_to_collection("Landmarks", bpy.data.objects["Femur Center"])
        return {'FINISHED'}


class FEMUR_OT_MedialDistalPoint(Operator):
    """ """
    bl_label = "Medial Distal Point"
    bl_idname = "object.medialdistalpoint"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        try:
            unhide(bpy.data.objects["Medial Distal Point"])
            delete_obj(bpy.data.objects["Medial Distal Point"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "Medial Distal Point"

        move_to_collection("Landmarks", bpy.data.objects["Medial Distal Point"])
        return {'FINISHED'}


class FEMUR_OT_LateralDistalPoint(Operator):
    """ """
    bl_label = "Lateral Distal Point"
    bl_idname = "object.lateraldistalpoint"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        try:
            unhide(bpy.data.objects["Lateral Distal Point"])
            delete_obj(bpy.data.objects["Lateral Distal Point"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "Lateral Distal Point"

        move_to_collection("Landmarks", bpy.data.objects["Lateral Distal Point"])
        return {'FINISHED'}


class FEMUR_OT_LateralEpicondyle(Operator):
    """ """
    bl_label = "Lateral Epicondyle"
    bl_idname = "object.lateralepicondyle"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        try:
            unhide(bpy.data.objects["Lateral Epicondyle"])
            delete_obj(bpy.data.objects["Lateral Epicondyle"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "Lateral Epicondyle"

        move_to_collection("Landmarks", bpy.data.objects["Lateral Epicondyle"])
        return {'FINISHED'}


class FEMUR_OT_MedialEpicondyle(Operator):
    """ """
    bl_label = "Medial Epicondyle"
    bl_idname = "object.medialepicondyle"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        try:
            unhide(bpy.data.objects["Medial Epicondyle"])
            delete_obj(bpy.data.objects["Medial Epicondyle"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "Medial Epicondyle"

        move_to_collection("Landmarks", bpy.data.objects["Medial Epicondyle"])
        return {'FINISHED'}

    
class FEMUR_OT_PosteriorMedialPoint(Operator):
    """ """
    bl_label = "Posterior Medial Point"
    bl_idname = "object.posteriormedialpoint"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        try:
            unhide(bpy.data.objects["Posterior Medial Point"])
            delete_obj(bpy.data.objects["Posterior Medial Point"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "Posterior Medial Point"

        move_to_collection("Landmarks", bpy.data.objects["Posterior Medial Point"])
        return {'FINISHED'}

    
class FEMUR_OT_PosteriorLateralPoint(Operator):
    """ """
    bl_label = "Posterior Lateral Point"
    bl_idname = "object.posteriorlateralpoint"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        try:
            unhide(bpy.data.objects["Posterior Lateral Point"])
            delete_obj(bpy.data.objects["Posterior Lateral Point"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "Posterior Lateral Point"

        move_to_collection("Landmarks", bpy.data.objects["Posterior Lateral Point"])
        return {'FINISHED'}


class FEMUR_OT_NeckCenter(Operator):
    """ """
    bl_label = "Neck Center"
    bl_idname = "object.neckcenter"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        try:
            unhide(bpy.data.objects["Neck Center"])
            delete_obj(bpy.data.objects["Neck Center"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "Neck Center"

        move_to_collection("Landmarks", bpy.data.objects["Neck Center"])
        return {'FINISHED'}


class FEMUR_OT_GreaterTrochanter(Operator):
    """ """
    
    bl_label = "Greater Trochanter"
    bl_idname = "object.greatertrochaner"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        try:
            unhide(bpy.data.objects["Greater Trochanter"])
            delete_obj(bpy.data.objects["Greater Trochanter"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "Greater Trochanter"

        move_to_collection("Landmarks", bpy.data.objects["Greater Trochanter"])
        return {'FINISHED'}


class FEMUR_OT_MidshaftFemurCenter(Operator):
    """ """
    bl_label = "Midshaft Femur Center"
    bl_idname = "object.midshaftfemurcenter"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        try:
            unhide(bpy.data.objects["Midshaft Femur Center"])
            delete_obj(bpy.data.objects["Midshaft Femur Center"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "Midshaft Femur Center"
        
        move_to_collection("Landmarks", bpy.data.objects["Midshaft Femur Center"])
        return {'FINISHED'}


class FEMUR_OT_AnatomicalPoint(Operator):
    """ """
    bl_label = "Anatomical Point"
    bl_idname = "object.anatomicalpoint"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        try:
            unhide(bpy.data.objects["Anatomical Point"])
            delete_obj(bpy.data.objects["Anatomical Point"])
        except:
            pass
        
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "Anatomical Point"

        move_to_collection("Landmarks", bpy.data.objects["Anatomical Point"])
        return {'FINISHED'}