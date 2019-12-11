import sys
import os

HADOOP_CMD="/opt/hadoop-3.1.3/bin/hadoop"
HDFS_CMD="/opt/hadoop-3.1.3/bin/hdfs"
STREAM_JAR_PATH="/opt/hadoop-3.1.3/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar"


INPUT_FILE_PATH_1="/root/hadoop-test/"
CENTET_POINTS_FILE="CENTET_POINTS.txt"
LABELS_FILE="LABELS.txt"

OUTPUT_PATH="/output"

cmd = "%s dfs -cat %sinput/data.txt" % (HDFS_CMD, INPUT_FILE_PATH_1)
# `/root/hadoop-test/input/data.txt
data = os.popen(cmd)
data = [[
        float(j) 
        for j in i.split(',')
    ] 
    for i in data.read().strip().split(' ')
]

k = 3

new_center_point = [[0, 0] for i in range(k)]


for line in sys.stdin:
    labels = line.strip().split()
    for d, label in zip(data, labels):
        label = int(label)
        new_center_point[label][0] += d[0]
        new_center_point[label][1] += d[1]
for i in range(k):
    new_center_point[i][0] /= len(data)
    new_center_point[i][1] /= len(data)

print(" ".join(["%.16f,%.16f"%tuple(i) for i in new_center_point]))