#!/bin/bash
# delete lines 1-27
# delete from file end to "WorldEnd"
# to remove settings in RIB files
cd $1
echo "delete in $1"
delete="1,27d;$d;/^WorldEnd /d"
find . -maxdepth 1 -type f -exec sed -i "$delete" {} \;