import sys
import os

HADOOP_CMD="/opt/hadoop-3.1.3/bin/hadoop"
HDFS_CMD="/opt/hadoop-3.1.3/bin/hdfs"
STREAM_JAR_PATH="/opt/hadoop-3.1.3/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar"


INPUT_FILE_PATH_1="/root/hadoop-test/"
CENTET_POINTS_FILE="CENTET_POINTS.txt"
LABELS_FILE="LABELS.txt"

OUTPUT_PATH="/output"

cmd = "%s dfs -cat %s%s" % (HDFS_CMD, INPUT_FILE_PATH_1, CENTET_POINTS_FILE)
# `/root/hadoop-test/CENTET_POINTS.txt

CENTET_POINTS = os.popen(cmd)

CENTET_POINTS = [[
        float(j) 
        for j in i.split(',')
    ] 
    for i in CENTET_POINTS.read().strip().split(' ')
]

for line in sys.stdin:
    points = line.strip().split()
    for point in points:
        px, py = [float(j) for j in point.split(',')]
        min_distance = -1
        min_distance_index = 0
        index = 0

        for cx, cy in CENTET_POINTS:
            distance = (cx - px) ** 2 + (cy - py) ** 2

            if min_distance == -1 or distance < min_distance:
                min_distance = distance
                min_distance_index = index
            index += 1
        print(min_distance_index, end=' ')


