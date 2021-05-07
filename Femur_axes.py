import bpy
from bpy.types import Operator
from .myPackage.Femur_functions import copy_object, make_axis, unhide_list,unhide, move_to_collection, delete_obj, check_obj_list

class FEMUR_OT_MechanicalAxis(Operator):
    """ """
    bl_label = "Mechanical Axis"
    bl_idname = "object.mechanicalaxis"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        unhide_list(["Mechanical Axis", 'Hip Center', 'Femur Center'])
        
        try:
            delete_obj(bpy.data.objects["Mechanical Axis"])
        except:
            pass
        
        check_list = check_obj_list(['Hip Center', 'Femur Center'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Hip Center'], "Hip Center for mech axis")
            copy_object(bpy.data.objects['Femur Center'], "Femur Center for mech axis")
            make_axis([bpy.data.objects['Hip Center for mech axis'], bpy.data.objects['Femur Center for mech axis']], "Mechanical Axis")
       
            move_to_collection("Axes", bpy.data.objects["Mechanical Axis"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))

        return {'FINISHED'}


class FEMUR_OT_TransEpicondylarAxis(Operator):
    """ """
    bl_label = "Trans Epicondylar Axis"
    bl_idname = "object.transepicondylaraxis"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):

        unhide_list(["Trans Epicondylar Axis", 'Lateral Epicondyle', 'Medial Epicondyle'])

        try:
            delete_obj(bpy.data.objects["Trans Epicondylar Axis"])
        except:
            pass

        check_list = check_obj_list(['Lateral Epicondyle', 'Medial Epicondyle'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Lateral Epicondyle'], "Lateral Epicondyle for TEA")
            copy_object(bpy.data.objects['Medial Epicondyle'], "Medial Epicondyle for TEA")
            make_axis([bpy.data.objects['Lateral Epicondyle for TEA'], bpy.data.objects['Medial Epicondyle for TEA']], "Trans Epicondylar Axis")

            move_to_collection("Axes", bpy.data.objects["Trans Epicondylar Axis"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class FEMUR_OT_NeckLine(Operator):
    """ """
    bl_label = "Neck Line"
    bl_idname = "object.neckline"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        
        unhide_list(["Neck Line", 'Hip Center', 'Neck Center'])
        
        try:
            delete_obj(bpy.data.objects["Neck Line"])
        except:
            pass

        check_list = check_obj_list(['Hip Center', 'Neck Center'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Hip Center'], "Hip Center for neck line")
            copy_object(bpy.data.objects['Neck Center'], "Neck Center for neck line")
            make_axis([bpy.data.objects['Hip Center for neck line'], bpy.data.objects['Neck Center for neck line']], "Neck Line")

            move_to_collection("Axes", bpy.data.objects["Neck Line"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class FEMUR_OT_DistalJointLine(Operator):
    """ """
    bl_label = "Distal Joint Line"
    bl_idname = "object.distaljointline"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

        unhide_list(["Distal Joint Line", 'Medial Distal Point', 'Lateral Distal Point'])
        
        try:
            delete_obj(bpy.data.objects["Distal Joint Line"])
        except:
            pass
        
        check_list = check_obj_list(['Medial Distal Point', 'Lateral Distal Point'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Medial Distal Point'], "Medial Distal Point for distal joint line")
            copy_object(bpy.data.objects['Lateral Distal Point'], "Neck Center for distal joint line")
            make_axis([bpy.data.objects['Medial Distal Point for distal joint line'], bpy.data.objects['Neck Center for distal joint line']], "Distal Joint Line")

            move_to_collection("Axes", bpy.data.objects["Distal Joint Line"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class FEMUR_OT_PosteriorCondylarAxis(Operator):
    """ """
    bl_label = "Posterir Condylar Axis"
    bl_idname = "object.posterircondylaraxis"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

        unhide_list(["Posterir Condylar Axis", 'Posterior Lateral Point', 'Posterior Medial Point'])
        
        try:
            delete_obj(bpy.data.objects["Posterir Condylar Axis"])
        except:
            pass

        check_list = check_obj_list(['Posterior Lateral Point', 'Posterior Medial Point'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Posterior Lateral Point'], "Posterior Lateral Point for posterior condylar axis")
            copy_object(bpy.data.objects['Posterior Medial Point'], "Posterior Medial Point for posterior condylar axis")
            make_axis([bpy.data.objects['Posterior Lateral Point for posterior condylar axis'], bpy.data.objects['Posterior Medial Point for posterior condylar axis']], "Posterir Condylar Axis")

            move_to_collection("Axes", bpy.data.objects["Posterir Condylar Axis"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class FEMUR_OT_AnatomicalAxis(Operator):
    """ """
    bl_label = "Anatomical Axis"
    bl_idname = "object.anatomicalaxis"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        try:
            unhide_list(["Anatomical Axis", 'Anatomical Point', 'Femur Center'])
        except:
            pass

        try:
            delete_obj(bpy.data.objects["Anatomical Axis"])
        except:
            pass
        
        check_list = check_obj_list(['Anatomical Point', 'Femur Center'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Anatomical Point'], "Anatomical Point for anatomical axis")
            copy_object(bpy.data.objects['Femur Center'], "Femur Center for anatomical axis")
            make_axis([bpy.data.objects['Anatomical Point for anatomical axis'], bpy.data.objects['Femur Center for anatomical axis']], "Anatomical Axis")

            move_to_collection("Axes", bpy.data.objects["Anatomical Axis"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}

