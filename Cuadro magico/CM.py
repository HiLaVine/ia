import heapq
import itertools

def magic_sum(n):
    return n*(n**2 + 1)//2

def heuristic(perm, magicSum):
    square = [perm[n:n+3] for n in range(0, len(perm), 3)]
    sums = [sum(row) for row in square] + [sum(col) for col in zip(*square)] + [sum(square[i][i] for i in range(3))] + [sum(square[i][2-i] for i in range(3))]
    return sum(abs(s - magicSum) for s in sums)

def best_first_search():
    magicSum = magic_sum(3)
    perms = list(itertools.permutations(range(1, 10)))
    heapq.heapify(perms)
    while perms:
        perm = heapq.heappop(perms)
        if heuristic(perm, magicSum) == 0:
            return [perm[n:n+3] for n in range(0, len(perm), 3)]

magicSquare = best_first_search()
for row in magicSquare:
    print(row)