# python2

import sys
from math import sqrt
from math import pow


class BinHeap:
    '''
    this is a binary heap of tuples. each tuple has two integers, the key and the value.
    the tuples in the heap are order by the key.
    '''

    def key(self, t):
        return t[0]

    def val(self, t):
        return t[1]

    def __init__(self):
        self.heap = [(0, -5000000)]
        self.size = 0

    def empty(self):
        return self.size == 0

    def insert(self, t):
        self.size = self.size + 1
        self.heap.append(t)
        self.percUp(self.size)

    def delMin(self):
        if self.size == 0:
            return None
        t_res = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop(self.size)
        self.size = self.size - 1

        if self.size != 0:
            self.percDown(1)

        return t_res

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.size = len(alist)
        self.heap = [(0, -5000000)] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

    def hasVal(self, val):
        i = -1
        for n in range(1, len(self.heap)):
            if self.val(self.heap[n]) == val:
                i = n
                break
        return i

    def changeVal(self, val, key):
        '''
        not standard heap API. required for the implementation of Dijkstra algorithm.
        each member of the heap is a tuple with two values. t[0] is the heap key also the vertes distance.
        t[1] is the value also the vertex.
        '''
        i = self.hasVal(val)
        if i == -1:
            return


        self.heap[i] = (key, val)

        min_child = self.min(self.heap, i)
        father = i // 2

        if self.key(self.heap[father]) > self.key(self.heap[i]):
            self.percUp(i)
        elif min_child and self.key(self.heap[min_child]) < self.key(self.heap[i]):
            self.percDown(i)


    def percUp(self, i):
        while i // 2 > 0:
            up = i // 2
            key_i = self.key(self.heap[i])
            key_up = self.key(self.heap[up])
            if key_i < key_up:
                self.swap(self.heap, up, i)
            i = up

    def percDown(self, i):
        while i < self.size:
            smallest = self.min(self.heap, i)
            if smallest == None:
                break
            elif self.key(self.heap[ smallest ]) < self.key(self.heap[i]):
                self.swap(self.heap, i, smallest)
                i = smallest
            else:
                break

    def swap(self, ls, one, two):
        tmp = ls[one]
        ls[one] = ls[two]
        ls[two] = tmp

    def min(self, ls, i):
        'between two children of i, will return the index of the one which has a smaller value'
        first = 2 * i
        sec = first + 1


        if sec > self.size and first <= self.size:
            res = first
        elif first > self.size:
            res = None
        else:
            key_first = self.key(ls[first])
            key_sec = self.key(ls[sec])
            if key_first <= key_sec:
                res = first
            else:
                res = sec

        return res

'''
read from stdin when submitting
Find the MinimL Spanning Tree of a graph using the Prim algorithm
'''
class ConnectingPrim:
    ################### Dijkstra's algorithm #############################
    def do_explore_all(self, adj, cost, dist, prev, s):
        q = BinHeap()
        size = len(adj)
        inlist = [ (self.INFINITY, i) if i != s else (0, i) for i in range(size)]
        q.buildHeap(inlist)

        while not q.empty():
            vertex = q.delMin()
            v = vertex[1]
            neighbours = zip(adj[v], cost[v])
            for onen in neighbours:
                n, c  = onen[0], onen[1]
                if q.hasVal(n) and dist[n] > c:
                    dist[n], prev[n] = c, v

                    idx = -1
                    back = adj[n]
                    for b in range(len(back)):
                        if back[b] == v:
                            idx = b; break;
                    if idx != -1:
                        adj[n].pop(idx) # the tricky part
                        cost[n].pop(idx)

                    q.changeVal(n, c)

    def explore(self, adj, cost, s):
        dists = [self.INFINITY if i != s else 0  for i in range(len(adj))]
        prev = [None for _ in range(len(adj))]
        self.do_explore_all(adj, cost, dists, prev, s)
        return dists

    def minimum_distance(self, x, y):
        self.INFINITY = 1000 * len(x)

        adj, cost = self.make_graph_ds(x, y)
        distances = self.explore(adj, cost, 0)
        min_span = sum(distances)
        return "%.9f" % min_span

    def make_graph_ds(self, x, y):
        adj, cost = [], []

        vertices = zip(x, y)
        size = len(vertices)
        for i in range(size):
            adj.append([])
            cost.append([])
            for j in range(size):
                if j == i:
                    continue
                adj[i].append(j)
                dist_ij = self.pyta(vertices, i, j)
                cost[i].append(dist_ij)

        return adj, cost

    def pyta(self,verts, i, j):
        width = verts[j][0] - verts[i][0]
        width = pow(width, 2)

        height = verts[j][1] - verts[i][1]
        height = pow(height, 2)

        alahson = sqrt(width + height)
        return alahson


    ################# build an adjaency list from the input ######
    def load_input_from_file(self):
        f = open('./connecting.txt')
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

        n = data[0]
        x = data[1::2]
        y = data[2::2]

        if len(x) != len(y):
            raise Exception('Wrong input format. X vector should have the same size as the Y vector')

        return x, y

    def do(self):
        data_str = self.read_input()
        x, y = self.make_adj_list(data_str)
        print(self.minimum_distance(x, y))

if __name__ == '__main__':
    try:
        prim = ConnectingPrim()
        prim.do()
    except Exception, e:
        print e.message
