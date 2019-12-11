export JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64/"
HADOOP_CMD="/opt/hadoop-3.1.3/bin/hadoop"
HDFS_CMD="/opt/hadoop-3.1.3/bin/hdfs"
STREAM_JAR_PATH="/opt/hadoop-3.1.3/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar"


INPUT_FILE_PATH_1="/root/hadoop-test/"
CENTET_POINTS_FILE="CENTET_POINTS.txt"
LABELS_FILE="LABELS.txt"

OUTPUT_PATH="/output"


python3 ./generate_data.py
$HDFS_CMD dfs -rm -r -skipTrash $INPUT_FILE_PATH_1
$HDFS_CMD dfs -mkdir -p $INPUT_FILE_PATH_1

$HDFS_CMD dfs -put ./$CENTET_POINTS_FILE $INPUT_FILE_PATH_1$CENTET_POINTS_FILE
$HDFS_CMD dfs -put ./$LABELS_FILE $INPUT_FILE_PATH_1$LABELS_FILE
$HDFS_CMD dfs -put $INPUT_FILE_PATH_1/input $INPUT_FILE_PATH_1/input


for i in {1..3}
do
    echo 第$i次
    $HDFS_CMD dfs -rm -r -skipTrash $OUTPUT_PATH
    $HADOOP_CMD jar $STREAM_JAR_PATH   \
    -input $INPUT_FILE_PATH_1/input   \
    -output $OUTPUT_PATH   \
    -mapper "python3 mapper.py"   \
    -reducer "python3 reducer.py"  \
    -file ./mapper.py   \
    -file ./reducer.py 

    $HDFS_CMD dfs -rm $INPUT_FILE_PATH_1$CENTET_POINTS_FILE
    $HDFS_CMD dfs -cp $OUTPUT_PATH/part-00000 $INPUT_FILE_PATH_1$CENTET_POINTS_FILE
    echo 当前中心点: 
    $HDFS_CMD dfs -cat /output/part-00000
done

