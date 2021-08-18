# Scripting in Maya with MEL and Python
## Contents
  - [Sample Scripts](#sample-scripts)
  - [What is MEL](#what-is-mel)
  - [What is Python in Maya](#what-is-python-in-maya)
  - [How to Use Scripts in Maya](#how-to-use-scripts-in-maya)

## Sample Scripts
- [animation.mel](../maya-scripts/animation.mel)
  - Animate a continuous sequence of objects with visibility.
  - For **ObjectName_x**
    - Display and key the object in **_frame x_**.
    - Hide and key the object in **_frame 0_** and **_frame (x+1)_**.
- [animation.py](../maya-scripts/animation.py)
  - Animate one (selected) object according to a TXT file.
  - For **ObjectName**
    - Translate and key at **_frame x_** according to **_line x_** in the input file.

## What is MEL
Maya Embedded Language (MEL) is a native scripting language in Maya.

The MEL used for each task performed in GUI can be viewed in "Script Editor".

## What is Python in Maya
Python in Maya uses Maya built-in Python 2.7. 

To use Maya commands, include "maya.cmds" in the Python script.

## How to Use Scripts in Maya
Both Python in Maya and MEL can perform the same task in Maya. 

For docs of any command, click <ins>python version</ins> or <ins>MEL version</ins> at top-right of the page to toggle.

To use a script in Maya:
- go to "Script Editor" 
- create a new file in "MEL" or "Python", or read a script file
- use ExecuteAll button to execute script