# python2

import sys

class Queue:
    def __init__(self):
        self.q = []

    def enque(self, a):
        self.q.append(a)

    def deque(self):
        r = self.q.pop(0)
        return r

    def empty(self):
        return len(self.q) == 0

    def size(self):
        return len(self.q)

    def show(self):
        for i in self.q: print i,

'read from stdin when submitting'
class Bipartite:
    ################### BFS algorithm #############################
    def do_explore_all(self, adj, dists, s):
        q = Queue()
        dists[s] = 0
        q.enque(s)

        while not q.empty():
            v = q.deque()
            neighbours = adj[v]
            for n in neighbours:
                if dists[n] == -1:
                    dists[n] = dists[v] + 1
                    q.enque(n)
                elif (dists[n] - dists[v]) % 2 == 0:
                    return 0
        return 1

    def explore(self, adj):
        dists = [-1 for _ in range(len(adj))]

        res = 0
        for i in range(len(adj)):
            if dists[i] == -1:
                res = self.do_explore_all(adj, dists, i)
                if res == 0:
                    break
        return res

    def bipartite(self, adj):
        #write your code here
        res = self.explore(adj)
        return res

    ################# build an adjaency list from the input ######
    def load_input_from_file(self):
        f = open('./bi.txt')
        return f.readlines()

    def load_input_from_stdin(self):
        'reads several lines of input and returns it as one string'

        # reading several lines of input
        # at the end of last line press enter
        # then press cmd+d (in Intellij) or ctrl+d (in shell)
        list_input = sys.stdin.readlines()
        return list_input

    def read_input(self):
        list_input = self.load_input_from_stdin()
        input = " ".join(list_input)
        data = list(map(int, input.split()))
        return data

    def make_adj_list(self, data):
        'builds a graph adjency list from the data. data is a list of ints'

        n, m = data[0:2]
        data = data[2:]

        if (2 * m) > len(data):
            raise Exception(
                'Wrong input format. Specified %d edges but there are actually % d' % (m, len(data) / 2))
        edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

        adj = [[] for _ in range(n)]
        for (a, b) in edges:
            adj[a - 1].append(b - 1)
            adj[b - 1].append(a - 1)

        return adj

    def do(self):
        data_str = self.read_input()
        adj = self.make_adj_list(data_str)
        print(self.bipartite(adj))

if __name__ == '__main__':
    try:
        bi = Bipartite()
        bi.do()
    except Exception, e:
        print e.message