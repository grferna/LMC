#! /bin/bash

files=(`ls *isomin*`)

for i in "${files[@]}"
do
    echo $i
done
