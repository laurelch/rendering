# Python for Blender Cheatsheet

Table of Contents
- [Python for Blender Cheatsheet](#python-for-blender-cheatsheet)
  - [Import](#import)
    - [Import Blender Python API](#import-blender-python-api)
    - [Import OBJ Files](#import-obj-files)
  - [Select](#select)
  - [Shader](#shader)
    - [Create a Principled BSDF Shader](#create-a-principled-bsdf-shader)
    - [Create a Mix](#create-a-mix)
    - [Create a Link Between Nodes (`node_a`, `node_b`)](#create-a-link-between-nodes-node_a-node_b)
    - [Clear Existing Materials of Object `obj` and Add a New Material `mat`](#clear-existing-materials-of-object-obj-and-add-a-new-material-mat)
  - [Animation](#animation)
    - [Insert Keyframe](#insert-keyframe)
    - [Hide/Show in Viewport](#hideshow-in-viewport)
    - [Hide/Show when Render](#hideshow-when-render)

## Import
### Import Blender Python API
```python
import bpy
```
### Import OBJ Files
```python
path_to_file=path_to_obj_dir+"/"+item
bpy.ops.import_scene.obj(filepath=path_to_file)
# print file name
obj_name=os.path.splitext(item)[0]
print(obj_name)
```
[Back to Top](#python-for-blender-cheatsheet)
## Select
```python
mesh_name="object-to-select"
obj=bpy.context.scene.objects[mesh_name]
```
[Back to Top](#python-for-blender-cheatsheet)
## Shader
More details: [Principled BSDF - Blender Manual](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/principled.html)
### Create a Principled BSDF Shader
```python
def newMaterial(id):
    mat=bpy.data.materials.get(id)
    if mat is None:
        mat=bpy.data.material(name=id)
    mat.use_nodes=True
    if mat.node_tree:
        mat.node_tree.links.clear()
        mat.node_tree.nodes.clear()
    return mat

def newShader(id,r,g,b,specular=0,roughness=0,transmission=0):
    mat=newMaterial(id)
    nodes=mat.node_tree.nodes
    links=mat.node_tree.links
    output=nodes.new(type='ShaderNodeOutputMaterial')
    shader=nodes.new(type='ShaderNodeBsdfPrincipled')
    nodes["Principled BSDF"].inputs[0].default_value=(r,g,b,1)
    nodes["Principled BSDF"].inputs[7].default_value=specular
    nodes["Principled BSDF"].inputs[9].default_value=roughness
    nodes["Principled BSDF"].inputs[17].default_value=transmission
    links.new(shader.outputs[0],output.inputs[0])
    return mat
```
### Create a Mix
```python
Mix=mat.node_tree.nodes.new("ShaderNodeMixRGB")
```
### Create a Link Between Nodes (`node_a`, `node_b`)
```python
mat.node_tree.links.new(node_a.outputs[0],node_b.inputs[0])
```
### Clear Existing Materials of Object `obj` and Add a New Material `mat`
```python
obj.data.materials.clear()
obj.data.materials.append(mat)
```
[Back to Top](#python-for-blender-cheatsheet)
## Animation
### Insert Keyframe
More details: [Keyframe(bpy_struct) - Blender Python API](https://docs.blender.org/api/current/bpy.types.Keyframe.html)
```python
current_frame=1
obj.keyframe_insert(data_path="location",frame=current_frame)
```
### Hide/Show in Viewport
Being displayed in Blender viewport
```python
obj.hide_viewport=True
obj.hide_viewport=False
```
### Hide/Show when Render
Being rendered when render
```python
obj.hide_render=True
obj.hide_render=False
```
[Back to Top](#python-for-blender-cheatsheet)