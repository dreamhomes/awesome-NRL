# -*- coding: utf-8 -*-

'''
@date: 2019-12-07
 
@author: dreamhomes
 
@description：deep walk pipeline
'''
import argparse
import time

from collections import Counter
from multiprocessing import cpu_count
from gensim.models import Word2Vec

import graph
from model import Skipgram


def count_words(walks):
    """cound word number.

    Arguments:
        walks {list} -- all corpus    
    Returns:
        dict -- word number
    """
    c = Counter()
    for words in walks:
        c.update(words)
    return c


def deepwalk(args):
    """deepwalk pipeline

    Arguments:
        args {dict} -- args
    """
    start_time = time.time()
    G = graph.Graph(args.input)

    total_walks = G.number_of_nodes * args.num_walks
    data_size = total_walks * args.walk_length

    print("\nNumber of nodes: {}".format(G.number_of_nodes))
    print("Number of edges: {}".format(G.number_of_edges))
    print("\nTotal number of walks: {}".format(total_walks))
    print("Data size (walks*length): {}\n".format(data_size))

    # Create the random walks and store them in walks list
    print("Generate walks ...")
    walks = G.build_deepwalk_corpus(
        num_paths=args.num_walks, path_length=args.walk_length)

    # Apply model to each walk = sentence
    print("Applying %s on walks ..." % args.model)
    if args.model == 'skipgram':
        # dictionary of the times each vertex appear in walks
        vertex_counts = count_words(walks)
        model = Skipgram(sentences=walks, vocabulary_counts=vertex_counts, size=args.dimension,
                         window=5, min_count=0, trim_rule=None, workers=cpu_count(), iter=args.iter)
    else:
        if args.model == 'word2vec':
            model = Word2Vec(walks, size=args.dimension, window=5,
                             min_count=0, sg=1, hs=1, workers=cpu_count())
        else:
            raise Exception("Unknown model: '%s'.  Valid models: 'word2vec', 'skipgram'" % args.model)

    # Save to output file
    print("----- Total time {:.2f}s -----".format(time.time() - start_time))
    model.wv.save_word2vec_format(args.output)
    return


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--num-walks', default=20, type=int)
    parser.add_argument('--walk-length', default=20, type=int)
    parser.add_argument('--dimension', type=int, default=128, help='Embeddings dimension')
    parser.add_argument('--iter', default=1, type=int, help='Number of epochs in SGD')
    parser.add_argument('--model', default='word2vec',  help='Type of model to apply on walks (word2vec/skipgram)')

    args = parser.parse_args()

    deepwalk(args)


if __name__ == "__main__":
    main()
