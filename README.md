# hadoop-kmeans
分布式kmeans

生成随机中心^ bash
do
    计算与中心点距离^ mapper
    确定数据新类^ mapper
    生成新中心^ reducer
while 中心变化不大: ^ reducer