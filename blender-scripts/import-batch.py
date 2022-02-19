"""
Import a sequence of OBJ files.
Optional: apply translation while import.
"""
import os
import bpy

path_to_obj_dir="/path/to/directory"
file_list=sorted(os.listdir(path_to_obj_dir))
obj_list=[item for item in file_list if item.endswith('.obj')]

bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)

count=0
for item in obj_list:
    path_to_file=path_to_obj_dir+"/"+item
    bpy.ops.import_scene.obj(filepath=path_to_file)
    obj_name=os.path.splitext(item)[0]
    print(obj_name)

    # (Optional) apply translation to object while import
    obj=bpy.context.scene.objects[obj_name]
    if(count<100):
        obj.location[0]=-1.1+(0.02*count)
    else:
        break

    count=count+1