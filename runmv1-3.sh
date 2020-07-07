#!/bin/bash
#dir = /home/rstewar2/Project3

#clean the output from local and hdfs
rm part-00000
hdfs dfs -rm /user/rstewar2/Project3/part-00000
hdfs dfs -rm -R /user/rstewar2/Project3/v1

# Run the first iteration
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.13.0.jar \
        -input /user/rstewar2/Project3/M.csv \
        -output /user/rstewar2/Project3/v1 \
        -file mapper_20200705_Tatham.py \
        -file reducer_20200705_Tatham.py \
        -mapper "python mapper_20200705_Tatham.py" \
        -reducer "python reducer_20200705_Tatham.py"

# get the output vector file
hdfs dfs -get /user/rstewar2/Project3/v1/part-00000
chmod -R 777 part-00000
hdfs dfs -put part-00000 /user/rstewar2/Project3
hdfs dfs -chmod -R 777 /user/rstewar2/Project3/part-00000

#Run the second iteration
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.13.0.jar \
        -input /user/rstewar2/Project3/M.csv \
        -output /home/rstewar2/v_final \
        -file mapper_part1_3.py \
        -file reducer_part1_3.py \
        -mapper "python mapper_part1_3.py" \
        -reducer "python reducer_part1_3.py"