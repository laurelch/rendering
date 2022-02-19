"""
Animate a sequence of objects by hiding and displaying them in order.
"""
import bpy

max_frame=100

for i in range(1,max_frame+1):
    mesh_name='mesh_%04d'%i
    obj=bpy.context.scene.objects[mesh_name]
    obj.hide_render=True
    obj.keyframe_insert("hide_render",frame=i-1)
    obj.hide_viewport=True
    obj.keyframe_insert("hide_viewport",frame=i-1)
    obj.hide_render=False
    obj.keyframe_insert("hide_render",frame=i)
    obj.hide_viewport=False
    obj.keyframe_insert("hide_viewport",frame=i)
    obj.hide_render=True
    obj.keyframe_insert("hide_render",frame=i+1)
    obj.hide_viewport=True
    obj.keyframe_insert("hide_viewport",frame=i+1)