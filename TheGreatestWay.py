#!/usr/bin/env python3


def find_the_greatest_way(filename):
    f = open(filename, 'r', encoding='utf-8')
    n = 0
    pred = {}
    c = {}
    target = []
    count = 0
    for line in f:
        if count == 0:
            n = int(line)
        elif count <= n:
            arr = line[:-2].split()
            vertices = []
            k = 1
            previous = 0
            for el in arr:
                if (k % 2) == 1:
                    vertices.append(int(el))
                    previous = el
                else:
                    c[(int(previous), count)] = int(el)
                k += 1
            pred[count] = vertices
        else:
            target.append(int(line))
        count += 1
    f.close()
    s = target[0]
    t = target[1]
    d = {}
    parents = {}
    for v in range(1, n + 1):
        if v != s:
            if s in pred[v]:
                d[v] = c[(s, v)]
            else:
                d[v] = float('-inf')
            parents[v] = s
    for k in range(2, n):
        for v in range(1, n + 1):
            if v != s:
                for w in pred[v]:
                    if w != s and w != v:
                        if d[w] + c[(w, v)] > d[v]:
                            d[v] = d[w] + c[(w, v)]
                            parents[v] = w
    f = open('out.txt', 'w', encoding='utf-8')
    if d[t] == float('-inf'):
        f.write('N')
    else:
        f.write('Y\n')
        way = []
        u = parents[t]
        while u != s:
            way.append(str(u))
            u = parents[u]
        way.append(str(s))
        way.reverse()
        way.append(str(t))
        f.write((' '.join(way)) + '\n')
        f.write(str(d[t]))
    f.close()


if __name__ == '__main__':
    find_the_greatest_way('in.txt')
