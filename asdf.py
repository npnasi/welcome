#n = int(sys.stdin.readline())
#n,m = map(int, sys.stdin.readline().split())
#command = list(map(int, input().split()))  #int
#command = sys.stdin.readline().rstrip()     #str

import sys
n = int(sys.stdin.readline())
nums = [0,1,1,1,1,1,1,1,1,1]

for i in range(n-1):
    temp = [0]*10
    temp[0] = nums[1]
    temp[9] = nums[8]
    
    for j in range(1,9):
        temp[j] = nums[j-1]+nums[j+1]
    
    nums = temp

print(sum(nums)%1000000000)

