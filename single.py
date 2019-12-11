from sklearn.cluster import KMeans
import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import random

k = 3

X, y = make_blobs(n_samples=1000, n_features=2, centers=[[-10,-1],[1,1],[2,2]], cluster_std=[0.4,0.5,0.2])
plt.scatter(X[:,0],X[:,1],c=y,s=3,marker='o')
plt.show()
# %%

X = np.array(X)
kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
print(kmeans.cluster_centers_)

# %%
X = np.hstack((X, np.zeros((X.shape[0], 1))))
k = 3

center_point = random.choices(X, k=k)
# %%
for i in range(7):
    center_point = [i[:-1] for i in center_point]

    labels = np.zeros(X.shape[0])
    for index in range(len(X)):
        x = X[index][:-1]
        
        distance = x - center_point
        distance = np.power(distance, 2)
        distance = np.sum(distance, 1)
        
        X[index][-1] = np.argmin(distance)
        # print(x, center_point)
    center_point = [np.mean(X[X[:, 2]==i], 0) for i in range(k)]
    # print(center_point)

print(center_point)