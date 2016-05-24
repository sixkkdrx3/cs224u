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
        print actual_bins[i],
    print
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

    print '=' * 79
    C = range(13)
    S = range(13)
    greedy_assignment = dict()
    while len(C) > 0:
        best_cnt = -1
        best_cluster = 0
        best_category = 0
        for c in C:
            max_cnt = -1
            max_cluster = 0
            for s in S:
                cnt = 0
                cluster = clusters[s]
                for cc in cluster:
                    if actual_clusters[cc] == c:
                        cnt = cnt + 1
                if cnt > max_cnt:
                    max_cnt = cnt
                    max_cluster = s

            if max_cnt > best_cnt:
                best_cnt = max_cnt
                best_cluster = max_cluster
                best_category = c

        C.remove(best_category)
        S.remove(best_cluster)
        greedy_assignment[best_cluster] = best_category


    print greedy_assignment
    total_cnt = 0
    for i in range(13):
        cluster = clusters[i]
        for c in cluster:
            if actual_clusters[c] == greedy_assignment[i]:
                total_cnt = total_cnt + 1

    print total_cnt / (40000.0)
