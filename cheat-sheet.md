# Rendering Cheatsheet

## Common Commands

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

- Crop file
```
convert input.png -crop 1280x1024+10+10 output.png done
```

- Activate Mitsuba Utilities (mtsutil)
```
source /path/to/mitsuba/setpath.sh
```

- Use MItsuba to convert EXR to PNG file
```
mtsutil tonemap -t *.exr
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
- Convert EXR sequence files to PNG format

(Windows)
```
FOR /R %a IN (*.exr) DO convert "%~a" "%~dpna.png"
```
- Convert PNG sequence to MP4 with framerate of 24
```
ffmpeg -framerate 24 -i %04d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4
```
(Windows)
```
C:\ffmpeg\bin\ffmpeg.exe -framerate 24 -i %04d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4
```

- Check size of directory
```
du -hs /path/to/directory
```

- Sort current directory with size
```
du -hs * | sort -h
```

- Use screen to keep command running in background
```
screen
screen -ls
screen -r
// ctrl + A + D, to exit
```

- Find a file (or directory)
```
find /path/ -name filename (-type d)
```

## Uncommon Commands

- Renew RenderMan license on Linux, after filling the survey online, without installing newest version
```
sudo /opt/pixar/RenderManProServer-<version>/bin/LicenseApp 
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

- Scale a video
```
ffmpeg -i input.mp4 -vf scale=1280:-1 output.mp4
```
