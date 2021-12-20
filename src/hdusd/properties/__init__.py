#**********************************************************************
# Copyright 2020 Advanced Micro Devices, Inc
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#********************************************************************
import bpy

from ..utils import stage_cache

from ..utils import logging
log = logging.Log('properties')

from pxr import UsdImagingLite, Tf


def _createGatlingRenderSettingsClass():
    renderer = UsdImagingLite.Engine()
    renderer.SetRendererPlugin('HdGatlingRendererPlugin')

    props = {}
    for setting in renderer.GetRendererSettingsList():
        name_str = str(setting.name)
        key_str = str(setting.key)
        type_str = str(setting.type)

        value = renderer.GetRendererSetting(Tf.MakeValidIdentifier(name_str))
        if value is None:
            value = setting.defValue

        if type_str == 'FLAG':
            props[key_str] = bpy.props.BoolProperty(name=name_str, default=value)
        elif type_str == 'INT':
            props[key_str] = bpy.props.IntProperty(name=name_str, default=value)
        elif type_str == 'FLOAT':
            props[key_str] = bpy.props.FloatProperty(name=name_str, default=value)
        elif type_str == 'STRING':
            props[key_str] = bpy.props.StringProperty(name=name_str, default=value)
        else:
            log.warn("Render setting {} of type {} not displayed".format(name_str, type_str))

    return type('GatlingRenderSettings', (bpy.types.PropertyGroup,), {'__annotations__': props})

GatlingRenderSettings = _createGatlingRenderSettingsClass()


class HdUSDProperties(bpy.types.PropertyGroup):
    bl_type = None

    @classmethod
    def register(cls):
        cls.bl_type.hdusd = bpy.props.PointerProperty(
            name="HdUSD properties",
            description="HdUSD properties",
            type=cls,
        )

    @classmethod
    def unregister(cls):
        del cls.bl_type.hdusd


class CachedStageProp(bpy.types.PropertyGroup, stage_cache.CachedStage):
    id: bpy.props.IntProperty(default=stage_cache.ID_NO_STAGE)
    is_owner: bpy.props.BoolProperty(default=False)

    def __del__(self):
        pass


from . import (
    scene,
    object,
    node,
    usd_list,
    material,
    hdrpr_render,
    hdprman_render,
    matlib
)
register, unregister = bpy.utils.register_classes_factory((
    CachedStageProp,

    hdrpr_render.QualitySettings,
    hdrpr_render.InteractiveQualitySettings,
    hdrpr_render.ContourSettings,
    hdrpr_render.DenoiseSettings,
    hdrpr_render.RenderSettings,

    hdprman_render.RenderSettings,

    GatlingRenderSettings,

    usd_list.PrimPropertyItem,
    usd_list.UsdListItem,
    usd_list.UsdList,

    node.NodeProperties,

    scene.FinalRenderSettings,
    scene.ViewportRenderSettings,
    scene.SceneProperties,

    object.ObjectProperties,

    material.MaterialProperties,

    matlib.MatlibProperties,
    matlib.WindowManagerProperties,
))
