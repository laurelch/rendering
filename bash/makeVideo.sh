#!/bin/bash
# make video inside folder $1 with filename $2
ffmpeg -framerate 24 -i $1/%04d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p $1/$2.mp4