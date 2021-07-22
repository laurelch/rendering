# Rendering Cheatsheet
## Contents
- [Multiplexer](#multiplexer): peform long-running task on a remote machine
- [Filename Manipulation](#filename-manipulation): batch edit filenames
- [Post-processing](#post-processing): convert EXR to PNG, crop files
- [Video](#video): convert PNG sequence to video
- [Storage](#storage): check storage status and file sizes
- [Renew RenderMan](#renew-renderman): renew RenderMan on Ubuntu

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
    // ctrl+A+D
    ```
## Filename Manipulation

- Add prefix in batch
```
ls | xargs -I {} mv {} PRE_{}
```

- Add suffix in batch

```
ls | xargs -I {} mv {} {}_SUF
```

- Remove prefix (PNG files)
```
for f in *.png; do mv "$f" "${f#PRE_}"; done;
```

## Post-processing
- Convert EXR sequence files to PNG format
```
(source /path/to/mitsuba/setpath.sh)
mtsutil tonemap -t *.exr
```
(Windows)
```
FOR /R %a IN (*.exr) DO convert "%~a" "%~dpna.png"
```

- Crop file
```
convert input.png -crop 1280x1024+10+10 output.png done
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
(Windows)
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

- Find a file (or directory)
```
find /path/ -name filename (-type d)
```

## Renew RenderMan

- Renew RenderMan license on Linux, after filling the survey online, without installing newest version
```
sudo /opt/pixar/RenderManProServer-<version>/bin/LicenseApp 
```
