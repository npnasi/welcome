#n = int(sys.stdin.readline())
#n,m = map(int, sys.stdin.readline().split())
#command = list(map(int, input().split()))  #int
#command = sys.stdin.readline().rstrip()     #str

import sys
TRY = int(sys.stdin.readline())

for T in range(TRY):
    N = int(sys.stdin.readline())
    table = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]

    if N>1:
        table[0][1] += table[1][0]
        table[1][1] += table[0][0]
    for n in range(2,N):
        table[0][n] += max(table[1][n-1],table[1][n-2])
        table[1][n] += max(table[0][n-1],table[0][n-2])
    
    print(max(table[0][-1],table[1][-1]))