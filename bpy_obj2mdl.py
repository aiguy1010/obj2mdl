import bpy
import sys

# Get arguments
argv = sys.argv[sys.argv.index('--')+1:] # Disregard all args before "--"
FILENAME = argv[0]
PATH = argv[1]

FULL_PATH = PATH+'/'+FILENAME

# Select all
for object in bpy.data.objects:
    object.select = True

# Delete all
bpy.ops.object.delete()

# Import .obj
bpy.ops.import_scene.obj(filepath=FULL_PATH)

slashIndex = FILENAME.rfind('/')
if slashIndex == -1:
    OBJ_NAME = FILENAME[: -4]
else:
    OBJ_NAME = FILENAME[slashIndex+1: -4]

bpy.data.objects[0].name = OBJ_NAME

# Export .mdl
bpy.data.scenes["Scene"].urho_exportsettings.outputPath = PATH+'/../bin/Data'
bpy.data.scenes["Scene"].urho_exportsettings.fileOverwrite = True
bpy.ops.urho.export()
