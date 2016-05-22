import numpy as np
from sklearn import cluster

if __name__ == "__main__":
    parent_dir = "../data/"
    train_filename = parent_dir + "train_large.csv"
    f_train = open(train_filename, 'r')

    cnt = 0
    X = np.zeros(shape=(40000, 5000))
    for line in f_train:
        args = line.split(',')
        row = np.array(args[1:])
        X[cnt, :] = row
        cnt += 1
        if cnt % 1000 == 0:
            print cnt

    print np.shape(X)

    k_means = cluster.KMeans(n_clusters=13, n_init=4)

    clusters = k_means.fit_predict(X)
    out_f = open("kmeans_result", 'w')
    for c in clusters:
        out_f.write("%d\n" % c)


