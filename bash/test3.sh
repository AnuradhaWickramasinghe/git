#!/bin/bash

. info.properties
top -b -n1 | sed -n '7,$p'  > $file1 
cat $file1 | awk '{for(i=1 ; i <=NF ; i++){printf "<td>%s</td> " ,$i}; printf "\n"}' > $file4


echo "<html><head></head><body><table>" > $file3
while read line
do
	echo $line
	echo "<tr> $line </tr>" >> $file3
done < $file4

echo "</table></body><html>" >> $file3
