from Edge import Edge


class DenseGraph:
    def __init__(self, n, directed=False):
        self.n = n  # number of vertex
        self.m = 0  # number of edge
        self.directed = directed
        self.martix = [[None for i in range(n)] for i in range(n)]

    def __str__(self):
        for line in self.martix:
            for ele in line:
                if isinstance(ele, Edge):
                    print(str(ele.wt()) + '   ', end='')
                else:
                    print('NULL   ', end='')
            print('')
        return ''  # __str__必须要返回字符串，否则报错。。。

    def V(self):
        return self.n

    def E(self):
        return self.m

    def addEdge(self, v, w, weight):
        if 0 <= v < self.n and 0 <= w < self.n:
            if self.hasEdge(v, w):
                return
            self.martix[v][w] = Edge(v, w, weight)
            if v != w and self.directed is False:
                self.martix[w][v] = Edge(v, w, weight)
            self.m += 1
        else:
            raise Exception('Vertex not in the graph')

    def hasEdge(self, v, w):
        if 0 <= v < self.n and 0 <= w < self.n:
            return self.martix[v][w] is not None
        else:
            raise Exception('Vertex not in the graph')

    def __iter__(self):
        return iter(range(self.m))

    def __getitem__(self, item):
        listP = []
        for index, ele in enumerate(self.martix[item]):
            if not isinstance(ele, Edge) and ele != 0:
                listP.append(index)
        return iter(listP)
