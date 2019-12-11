import random
from pathlib import Path
from sklearn.datasets import make_blobs


X, Y = make_blobs(
    n_samples=1000, n_features=2, 
    centers=[[-0.3, -0.3], [0, 0], [0.3, 0.3]], 
    cluster_std=[0.01, 0.02, 0.03]
)
points = []
labels = []
for x, y in zip(X, Y):
    points.append("%.16f,%.16f" % tuple(x))
    labels.append("%d" % y)

with open('./LABELS.txt', 'w') as f:
    f.write(" ".join(labels))
with open('./input/data.txt', 'w') as f:
    f.write(" ".join(points))

with open('./CENTET_POINTS.txt', 'w') as f:
    f.write(" ".join(["%.16f,%.16f" % tuple(random.choice(X)) for i in range(3)]))
