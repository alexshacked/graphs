# python2

import sys

'read from stdin when submitting'
class NegativeCycles:
    ################### Dijkstra's algorithm #############################
    def do_explore_all(self, adj, cost, dist, prev):
        'we are looking for a negative cycle here. this will be decided in the last MAIN_ITER'
        dist[0], MAIN_ITER = 0,  len(adj)

        for _ in range(MAIN_ITER):
            relax = False
            for vi in range(len(adj)): # go over all edges in each MAIN_ITER
                neighbours = zip(adj[vi], cost[vi])
                for one_neighbour in neighbours: # go over al neighbours of vi and try to relax them
                    neigh_idx, neigh_cost = one_neighbour[0], one_neighbour[1]
                    if dist[neigh_idx] > (dist[vi] + neigh_cost): # relax
                        relax, dist[neigh_idx], prev[neigh_idx] = True,   dist[vi] + neigh_cost,   vi
            # finished one MAIN_ITER -  one iteration over all edges. now conclusions:
            if relax == False: # at current MAIN_ITER we couldnt relax any node. no negative cycles. we leave
                return 0
        else:
            return 1

    def explore(self, adj, cost):
        dists = [self.INFINITY for _ in range(len(adj))]
        prev = [None for _ in range(len(adj))]
        is_negative = self.do_explore_all(adj, cost, dists, prev)
        return is_negative

    def negative_cycle(self, adj, cost):
        self.INFINITY = 1000 * len(adj)

        is_negative_cycle = self.explore(adj, cost)
        return is_negative_cycle

    ################# build an adjaency list from the input ######
    def load_input_from_file(self):
        f = open('./negative.txt')
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

        if (3 * m) > len(data):
            raise Exception(
                'Wrong input format. Specified %d edges but there are actually % d' % (m, len(data) / 3))
        edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))

        adj = [[] for _ in range(n)]
        cost = [[] for _ in range(n)]
        for ((a, b), w) in edges:
            adj[a - 1].append(b - 1)
            cost[a - 1].append(w)

        return adj, cost

    def do(self):
        data_str = self.read_input()
        adj, cost = self.make_adj_list(data_str)
        print(self.negative_cycle(adj, cost))

if __name__ == '__main__':
    try:
        ngc = NegativeCycles()
        ngc.do()
    except Exception, e:
        print e.message



