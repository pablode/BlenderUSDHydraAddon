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

# logging
logging_level = 'INFO'     # available levels: 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL'
logging_backups = 5

# other settings
matlib_enabled = True
engine_use_preview = True
usd_mesh_assign_material_enabled = False

# dev settings
show_dev_settings = False


try:
    # Trying to load configdev.py if it exist
    # example for logging setup:
    #   from . import config
    #   config.<parameter> = <value>

    from . import configdev

except ImportError:
    pass
