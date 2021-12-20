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
from . import HdUSD_Panel

class HDUSD_RENDER_PT_gatling_settings(HdUSD_Panel):
    bl_label = "Gatling Settings"

    @classmethod
    def poll(cls, context, delegate):
        return super().poll(context) and delegate == 'HdGatlingRendererPlugin'

    def draw(self, context, gatling):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        col = layout.column()
        for key in gatling.__annotations__.keys():
            col.prop(gatling, key)


class HDUSD_RENDER_PT_gatling_settings_final(HDUSD_RENDER_PT_gatling_settings):
    bl_parent_id = 'HDUSD_RENDER_PT_render_settings_final'

    @classmethod
    def poll(cls, context):
        return HDUSD_RENDER_PT_gatling_settings.poll(context, context.scene.hdusd.final.delegate)

    def draw(self, context):
        return HDUSD_RENDER_PT_gatling_settings.draw(self, context, context.scene.hdusd.final.gatling)


class HDUSD_RENDER_PT_gatling_settings_viewport(HDUSD_RENDER_PT_gatling_settings):
    bl_parent_id = 'HDUSD_RENDER_PT_render_settings_viewport'

    @classmethod
    def poll(cls, context):
        return HDUSD_RENDER_PT_gatling_settings.poll(context, context.scene.hdusd.viewport.delegate)

    def draw(self, context):
        return HDUSD_RENDER_PT_gatling_settings.draw(self, context, context.scene.hdusd.viewport.gatling)
