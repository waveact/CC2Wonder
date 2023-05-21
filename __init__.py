bl_info = {
    "name": "CC2Wonder",
    "blender": (3, 4, 0),
    "version": (0, 0, 1),
    "category": "Characters",
    "location": "3D View > Properties > CC2Wonder",
    "description": "Converting Reallusion CC characters to be compatible with the Wonder Studio platform.",
}

import bpy

# Register and import submodules
def register():
    from . import panel, action
    panel.register()
    action.register()

def unregister():
    from . import panel, action
    panel.unregister()
    action.unregister()

if __name__ == "__main__":
    register()