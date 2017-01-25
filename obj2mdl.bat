for %%f in (objs/*.obj) do (
   blender --background --python bpy_obj2mdl.py -- objs/"%%~f" "%cd%"
)
