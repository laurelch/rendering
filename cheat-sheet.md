# Rendering Cheatsheet
## Contents
- [Multiplexer](#multiplexer): peform long-running task on a remote machine
- [Filename Manipulation](#filename-manipulation): batch edit filenames
- [Post-processing](#post-processing): after obtaining rendering file
  - [Convert EXR to PNG](#convert-exr-to-png): with Mitsuba renderer utilities
  - [Image Manipulation](#image-manipulation): resize, crop, append
- [Video](#video): convert PNG sequence to video
- [Storage](#storage): check storage status and file sizes
- [Renew RenderMan](#renew-renderman): renew RenderMan on Ubuntu
- [Start Maya](#start-maya): start Maya from command line
- [Basic PxrSurface](#basic-pxrsurface): basic shader in RenderMan RIB file

## Multiplexer
- Use $ screen to keep command running in background
  - Create a session
    ```
    screen
    ```
  - List all sessions
    ```
    screen -ls
    ```
  - Return to a session
    ```
    screen -r <session-#>
    ```
  - Exit current session
    ```
    Ctrl + A + D
    ```
## Filename Manipulation

- Add prefix in batch
```
ls | xargs -I {} mv {} <prefix>{}
```

- Add suffix in batch

```
ls | xargs -I {} mv {} {}<suffix>
```

- Remove prefix (for PNG files)
```
for f in *.png; do mv "$f" "${f#<prefix>}"; done;
```
## Post-processing
### Convert EXR to PNG
- Source mitsuba configuration file
```
source /path/to/mitsuba/setpath.sh
```
- Convert EXR sequence files to PNG format

Note: source the setpath.sh file if $mtsutil command does not exist.

```
mtsutil tonemap -t *.exr
```
_Windows_
```
FOR /R %a IN (*.exr) DO convert "%~a" "%~dpna.png"
```

### Image Manipulation
- Resize file, \<target-width> x \<target-height>
```
convert input.png -resize 1280x1024 resize.png
```

- Resize file, with \<target-height> only
```
convert input.png -resize x1024 resize.png
```

- Resize (or scale) file by scaling percentage
```
convert input.png -resize 50% half_input.png
```

- Crop file, \<target-width> x \<target-height> + \<left> + \<top>
```
convert input.png -crop 1280x1024+10+10 output.png
```

- Append file without gap horizontally and vertically
```
convert col_1.png col_2.png +append output.png
```
```
convert row_1.png row_2.png -append output.png
```

- Append file with gap of **n** pixels horizontally and vertically
```
convert col_1.png col_2.png +smush n output.png
```
```
convert row_1.png row_2.png -smush n col.png
```
## Video
- Convert PNG sequence to MP4 with framerate of 24
```
ffmpeg -framerate 24 -i %04d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4
```
Set starting frame to be 10
```
ffmpeg -framerate 24 -start_number 10 -i %04d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4
```
_Windows_
```
C:\ffmpeg\bin\ffmpeg.exe -framerate 24 -i %04d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4
```

- Extract frames from a video
```
ffmpeg -i output.mp4 frames.%04d.png -hide_banner
```

- Crop a video
```
ffmpeg -i input.mp4 -filter:v “crop=1920:1080:0:0” output.mp4
```

- Screencast, screen recording of whole screen on Ubuntu
```
Ctrl + Alt + Shift + R
```

## Storage
- Check total usage of disk
```
df -h --total
```

- Check size of directory
```
du -hs /path/to/directory
```

- Sort current directory with size
```
du -hs * | sort -h
```

- Find a file
```
find /path/to/find -name <filename>
```

- Find a directory
```
find /path/to/find -name <directory-name> -type d
```

- Delete all EXR files
```
find . -name '*.exr' -delete
```

## Renew RenderMan
- Render RIB file with RenderMan
```
prman -progress <file>.rib
```

To view more details
```
prman -progress -loglevel 4 <file>.rib
```

- Check RenderMan version
```
prman --version
```

- Renew RenderMan license on Linux

Note: will get license with the latest available version
```
sudo /opt/pixar/RenderManProServer-<version>/bin/LicenseApp 
```

## Start Maya
- May be shortened
```
/usr/autodesk/maya2020/bin/maya
```

## Basic PxrSurface
in RIB (RenderMan file)
```
AttributeBegin
  Bxdf "PxrSurface" "shader_name" "float diffuseGain" [1] "color diffuseColor" [1.0 1.0 1.0] "string __materialid" ["shader_name_SG"]
AttributeEnd
```
