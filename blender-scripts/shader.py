"""
Create a shader (Principled BSDF) and apply to a sequence of objects
Reference: vividfax.github.io/2021/01/14/blender-materials.html
"""
import bpy

max_frame=100

def newMaterial(id):
    mat=bpy.data.materials.get(id)
    if mat is None:
        mat=bpy.data.materials.new(name=id)
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

# Shader
mat=newShader("shader_test",1,1,1,specular=0.1,roughness=0.3,transmission=1)

for i in range(1,max_frame+1):
    mesh_name='mesh_%04d'%i
    obj=bpy.context.scene.objects[mesh_name]
    obj.data.materials.clear()
    obj.data.materials.append(mat)
