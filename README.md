# **Rendering Tools and Utilities**
## Contents
- [Get Started](#get-started): Introduction to softwares, tools, and general rendering process
- [Bash Commands](#bash-commands): Commonly used bash commands
- [Bash Scripts](#bash-scripts): Commonly used bash scripts that takes inputs
- [Content Creation Softwares](#content-creation-softwares): Download and recommended tutorials
  - [Maya](#maya):
    - Python for Maya [cheat-sheet](py-maya-cheat-sheet.md)
    - install Maya on Ubuntu [guide](maya-install-ubuntu.md)
  - [Blender](#blender)
  - [RenderMan](#renderman)
  - [Houdini](#houdini)
- [References](#references): Other useful resources


## Get Started
- Softwares or tools recommended:
  - **[Maya](#maya)** or [Blender](#blender)
    - for 3D content creation: modeling, animation
    - use with renderer plugin
  - **RenderMan** and **RenderMan for Maya**
    - standalone renderer and its plugin: shading, lighting
    - can render with RIB (**R**enderMan **I**nterface **B**ytestream) file with command
        ```
        prman -progress <file-name>.rib
        ```
  - **Python**
    - **Python for Maya** ([cheat-sheet](py-maya-cheat-sheet.md)): batch modification in Maya
    - batch rendering with RIB files
  - Houdini
    - convert particles to mesh
  - Mitsuba renderer 0.6 utilities
    - convert EXR to PNG with
      ```
      mtsutil tonemap -t *.exr
      ```
- General Process Description
  1. **Modeling**
     - low-poly modeling
     - meshing from particles, with [Houdini](#houdini)
     - find free 3D models at [turbosquid](https://www.turbosquid.com/), [sketchfab](https://sketchfab.com/feed)
     - find and follow tutorial for 3D modeling
  2. UV Editing *(optional)*
  3. **Shading** (Textures, Materials)
     - use renderer's shading node (e.g [PxrSurface](https://rmanwiki.pixar.com/display/REN24/PxrSurface) with RenderMan)
     - find free textures at [textures.com](https://www.textures.com/library)
  4. Lighting
     - use renderer's lighting node (e.g [PxrDomeLight](https://rmanwiki.pixar.com/display/REN24/PxrDomeLight) with RenderMan)
  5. Camera
     - set aspect ratio, usually 1240x1024
  6. Animation
     - with built-in tools
     - **with data**, using Python (for Maya)
  7. Rendering
     - with built-in renderer (e.g Arnold in Maya, Cycles in Blender)
     - with plug-in renderer (e.g RenderMan in Maya or Blender)
     - **with standalone renderer** (e.g. RenderMan): export RIB files from Maya, then render with bash commands and Python
    <!-- - convert particles to mesh, [quick guide](houdini-particles-to-mesh.md) -->

## Bash Commands
- Check out [cheat-sheet](cheat-sheet.md) for commonly used commands:
  - [Multiplexer](cheat-sheet.md#multiplexer)
  - [Filename manipulation](cheat-sheet.md#filename-manipulation)
  - [Post-processing](cheat-sheet.md#post-processing)
  - [Video](cheat-sheet.md#video)
  - [Storage](cheat-sheet.md#storage)
  - [Renew RenderMan on Ubuntu](cheat-sheet.md#renew-renderman)

## Bash Scripts
Check out [bash](bash) folder for bash scripts (**.sh** files for Linux, **.bat** files for Windows):
  - [ccrop.sh](bash/ccrop.sh): crop with target center, and target width and height
  - [convert.bat](bash/convert.bat): batch convert EXR files to PNG files
  - [deleteLines.sh](bash/deleteLines.sh): delete lines in (RIB) files with line numbers and from the file end
  - [makeVideo.sh](bash/makeVideo.sh): make video for a given folder with given name
  - [replace.sh](bash/replace.sh): replace strings for all (RIB) files in a folder
  - [vcrop.sh](bash/vcrop.sh): crop left and right of an image with target width

## Content Creation Softwares
### Maya
- Industry standard software
- Free education version available, renews every year
- Download education version at https://www.autodesk.com/education/edu-software/overview
- Recommended tutorial:
  - [Intro to Maya Series](https://www.youtube.com/watch?v=LJLo6MafPVM) by Maya Learning Channel @YouTube
  - Maya 2019 Fundamentals @PluralSight, [preview](https://www.youtube.com/watch?v=ez6GSrMtFYI)
- Check out my [cheat-sheet](py-maya-cheat-sheet.md) for **Python for Maya** :
  - [Import](py-maya-cheat-sheet.md#import)
  - [Objects](py-maya-cheat-sheet.md#objects)
  - [Transformation](py-maya-cheat-sheet.md#transformation)
  - [Shading](py-maya-cheat-sheet.md#shading)
  - [Animation](py-maya-cheat-sheet.md#animation)
- To install Maya on **Ubuntu**, check this [install guide](maya-install-ubuntu.md) that worked for me

### Blender
- Free, open-source, handy, and beginner-friendy
- Download at https://www.blender.org/
- Recommended tutorial:
  - [Grant Abbitt](https://www.youtube.com/channel/UCZFUrFoqvqlN8seaAeEwjlw) @YouTube, and his complete beginners [guide](https://www.youtube.com/watch?v=wNQYhbvTJi8)
  - Many other resources @YouTube

### RenderMan
- Free non-commercial license available, renews every 3 months
- Download at https://renderman.pixar.com/store
- Recommended tutorial:
  - [RenderMan Docs](https://rmanwiki.pixar.com/display/REN24/RenderMan): official RenderMan Docs, installation guides, plugins guides
  - [Learn RenderMan](https://renderman.pixar.com/learn): official RenderMan learning resources
  - [Small Robot Studio](https://www.youtube.com/channel/UCvRPmhwzn2pFdLes0vcTeJQ) @YouTube: learn specific RenderMan shading features

### Houdini
- Procedural generation software, commonly used for visual effects
- Many versions, including free and indie version, avaialble at https://www.sidefx.com/buy/
- Recommended tutorial:
  - [Learning Houdini](https://www.sidefx.com/learn/getting_started/): official SideFX get started tutorial
- Check out how I use houdini for [meshing](houdini-particles-to-mesh.md)

<!-- TODO: ### Others
- Check out my [experiences](experiences.md): get inspired by my stories with content creation softwares
  - [Maya](experiences.md#maya-)
  - [RenderMan](experiences.md#renderman-)
  - [Blender](experiences.md#blender-) -->

## References: 
  - Bash scripting cheatsheet: [devhints.io/bash](https://devhints.io/bash)
  - Python for Maya commands: [Docs (2017 version)](https://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/CommandsPython)
  - Udemy: 3D and Animation [courses](https://www.udemy.com/courses/design/3d-and-animation/), high-quality with regular discounts

<!-- TODO: Q&A
One question: I currently have windows 10, should I download Ubuntu or is it ok to do everything in windows?

Answer:General speaking you can do everything with your own machine, and you should get started with your own machine. 
Only when you need to render for paper submission, since rendering is a time-consuming and heavy work, it is better to utilize lab machines (Ubuntu) to avoid crash on your own machine or disturbing your other works. 
We can talk more on the details about how to transfer your work to lab machines later.
-->

