#!/bin/bash
# crop left & right of a 1280x1024 image
# input: target width
let "w=(1280-$2)/2"
convert $1.png -crop $2x1024+$w+0 $1_2.png