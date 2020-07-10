#!/bin/bash

# Cleanup
#rm part-00000
#rm part-00000.txt
#hdfs dfs -rm -R /user/rstewar2/Project3/Google_v1
hdfs dfs -rm -R /user/rstewar2/Project3/Google_vfinal

# Run the first iteration
#hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.13.0.jar \
#        -input /user/rstewar2/Project3/Google_M.csv \
#        -output /user/rstewar2/Project3/Google_v1 \
#        -file mapper_part2_1.py \
#        -file reducer_part2_1.py \
#	-file initial_V.txt \
#        -mapper "python mapper_part2_1.py" \
#        -reducer "python reducer_part2_1.py"

# Retrieve the vector file
#hdfs dfs -chmod 777 /user/rstewar2/Project3/Google_v1/part-00000
#hdfs dfs -get /user/rstewar2/Project3/Google_v1/part-00000
#iconv -f utf-16 -t ascii part-00000 > part-00000.txt
#chmod 664 part-00000
#mv part-00000 part-00000.txt
#hdfs dfs -put part-00000.txt /user/rstewar2/Project3

# Run the second iteration
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.13.0.jar \
        -input /user/rstewar2/Project3/Google_M.csv \
        -output /user/rstewar2/Project3/Google_vfinal \
        -file mapper_part2_2.py \
        -file reducer_part2_2.py \
	-file part-00000 \
        -mapper "python mapper_part2_2.py" \
        -reducer "python reducer_part2_2.py"
