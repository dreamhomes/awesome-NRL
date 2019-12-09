# -*- coding: utf-8 -*-

'''
@date: 2019-12-08

@author: dreamhomes

@description：evaluate model on datasets.
'''
import argparse
import sys
import networkx as nx
import numpy as np
from gensim.models import KeyedVectors
from sklearn.linear_model import LogisticRegression


def encode_onehot(labels):
    classes = set(labels)
    classes_dict = {c: np.identity(len(classes))[i, :] for i, c in enumerate(classes)}
    labels_onehot = np.array(
        list(map(classes_dict.get, labels)), dtype=np.int32)
    return labels_onehot


def get_splits():
    """HELPER FUNCTIONS FOR SPLITTING DATA TRAIN, VALIDATION, TEST"""
    idx_train = range(200)
    idx_val = range(200, 500)
    idx_test = range(500, 1500)
    return idx_train, idx_val, idx_test


def main():
    """Evaluate:Perform Logistic Regression of embedding"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--embedding", required=True, help="Embedding file.")
    parser.add_argument("--network", required=True, help="A .edgelist network file.")
    parser.add_argument("--labels", required=True)

    args = parser.parse_args()

    # Load Embeddings
    embeddings_file = args.embedding
    model = KeyedVectors.load_word2vec_format(embeddings_file, binary=False)

    # Load graph and labels
    graph = nx.read_edgelist(args.network)
    idx_label = np.genfromtxt(args.labels, dtype=np.dtype(str))

    # Map nodes to features
    features_matrix = np.asarray([model[node] for node in idx_label[:, 0]])
    # Map nodes to onehot labels
    print("Dataset has {} classes.".format(len(set(idx_label[:, 1]))))
    labels_matrix = idx_label[:, 1]

    # Split in training, validation, test set
    X, y = features_matrix, labels_matrix

    idx_train, idx_val, idx_test = get_splits()
    y_train = y[idx_train]
    y_val = y[idx_val]
    y_test = y[idx_test]
    X_train = X[idx_train]
    X_test = X[idx_test]

    # Logistic Regression

    # Train on data
    logisticRegr = LogisticRegression()
    logisticRegr.fit(X_train, y_train)

    # Measure accuracy
    score = logisticRegr.score(X_test, y_test)

    # Output results
    print('---------------------------------')
    print('Accuracy Score :   ', score)
    print('---------------------------------')

if __name__ == "__main__":
    sys.exit(main())
