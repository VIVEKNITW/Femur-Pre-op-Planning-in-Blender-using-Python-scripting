import bpy
from bpy.types import Operator
from .myPackage.Femur_functions import copy_object, shrinkwrap_obj, unhide_list, move_to_collection, delete_obj

class FEMUR_OT_Projections(Operator):
    """ """
    bl_label = "Projections"
    bl_idname = "object.projections"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        unhide_list(['Hip Center', 'Posterior Lateral Point', 'Posterior Medial Point', 'Lateral Epicondyle', 'Medial Epicondyle', "Sagittal Plane at Midshaft", "Coronal Plane at Midshaft", 'Midshaft Femur Center', 'Lateral Distal Point', "Coronal Plane", 'Medial Distal Point','Anatomical Point', "Sagittal Plane at Hip", "Greater Trochanter", 'Neck Center', "Coronal Plane at Hip", "Sagittal Plane", "Distal Plane"])
        unhide_list(["Hip Center P:Dis", "Posterior Lateral Point P:Dis", "Posterior Medial Point P:Dis", "Lateral Epicondyle P:Dis", "Medial Epicondyle P:Dis", "Midshaft Femur Center P:Sag", "Midshaft Femur Center P:Cor", "Lateral Distal P:Cor", "Medial Distal P:Cor", "Anatomical Point P:Cor", "Neck Center P:Cor", "Neck Center P:Sag", "Neck Center P:Dis", "GT P:Cor", "GT P:Sag"])
        try:
            delete_obj(bpy.data.objects["Neck Center P:Cor"])
        except:
            pass

        try:
            copy_object(bpy.data.objects['Neck Center'], "Neck Center P:Cor")
            shrinkwrap_obj(bpy.data.objects["Neck Center P:Cor"], bpy.data.objects["Coronal Plane at Hip"])
            move_to_collection("Projections", bpy.data.objects["Neck Center P:Cor"])        
        except:
            pass
        

        try:
            delete_obj(bpy.data.objects["Neck Center P:Sag"])
        except:
            pass

        try:
            copy_object(bpy.data.objects['Neck Center'], "Neck Center P:Sag")
            shrinkwrap_obj(bpy.data.objects["Neck Center P:Sag"], bpy.data.objects["Sagittal Plane at Hip"])
            move_to_collection("Projections", bpy.data.objects["Neck Center P:Sag"])     
        except:
            pass
        

        try:
            delete_obj(bpy.data.objects["Neck Center P:Dis"])
        except:
            pass

        try:
            copy_object(bpy.data.objects['Neck Center'],  "Neck Center P:Dis")
            shrinkwrap_obj(bpy.data.objects["Neck Center P:Dis"], bpy.data.objects["Distal Plane"])
            move_to_collection("Projections", bpy.data.objects["Neck Center P:Dis"])   
        except:
            pass


        try:
            delete_obj(bpy.data.objects["GT P:Cor"])
        except:
            pass

        try:
            copy_object(bpy.data.objects["Greater Trochanter"], "GT P:Cor")
            shrinkwrap_obj(bpy.data.objects["GT P:Cor"], bpy.data.objects["Coronal Plane at Hip"])
            move_to_collection("Projections", bpy.data.objects["GT P:Cor"])  
        except:
            pass
        
        
        try:
            delete_obj(bpy.data.objects["GT P:Sag"])
        except:
            pass

        try:
            copy_object(bpy.data.objects["Greater Trochanter"], "GT P:Sag")
            shrinkwrap_obj(bpy.data.objects["GT P:Sag"], bpy.data.objects["Sagittal Plane at Hip"])
            move_to_collection("Projections", bpy.data.objects["GT P:Sag"])  
        except:
            pass

        
        try:
            delete_obj(bpy.data.objects["Anatomical Point P:Cor"])
        except:
            pass

        try:
            copy_object(bpy.data.objects['Anatomical Point'], "Anatomical Point P:Cor")
            shrinkwrap_obj(bpy.data.objects["Anatomical Point P:Cor"], bpy.data.objects["Coronal Plane at Hip"])
            move_to_collection("Projections", bpy.data.objects["Anatomical Point P:Cor"])  
        except:
            pass
        
        
        try:
            delete_obj(bpy.data.objects["Medial Distal P:Cor"])
        except:
            pass

        try:
            copy_object(bpy.data.objects['Medial Distal Point'], "Medial Distal P:Cor")
            shrinkwrap_obj(bpy.data.objects["Medial Distal P:Cor"], bpy.data.objects["Coronal Plane"])
            move_to_collection("Projections", bpy.data.objects["Medial Distal P:Cor"])  
        except:
            pass

        
        try:
            delete_obj(bpy.data.objects["Lateral Distal P:Cor"])
        except:
            pass

        try:
            copy_object(bpy.data.objects['Lateral Distal Point'], "Lateral Distal P:Cor")
            shrinkwrap_obj(bpy.data.objects["Lateral Distal P:Cor"], bpy.data.objects["Coronal Plane"])
            move_to_collection("Projections", bpy.data.objects["Lateral Distal P:Cor"])  
        except:
            pass

        
        try:
            delete_obj(bpy.data.objects["Midshaft Femur Center P:Cor"])
        except:
            pass

        try:
            copy_object(bpy.data.objects['Midshaft Femur Center'], "Midshaft Femur Center P:Cor")
            shrinkwrap_obj(bpy.data.objects["Midshaft Femur Center P:Cor"], bpy.data.objects["Coronal Plane at Midshaft"])
            move_to_collection("Projections", bpy.data.objects["Midshaft Femur Center P:Cor"])         
        except:
            pass
        
        
        try:
            delete_obj(bpy.data.objects["Midshaft Femur Center P:Sag"])
        except:
            pass

        try:
            copy_object(bpy.data.objects['Midshaft Femur Center'], "Midshaft Femur Center P:Sag")
            shrinkwrap_obj(bpy.data.objects["Midshaft Femur Center P:Sag"], bpy.data.objects["Sagittal Plane at Midshaft"])
            move_to_collection("Projections", bpy.data.objects["Midshaft Femur Center P:Sag"])  
        except:
            pass
        
        
        try:
            delete_obj(bpy.data.objects["Medial Epicondyle P:Dis"])
        except:
            pass

        try:
            copy_object(bpy.data.objects['Medial Epicondyle'], "Medial Epicondyle P:Dis")
            shrinkwrap_obj(bpy.data.objects["Medial Epicondyle P:Dis"], bpy.data.objects["Distal Plane"])
            move_to_collection("Projections", bpy.data.objects["Medial Epicondyle P:Dis"])          
        except:
            pass
        
        
        try:
            delete_obj(bpy.data.objects["Lateral Epicondyle P:Dis"])
        except:
            pass
        
        try:
            copy_object(bpy.data.objects['Lateral Epicondyle'], "Lateral Epicondyle P:Dis")
            shrinkwrap_obj(bpy.data.objects["Lateral Epicondyle P:Dis"], bpy.data.objects["Distal Plane"])
            move_to_collection("Projections", bpy.data.objects["Lateral Epicondyle P:Dis"])  
        except:
            pass
        
        
        try:
            delete_obj(bpy.data.objects["Posterior Medial Point P:Dis"])
        except:
            pass

        try:
            copy_object(bpy.data.objects['Posterior Medial Point'], "Posterior Medial Point P:Dis")
            shrinkwrap_obj(bpy.data.objects["Posterior Medial Point P:Dis"], bpy.data.objects["Distal Plane"])
            move_to_collection("Projections", bpy.data.objects["Posterior Medial Point P:Dis"])  
        except:
            pass
        
        
        try:
            delete_obj(bpy.data.objects["Posterior Lateral Point P:Dis"])
        except:
            pass

        try:
            copy_object(bpy.data.objects['Posterior Lateral Point'], "Posterior Lateral Point P:Dis")
            shrinkwrap_obj(bpy.data.objects["Posterior Lateral Point P:Dis"], bpy.data.objects["Distal Plane"])
            move_to_collection("Projections", bpy.data.objects["Posterior Lateral Point P:Dis"])  
        except:
            pass
        
        
        try:
            delete_obj(bpy.data.objects["Hip Center P:Dis"])
        except:
            pass

        try:
            copy_object(bpy.data.objects['Hip Center'], "Hip Center P:Dis")
            shrinkwrap_obj(bpy.data.objects["Hip Center P:Dis"], bpy.data.objects["Distal Plane"])
            move_to_collection("Projections", bpy.data.objects["Hip Center P:Dis"])  
        except:
            pass
                
        return {'FINISHED'}