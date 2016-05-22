import numpy as np

if __name__ == "__main__":
    clusters = np.load("clusters_result.npy")

    f_clusters = open("kmeans_result", 'r')
    clusters = dict()
    for i in range(13):
        clusters[i] = []

    cnt = 0
    for line in f_clusters:
        clusters[int(line)].append(cnt)
        cnt = cnt + 1

    f_data = open("../data/train_large.csv", 'r')
    actual_clusters = []
    actual_bins = [0 for _ in range(13)]
    for line in f_data:
        line = line.split(',')
        actual_clusters.append(int(line[0]))
        actual_bins[int(line[0])] = actual_bins[int(line[0])] + 1

    for i in range(13):
        print actual_bins[i]
    print '=' * 79


    total_cnt = 0
    for i in range(13):
        cluster = clusters[i]
        #print cluster
        bins = [0 for _ in range(13)]
        for c in cluster:
            bins[actual_clusters[c]] = bins[actual_clusters[c]] + 1

        print max(bins), sum(bins)
        print bins.index(max(bins))
        total_cnt = total_cnt + max(bins)

    print total_cnt / (cnt * 1.0)

            


