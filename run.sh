export JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64/"
HADOOP_CMD="/opt/hadoop-3.1.3/bin/hadoop"
HDFS_CMD="/opt/hadoop-3.1.3/bin/hdfs"
STREAM_JAR_PATH="/opt/hadoop-3.1.3/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar"

INPUT_FILE_PATH_1="/root/hadoop-test/"
CENTET_POINTS_FILE="/root/hadoop-test/CENTET_POINTS.txt"
LABELS_FILE="/root/hadoop-test/LABELS.txt"

OUTPUT_PATH="/output"

$HDFS_CMD dfs -rm -r -skipTrash $INPUT_FILE_PATH_1
$HDFS_CMD dfs -mkdir -p $INPUT_FILE_PATH_1
$HDFS_CMD dfs -put $INPUT_FILE_PATH_1/input/* $INPUT_FILE_PATH_1
$HDFS_CMD dfs -rm -r -skipTrash $OUTPUT_PATH


$HADOOP_CMD jar $STREAM_JAR_PATH   \
-input $INPUT_FILE_PATH_1   \
-output $OUTPUT_PATH   \
-mapper "python3 mapper.py"   \
-reducer "python3 reducer.py"  \
-file ./mapper.py   \
-file ./reducer.py  \

$HDFS_CMD dfs -cat /output/part-00000