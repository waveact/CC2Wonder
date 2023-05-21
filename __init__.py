bl_info = {
    "name": "CC2Wonder",
    "blender": (3, 4, 0),
    "category": "Characters",
    "location": "Menu > Object > CC2Wonder",
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