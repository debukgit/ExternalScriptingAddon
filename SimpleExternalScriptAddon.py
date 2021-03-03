# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy
import os


bl_info = {
    "name": "Simple External Script Addon",
    "description": "This is a small addon for scripting in an external editor easily",
    "author": "Debuk",
    "version": (1, 0, 0),
    'license': 'GPL v3',
    "blender": (2, 80, 0),
    "support": "COMMUNITY",
    "category": "Development"    
}

def menu_entry(self, context):
    self.layout.operator("debuk.run_external_default_script")


class OBJECT_OT_run_external_default_script(bpy.types.Operator):
    """"Simple External Script Addon"""
    bl_idname = "debuk.run_external_default_script"
    bl_label = "Run defaultscript"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):

        filename = "defaultscript.py"

        filepath = os.path.join(os.path.dirname(bpy.data.filepath), filename)
        global_namespace = {"__file__": filepath, "__name__": "__main__"}
        with open(filepath, 'rb') as file:
            exec(compile(file.read(), filepath, 'exec'), global_namespace)
        return {'FINISHED'}

 
def register():
    bpy.utils.register_class(OBJECT_OT_run_external_default_script)
    bpy.types.TOPBAR_MT_file_defaults.append(menu_entry)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_run_external_default_script)
    bpy.types.TOPBAR_MT_file_defaults.remove(menu_entry)

    
if __name__ == "__main__":
    register()