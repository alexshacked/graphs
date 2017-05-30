#python2

import sys

# 1. preorder and postorder clocks for every vertex in G
# 2. G' is the reverse graph of G
# 3. find the vertex with the highest postorder number in G'.
#    this vertex l is in a sink SCC_1 in G
# 4. dfs on l in G to find all the vertices in the SCC of l
# 5. remove the sink vertices of SCC_1 from G'
# 6. the next component in G' the postorder sort belongs to the next SCC

'read from stdin when submitting'
class Acyclicity:
    ################### DFS algorithm #############################
    def do_explore_reverse_one(self, i, adj, visit, pre, post, clock):
        visit[i] = True
        clock = self.contorni(i, clock, pre)

        neigbours = adj[i]
        for j in neigbours:
            if visit[j] == False:
                clock = self.do_explore_reverse_one(j, adj, visit, pre, post, clock)

        clock = self.contorni(i, clock, post)
        return clock

    def contorni(self, i, clock, buf):
        buf[i] = clock
        clock = clock + 1
        return clock

    def do_explore_reverse_all(self, adj, pre, post):
        clock = 1
        visit = [False for _ in range(len(adj))]
        for i in range(len(adj)):
            if visit[i] == False:
                clock = self.do_explore_reverse_one(i, adj, visit, pre, post, clock)

    def explore_reverse(self, adj):
        pre = [0 for _ in range(len(adj))]
        post = [0 for _ in range(len(adj))]
        self.do_explore_reverse_all(adj, pre, post)
        return post

    def reverse_graph(self, adj):
        adj_rev = [[] for _ in range(len(adj))]
        for i in range(len(adj)):
            neighbours = adj[i]
            for n in neighbours:
                adj_rev[n].append(i)
        return adj_rev

    def acyclic(self, adj):
        #write your code here
        result = 0
        adj_rev = self.reverse_graph(adj)

        post = self.explore_reverse(adj_rev)
        post_clocks = [(v, clock) for (v, clock) in enumerate(post)]
        post_clocks_sorted = sorted(post_clocks, key = lambda p: p[1], reverse = True)
        vertices_sorted = [p[0] for p in post_clocks_sorted]

        components = self.explore(adj, vertices_sorted)
        comps_distinct = set(components)
        result = 1 if len(comps_distinct) < len(adj) else 0

        return result

    def explore(self, adj, vertices):
        components = [0 for _ in range(len(adj))]
        self.do_explore_all(adj, vertices, components)
        return components

    def do_explore_all(self, adj, vertices, components):
        visit = [False for _ in range(len(adj))]
        comp = 1
        for i in vertices:
            if visit[i] == False:
                self.do_explore_one(i, adj, components, visit, comp)
                comp = comp + 1

    def do_explore_one(self, i, adj, components, visit, comp):
        visit[i] = True
        components[i] = comp

        neigbours = adj[i]
        for j in neigbours:
            if visit[j] == False:
                self.do_explore_one(j, adj, components, visit, comp)

    ################# build an adjaency list from the input ######
    def load_input_from_file(self):
        f = open('./acyclicity.txt')
        return f.readlines()

    def load_input_from_stdin(self):
        'reads several lines of input and returns it as one string'

        # reading several lines of input
        # at the end of last line press enter
        # then press cmd+d (in Intellij) or ctrl+d (in shell)
        list_input = sys.stdin.readlines()
        return list_input

    def read_input(self):
        list_input = self.load_input_from_file()
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

        return adj

    def do(self):
        data_str = self.read_input()
        adj = self.make_adj_list(data_str)

        print(self.acyclic(adj))

if __name__ == '__main__':
    try:
        asi = Acyclicity()
        asi.do()
    except Exception, e:
        print e.message

