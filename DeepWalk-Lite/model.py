# -*- coding: utf-8 -*-

'''
@date: 2019-12-07
 
@author: dreamhomes
 
@description：skig-gram model setting
'''

from gensim.models import Word2Vec
from multiprocessing import cpu_count


class Skipgram(Word2Vec):

    def __init__(self, vocabulary_counts=None, **kwargs):

        self.vocabulary_counts = None

        kwargs["min_count"] = kwargs.get("min_count", 0)
        kwargs["workers"] = kwargs.get("workers", cpu_count())
        kwargs["size"] = kwargs.get("size", 128)
        kwargs["sentences"] = kwargs.get("sentences", None)
        kwargs["window"] = kwargs.get("window", 10)
        kwargs["sg"] = 1  # 1 for skip-gram; otherwise CBOW.
        kwargs["hs"] = 1  # hierarchical softmax

        if vocabulary_counts != None:
            self.vocabulary_counts = vocabulary_counts

        super(Skipgram, self).__init__(**kwargs)
