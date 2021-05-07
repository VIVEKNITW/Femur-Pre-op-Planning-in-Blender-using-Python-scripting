import bpy
from bpy.types import Operator
from .myPackage.Femur_functions import save_orientation_InEditMode, deselect, select_activate, cursor_to_obj, add_plane, copy_object, delete_obj, save_orientation_obj, unhide_list, move_to_collection, check_obj_list

class FEMUR_OT_CoronalPlane(Operator):
    """ """
    bl_label = "Coronal Plane"
    bl_idname = "object.coronalplane"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        
        unhide_list(["Coronal Plane", 'Mechanical Axis', 'Trans Epicondylar Axis', 'Femur Center'])
        
        try:
            delete_obj(bpy.data.objects["Coronal Plane"])
        except:
            pass
        
        check_list = check_obj_list(['Mechanical Axis', 'Trans Epicondylar Axis', 'Femur Center'])
        if len(check_list) == 0:
            save_orientation_InEditMode(bpy.data.objects['Mechanical Axis'], "EDGE")
            copy_object(bpy.data.objects['Trans Epicondylar Axis'], 'Trans Epicondylar Axis for coronal plane')
        
            deselect()
            select_activate(bpy.data.objects['Trans Epicondylar Axis for coronal plane'])
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_mode(type="EDGE")
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, -120, 0), "constraint_axis":(False, True, False)})
            bpy.ops.mesh.select_mode(type="FACE")
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.transform.create_orientation(use=True)
            bpy.ops.object.editmode_toggle()

            cursor_to_obj(bpy.data.objects['Femur Center'])
        
            add_plane("Coronal Plane")
            delete_obj(bpy.data.objects['Trans Epicondylar Axis for coronal plane'])

            move_to_collection("Planes", bpy.data.objects["Coronal Plane"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class FEMUR_OT_SagittalPlane(Operator):
    """ """
    bl_label = "Sagittal Plane"
    bl_idname = "object.sagittalplane"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):

        unhide_list(["Sagittal Plane", 'Coronal Plane', 'Femur Center'])
        
        try:
            delete_obj(bpy.data.objects["Sagittal Plane"])
        except:
            pass
        
        check_list = check_obj_list(['Coronal Plane', 'Femur Center'])
        if len(check_list) == 0:
            save_orientation_obj(bpy.data.objects['Coronal Plane'])
            cursor_to_obj(bpy.data.objects['Femur Center'])
            add_plane("Sagittal Plane")
            bpy.ops.transform.transform(mode='ALIGN')
            bpy.ops.transform.rotate(value=1.5708, orient_axis='Y',  constraint_axis=(False, True, False))

            move_to_collection("Planes", bpy.data.objects["Sagittal Plane"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class FEMUR_OT_DistalPlane(Operator):
    """ """
    bl_label = "Distal Plane"
    bl_idname = "object.distalplane"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):

        unhide_list(["Distal Plane", 'Coronal Plane', 'Femur Center'])

        try:
            delete_obj(bpy.data.objects["Distal Plane"])
        except:
            pass
        
        check_list = check_obj_list(['Coronal Plane', 'Femur Center'])
        if len(check_list) == 0:
            save_orientation_obj(bpy.data.objects['Coronal Plane'])
            cursor_to_obj(bpy.data.objects['Femur Center'])
            add_plane("Distal Plane")
            bpy.ops.transform.transform(mode='ALIGN')
            bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='Coronal Plane', orient_matrix_type='Coronal Plane', constraint_axis=(False, True, False))

            move_to_collection("Planes", bpy.data.objects["Distal Plane"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class FEMUR_OT_CoronalAtHip(Operator):
    """ """
    bl_label = "Coronal Plane at Hip"
    bl_idname = "object.coronalathip"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):

        unhide_list(["Coronal Plane at Hip", 'Coronal Plane', 'Hip Center'])
        
        try:
            delete_obj(bpy.data.objects["Coronal Plane at Hip"])
        except:
            pass

        check_list = check_obj_list(['Coronal Plane', 'Hip Center'])
        if len(check_list) == 0:
            save_orientation_obj(bpy.data.objects['Coronal Plane'])
            cursor_to_obj(bpy.data.objects['Hip Center'])
            add_plane("Coronal Plane at Hip")
            bpy.ops.transform.transform(mode = 'ALIGN')

            move_to_collection("Planes", bpy.data.objects["Coronal Plane at Hip"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class FEMUR_OT_SagittalAtHip(Operator):
    """ """
    bl_label = "Sagittal Plane at Hip"
    bl_idname = "object.sagittalathip"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
    
        unhide_list(["Sagittal Plane at Hip", 'Sagittal Plane', 'Hip Center'])
       
        try:
            bpy.data.objects["Sagittal Plane at Hip"]
        except:
            pass
        
        check_list = check_obj_list(['Sagittal Plane', 'Hip Center'])
        if len(check_list) == 0:
            save_orientation_obj(bpy.data.objects['Sagittal Plane'])
            cursor_to_obj(bpy.data.objects['Hip Center'])
            add_plane("Sagittal Plane at Hip")
            bpy.ops.transform.transform(mode = 'ALIGN')

            move_to_collection("Planes", bpy.data.objects["Sagittal Plane at Hip"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class FEMUR_OT_CoronalAtMidshaft(Operator):
    """ """
    bl_label = "Coronal Plane at Midshaft"
    bl_idname = "object.coronalatmidshaft"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):

        unhide_list(["Coronal Plane at Midshaft", 'Coronal Plane', 'Mechanical Axis'])
        
        try:
            bpy.data.objects["Coronal Plane at Midshaft"]
        except:
            pass
        
        check_list = check_obj_list(['Coronal Plane', 'Mechanical Axis'])
        if len(check_list) == 0:
            save_orientation_obj(bpy.data.objects['Coronal Plane'])
            cursor_to_obj(bpy.data.objects['Mechanical Axis'])
            add_plane("Coronal Plane at Midshaft")
            bpy.ops.transform.transform(mode = 'ALIGN')

            move_to_collection("Planes", bpy.data.objects["Coronal Plane at Midshaft"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))

        return {'FINISHED'}


class FEMUR_OT_SagittalAtMidshaft(Operator):
    """ """
    bl_label = "Sagittal Plane at Midshaft"
    bl_idname = "object.sagittalatmidshaft"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
    
        unhide_list(["Sagittal Plane at Midshaft", 'Sagittal Plane', 'Mechanical Axis'])
        
        try:
            bpy.data.objects["Sagittal Plane at Midshaft"]
        except:
            pass
        
        check_list = check_obj_list(['Sagittal Plane', 'Mechanical Axis'])
        if len(check_list) == 0:
            save_orientation_obj(bpy.data.objects['Sagittal Plane'])
            cursor_to_obj(bpy.data.objects['Mechanical Axis'])
            add_plane("Sagittal Plane at Midshaft")
            bpy.ops.transform.transform(mode = 'ALIGN')

            move_to_collection("Planes", bpy.data.objects["Sagittal Plane at Midshaft"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
       
        return {'FINISHED'}