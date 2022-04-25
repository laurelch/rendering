"""
* Used as Python for Blender

1. crowd in Blender file has been created as cylinders, named "cylinder0001", etc
2. read CSV files to load translations in 2D and key animations
3. apply color with "Principled BSDF" and "Mix" shaders
"""

import bpy
updatePosition=False # reload positions info
displayGroup=True # display group info
totalGroups=2 # number of groups
createMaterial=False # recreate material
# input data directory
project_directory="/path/to/project/"
directory=project_directory+"path/to/data/"

def main():
    start=1
    end=10
    step=1
    readData(start,end,step)

def newMaterial(id):
    mat=bpy.data.materials.get(id)
    if mat is None:
        mat=bpy.data.materials.new(name=id)
    mat.use_nodes=True
    if mat.node_tree:
        mat.node_tree.links.clear()
        mat.node_tree.nodes.clear()
    return mat

def newShader(id,r=0,g=0,b=0):
    mat=newMaterial(id)
    nodes=mat.node_tree.nodes
    links=mat.node_tree.links
    # main shader
    output=nodes.new(type='ShaderNodeOutputMaterial')
    shader=nodes.new(type='ShaderNodeBsdfPrincipled')
    nodes["Principled BSDF"].inputs[0].default_value=(r,g,b,1)
    # color based on group info
    # uses two Mix nodes chained together
    groupMix=nodes.new("ShaderNodeMixRGB")
    groupMix.name="groupMix"
    groupMix.inputs[1].default_value=(1,1,0,0)
    groupMix.inputs[2].default_value=(0,0,1,0)
    mix=nodes.new("ShaderNodeMixRGB")
    mix.name="Mix"
    mix.inputs[0].default_value=0 # Fac
    links.new(mix.inputs[2],groupMix.outputs[0])
    links.new(output.inputs[0],mix.outputs[0])
    return mat

def readData(start,end,step):
    for file_i in range(start,end+1,step):
        filename=directory+"%04d"%file_i+".csv"
        frame_i=file_i/step
        print("frame %d"%frame_i)
        print(filename)
        lines=[]
        with open(filename) as f:
            lines=f.readlines()

        # read CSV data
        for i in range(1,len(lines)):
            line=lines[i].split(',')

            cylinderName="cylinder%04d"%i
            cylinder=bpy.context.scene.objects[cylinderName]
            cylinderMaterialName="cylinderMaterial.%04d"%i
            mat=bpy.data.materials.get(cylinderMaterialName)

            # create shader material
            if createMaterial:
                mat=newShader(cylinderMaterialName)
                cylinder.data.materials.clear()
                cylinder.data.materials.append(mat)

            # animate the objects
            if updatePosition:
                x=float(line[0])
                y=float(line[1])
                cylinder.location=(x,0,y)
                cylinder.keyframe_insert(data_path="location",frame=frame_i)

            # color the group
            if displayGroup:
                mixNode=mat.node_tree.nodes["Mix"]
                mixNode.inputs[0].default_value=1
                groupMixNode=mat.node_tree.nodes["groupMix"]
                group_id=int(line[4])
                groupMixNode.inputs[0].default_value=group_id/(totalGroups-1)
                groupMixNode.inputs["Fac"].keyframe_insert("default_value",frame=frame_i)

if __name__ == "__main__":
    main()