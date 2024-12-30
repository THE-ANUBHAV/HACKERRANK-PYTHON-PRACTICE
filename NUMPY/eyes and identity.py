import numpy as np
n,m = map(int,input().split())
np.set_printoptions(legacy='1.13')
print(np.eye(n,m, k = 0))
