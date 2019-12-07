# -*- coding: utf-8 -*-

'''
@date: 2019-12-07

@author: dreamhomes

@description：nx.Graph and generate random walks.
'''
import random
import networkx as nx


class Graph(object):
    def __init__(self, graph_path):
        """ undirected graph initialization. """

        self.G = nx.read_edgelist(graph_path)
        self.number_of_nodes = self.G.number_of_nodes()
        self.number_of_edges = self.G.number_of_edges()
        self.nodes = self.G.nodes(data=True)
        self.edges = self.G.edges(data=True)

    def random_walk(self, path_length, alpha=0, rand=random.Random(), start=None):
        """Returns a truncated random walk.
        
        Arguments:
            path_length {int} -- random walk length(sentence length).
        
        Keyword Arguments:
            alpha {int} -- probability of restart (default: {0})
            rand {Random obj} -- random seed (default: {random.Random()})
            start {node} -- node start (default: {None})
        """        
        G = self.G
        if start:  # Select start node.
            path = [start]
        else:
            path = [rand.choice(list(G.nodes(data=False)))]
            
        while len(path) < path_length:
            cur = path[-1]
            if len(G[cur]) > 0:
                if rand.random() >= alpha:
                    path.append(rand.choice(list(G[cur].keys())))
                else:
                    path.append(path[0])
            else:
                break
        return [str(node) for node in path]


    def build_deepwalk_corpus(self, num_paths, path_length, alpha=0, rand=random.Random(0)):
        """[summary]
        
        Arguments:
            num_paths {int} -- sentence length
            path_length {int} -- path
        
        Keyword Arguments:
            alpha {int} -- probility to restart (default: {0})
            rand {[type]} --  (default: {random.Random(0)})
        
        Returns:
            list -- walks
        """        
        temp_G = self.G
        walks = []
        nodes = list(temp_G.nodes())

        for cnt in range(num_paths):
            rand.shuffle(nodes)
            for node in nodes:
                walks.append(self.random_walk(path_length, rand=rand, alpha=alpha, start=node))

        return walks


if __name__ == '__main__':
    G = Graph('../data/BlogCatalog/blog.edgelist')
    print(G.number_of_nodes)
    print(G.build_deepwalk_corpus(1, 2))
