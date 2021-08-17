# Python for Maya Cheatsheet
## Contents
  - [Import](#import)
  - [Objects](#objects)
  - [Transformation](#transformation)
  - [Shading](#shading)
  - [Animation](#animation)

## Import
- Import maya commands
```
import maya.cmds as mc
```

## Objects

- [Select](https://download.autodesk.com/global/docs/maya2012/en_us/CommandsPython/select.html) all objects with given name (full or partial name)
```
select_all=mc.ls("<name>")
mc.select(select_all)
```
```
select_all=mc.ls("*<partial name>*")
mc.select(select_all)
```
r = replace the existing item on the active list
```
mc.select("<name>",r=True)
```
- Check if an object exists
```
mc.objExists("<name>")
```

- [Delete](https://download.autodesk.com/us/maya/2009help/commandspython/delete.html) the object(s), if the object exists
```
if(mc.objExists("<name>")):
    mc.select("<name>",r=True)
    mc.delete()
```
  
## Transformation
- Translate object with [move](https://download.autodesk.com/us/maya/2011help/Commandspython/move.html) command
```
mc.move(x,y,z,name,absolute=True)
```

- Rotate object with [rotate](https://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/CommandsPython/rotate.html) command
```
mc.rotate('90deg',0,0,name)
```

- Scale object with [scale](https://download.autodesk.com/us/maya/2011help/commandspython/scale.html) command
```
mc.scale(x,y,z,name,absolute=True)
```

## Shading
- Apply material (shading group) with [sets](https://download.autodesk.com/us/maya/2011help/commandspython/sets.html) command
```
mc.sets(name,forceElements="<shader-name>_SG")
```

- Set attribute with [setAttr](https://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/CommandsPython/setAttr.html) command, attribute may be a color [r,g,b]
```
mc.setAttr(shape_name+".<attribute_name>",r,g,b)
```
The attribute may be a float x
```
mc.setAttr(shape_name+".<attribute_name>",x)
```
## Animation 
- Set [current time](https://download.autodesk.com/us/maya/2011help/Commandspython/currentTime.html), set current frame to 1
```
mc.currentTime(1)
```

- Set [keyframe](https://download.autodesk.com/us/maya/2009help/commandspython/setKeyframe.html) of translate X with value "x"
```
mc.setKeyframe(name,v=x,at='tx',t=frame)
```
```
mc.setKeyframe(name,v=x,at='translateX',t=frame)
```

- Cut animation keys with [cutKey](https://download.autodesk.com/us/maya/2011help/commandspython/cutKey.html) command 
  
Cut all keys of all active objects, from frame 0 to 100
```
mc.cutKey(time=(0,100))
```