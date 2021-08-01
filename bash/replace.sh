#!/bin/bash
# replace string(s) for each file in folder $1
cd $1
echo "replace in $1"
# disable RIB file generation of statistics XML file
replace="s/Option\ \"statistics\"/#Option\ \"statistics\"/g;\
s/foo/bar/g;"
find . -maxdepth 1 -type f -exec sed -i "$replace" {} \;