"""
Translate and key one selected object 
according to input file
"""
import maya.cmds as mc
import math

directory = "./"
file_name = directory + 'animation.txt'
lines = []
with open(file_name) as f:
    lines = f.readlines()
for i in range(len(lines)):
    line = lines[i].split()
    current_frame = line[0]
    print(current_frame)
    
    # parse line
    x = float(line[2])-0.006
    y = 0.45
    z = float(line[4])-0.009

    # key object
    mc.currentTime(current_frame)
    mc.move(x,y,z,y=False,a=True)
    mc.setKeyframe('ObjectName',v=x,at='translateX')
    mc.setKeyframe('ObjectName',v=y,at='translateY')
    mc.setKeyframe('ObjectName',v=z,at='translateZ')