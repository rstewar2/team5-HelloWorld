#!/bin/bash
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.13.0.jar \
        -input "/user/ctatham13/M.csv" \
        -output "/user/ctatham13/v1" \
        -file mapper_20200705_Tatham.py \
        -file reducer_20200705_Tatham.py \
		    -file part1-v.txt \
        -mapper "python mapper_20200705_Tatham.py" \
        -reducer "python reducer_20200705_Tatham.py" 