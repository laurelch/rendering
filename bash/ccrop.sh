#!/bin/bash
# crop image with target center (c1,c2)
# and target image width (w) and height (h)
c1=$2
c2=$3
w=$4
h=$5
let "left=$c1-($w/2)"
let "top=$c2-($h/2)"
convert $1.png -crop $w\x$h+$left+$top $1_2.png