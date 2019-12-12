# hadoop-kmeans
分布式kmeans

```
生成随机中心^ bash
do
    获取中心点^ mapper from center_points.txt
    计算与中心点距离^ mapper 
    确定数据新类^ mapper to labels.txt
    生成新中心^ reducer to center_points.txt
while 中心变化不大: ^ bash


```