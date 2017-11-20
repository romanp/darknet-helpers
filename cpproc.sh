#!/bin/bash
num=0
while [ 1 ]
do
  if [ $(ls -1A ./predictions.png wc -l 2>/dev/null | wc -l 2>/dev/null) -gt 0 ]
  then
    mv ./predictions.png ./result/predictions-$num.png
    (( ++num ))
  fi
done
