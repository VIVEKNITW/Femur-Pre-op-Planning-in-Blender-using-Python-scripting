# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Femur preop-planning",
    "author" : "Vivekanand Shanbhag",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy

from .Femur_collections_panel import FEMUR_PT_Collections
from .Femur_landmark_panel import FEMUR_PT_Landmark_assignment
from .Femur_projections_panel import FEMUR_PT_Projections
from .Femur_angles_panel import FEMUR_PT_Angles
from .Femur_measureIt_panel import FEMUR_PT_MeasureIt, MyProperty
from .Femur_collections import FEMUR_OT_Collections
from .Femur_Landmarks import FEMUR_OT_HipCenter, FEMUR_OT_FemurCenter, FEMUR_OT_MedialDistalPoint, FEMUR_OT_LateralDistalPoint, FEMUR_OT_LateralEpicondyle, FEMUR_OT_MedialEpicondyle, FEMUR_OT_PosteriorMedialPoint, FEMUR_OT_PosteriorLateralPoint, FEMUR_OT_NeckCenter, FEMUR_OT_GreaterTrochanter, FEMUR_OT_MidshaftFemurCenter, FEMUR_OT_AnatomicalPoint
from .Femur_axes import FEMUR_OT_MechanicalAxis, FEMUR_OT_TransEpicondylarAxis, FEMUR_OT_NeckLine, FEMUR_OT_PosteriorCondylarAxis, FEMUR_OT_DistalJointLine, FEMUR_OT_AnatomicalAxis
from .Femur_planes import FEMUR_OT_CoronalPlane, FEMUR_OT_SagittalPlane, FEMUR_OT_DistalPlane, FEMUR_OT_CoronalAtHip, FEMUR_OT_SagittalAtHip, FEMUR_OT_CoronalAtMidshaft, FEMUR_OT_SagittalAtMidshaft
from .Femur_projections import FEMUR_OT_Projections
from .Femur_angles import FEMUR_OT_ValgusAngle, FEMUR_OT_NSACoronal, FEMUR_OT_NSASagittal, FEMUR_OT_mLDFA, FEMUR_OT_mLPFA, FEMUR_OT_aMPFA, FEMUR_OT_aLDFA, FEMUR_OT_MidshaftVarusInCoronalPlane, FEMUR_OT_MidshaftBowInSagittalPlane, FEMUR_OT_DistalFemurValgusCoronalPlane, FEMUR_OT_DistalFemurFlexionSagittalPlane, FEMUR_OT_ProximalFemurVarusCoronalPlane, FEMUR_OT_ProximalFemurFlexionSagittalPlane, FEMUR_OT_CondylarDifferenceCoronalPlane, FEMUR_OT_CondylarDifferenceTransversePlane, FEMUR_OT_RotationalAngle, FEMUR_OT_FemurTorsionalAngle
from .Femur_measureIt import FEMUR_OT_EnableOrDisableMeasureIt
classes = (MyProperty, FEMUR_PT_Collections, FEMUR_PT_Landmark_assignment, FEMUR_PT_Projections, FEMUR_PT_Angles, FEMUR_PT_MeasureIt, FEMUR_OT_HipCenter, FEMUR_OT_FemurCenter, FEMUR_OT_MedialDistalPoint, FEMUR_OT_LateralDistalPoint, FEMUR_OT_LateralEpicondyle, FEMUR_OT_MedialEpicondyle, FEMUR_OT_PosteriorMedialPoint, FEMUR_OT_PosteriorLateralPoint, FEMUR_OT_NeckCenter, FEMUR_OT_GreaterTrochanter, FEMUR_OT_MidshaftFemurCenter, FEMUR_OT_AnatomicalPoint, FEMUR_OT_MechanicalAxis, FEMUR_OT_TransEpicondylarAxis, FEMUR_OT_NeckLine, FEMUR_OT_PosteriorCondylarAxis, FEMUR_OT_DistalJointLine, FEMUR_OT_AnatomicalAxis, FEMUR_OT_CoronalPlane, FEMUR_OT_SagittalPlane, FEMUR_OT_DistalPlane, FEMUR_OT_CoronalAtHip, FEMUR_OT_SagittalAtHip, FEMUR_OT_CoronalAtMidshaft, FEMUR_OT_SagittalAtMidshaft, FEMUR_OT_Projections, FEMUR_OT_ValgusAngle, FEMUR_OT_NSACoronal, FEMUR_OT_NSASagittal, FEMUR_OT_mLDFA, FEMUR_OT_mLPFA, FEMUR_OT_aMPFA, FEMUR_OT_aLDFA, FEMUR_OT_MidshaftVarusInCoronalPlane, FEMUR_OT_MidshaftBowInSagittalPlane, FEMUR_OT_DistalFemurFlexionSagittalPlane, FEMUR_OT_DistalFemurValgusCoronalPlane, FEMUR_OT_ProximalFemurVarusCoronalPlane, FEMUR_OT_ProximalFemurFlexionSagittalPlane, FEMUR_OT_CondylarDifferenceCoronalPlane, FEMUR_OT_CondylarDifferenceTransversePlane, FEMUR_OT_RotationalAngle, FEMUR_OT_FemurTorsionalAngle, FEMUR_OT_Collections, FEMUR_OT_EnableOrDisableMeasureIt)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=MyProperty)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.my_tool

if __name__ == "__main__":
    register()