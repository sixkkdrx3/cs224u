import numpy as np
from sklearn import cluster
import sys
import os
import utils

def tfidf(mat):
    colsums = np.sum(mat, axis=0)
    doccount = mat.shape[1]
    w = np.array([_tfidf_row_func(row, colsums, doccount) for row in mat])
    return w

def _tfidf_row_func(row, colsums, doccount):
    df = float(len([x for x in row if x > 0]))
    idf = 0.0
    if df > 0.0 and df != doccount:
        idf = np.log(doccount / df)
    tfs = row/colsums
    return tfs * idf

def extract_top_words():
    f = open('word_list.txt', 'r')
    line = f.readline()
    words = line.split(',')
    return words

if __name__ == "__main__":
    total_songs = 10010
    total_words = 5000
    top_words = 5

    train_filename = sys.argv[1]
    f_train = open(train_filename, 'r')

    cnt = 0
    X = np.zeros(shape=(total_words, total_songs))
    for line in f_train:
        args = line.split(',')
        row = np.array(args[1:])
        X[:, cnt] = row
        cnt += 1
        if cnt % 1000 == 0:
            print cnt

    X = tfidf(X)
    glove_home = 'glove.6B'
    GLOVE = utils.glove2dict(os.path.join(glove_home, 'glove.6B.100d.txt'))

    Y = np.zeros(shape=(total_songs, 100))
    word_list = extract_top_words()
    for i in range(total_songs):
        order = np.argsort(X[:, i])
        words = []
        for j in range(top_words):
            words.append(word_list[order[j]])
        
        allvecs = np.array([GLOVE[w] for w in words if w in GLOVE])
        feature = np.sum(allvecs, axis=0)

        Y[i,:] = feature


    k_means = cluster.KMeans(n_clusters=10, n_init=4)

    clusters = k_means.fit_predict(Y)
    out_f = open("kmeans_plus_result", 'w')
    for c in clusters:
        out_f.write("%d\n" % c)


    
