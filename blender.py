import bpy 
from pathlib import Path
from math import * 
import time

object1 = bpy.data.objects["Curve"]
object1.location = (0, 0, 0 )
object1.rotation_euler = (radians(90),radians(90),radians(0)) 

object2 = bpy.data.objects["Curve.002"]
object2.location = (0, 0, 0 )
object2.rotation_euler = (radians(0),radians(90),radians(0)) 

selected_objects = bpy.context.selected_objects
for obj in selected_objects:
    obj.select_set(False)
bpy.context.view_layer.objects.active = object1
selection = object1.select_get()
object1.select_set(True)
bpy.ops.object.convert(target="MESH")
for obj in selected_objects:
    obj.select_set(False)
bpy.context.view_layer.objects.active = object2
selection = object2.select_get()
object2.select_set(True)
bpy.ops.object.convert(target="MESH")
bool_mod1 = object1.modifiers.new(name='Boolean1', type='BOOLEAN')
bool_mod1.operation = 'INTERSECT'
bool_mod1.object = object2
bpy.ops.bool_mod1.solver = 'CARVE'  # or 'FAST' or 'EXACT'
bpy.context.view_layer.objects.active = object2
object2.select_set(True)
object1.select_set(True)
bpy.ops.object.modifier_apply({"object": object1},modifier=bool_mod1.name)

object3 = bpy.data.objects["Curve.006"]
selected_objects = bpy.context.selected_objects
for obj in selected_objects:
    obj.select_set(False)
bpy.context.view_layer.objects.active = object3
selection = object3.select_get()
object3.select_set(True)
bpy.ops.object.convert(target="MESH")
bool_mod1 = object3.modifiers.new(name='Boolean1', type='BOOLEAN')
bool_mod1.operation = 'INTERSECT'
bool_mod1.object = object1
bpy.ops.bool_mod1.solver = 'CARVE'  # or 'FAST' or 'EXACT'
bpy.context.view_layer.objects.active = object1
object3.select_set(True)
object1.select_set(True)
bpy.ops.object.modifier_apply({"object": object3},modifier=bool_mod1.name)
bpy.context.view_layer.objects.active = object3
object1.select_set(True)
object2.select_set(True)
object3.select_set(False)
bpy.context.view_layer.objects.active = object2
bpy.ops.object.delete()
object4 = bpy.data.objects["Curve.001"]
object4.select_set(True)
bpy.ops.export_mesh.stl(filepath="/Users/NBSchwa/Desktop/final.stl")
