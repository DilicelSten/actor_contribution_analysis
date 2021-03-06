# coding=utf-8
"""
created on:2017/11/26
author:DilicelSten
target:判断贡献因子的相对重要性
finished on:2017/11/26
"""
import numpy as np
import numpy.linalg as nplg

# da = [[1,0.20,0.14,0.20,0.33,0.33,0.14,0.14,0.20],
# [5,1,0.14,0.14,3,1,0.20,3,3],
# [7,7,1,0.20,5,0.33,0.20,0.33,0.33],
# [5,7,5,1,0.14,5,0.33,1,0.33],
# [3,0.33,0.20,7,1,0.20,0.14,0.20,0.20],
# [3,1,3,0.20,5,1,0.14,0.33,0.33],
# [7,5,5,3,7,7,1,5,5],
# [7,0.33,3,1,5,3,0.20,1,0.33],
# [5,0.33,3,3,5,3,0.20,3,1]]
# da = [[1,0.11,0.11,0.14,0.14,0.2,0.33,1,0.33],
# [9,1,0.14,0.14,0.2,0.2,0.33,0.33,0.33],
# [9,7,1,5,3,5,3,3,3],
# [7,7,0.2,1,3,1,0.33,5,1],
# [7,5,0.2,0.33,1,3,3,5,3],
# [5,5,0.2,1,0.33,1,0.33,3,0.33],
# [3,3,0.33,3,0.33,3,1,5,3],
# [1,3,0.33,0,0.2,0.33,0.2,1,0.33],
# [3,3,0.33,1,3,3,0.33,3,1]]

da = [
[1,3,3,5,3,5,5],
[0.33,1,1,3,1,3,3],
[0.33,1,1,3,1,3,3],
[0.20,0.33,0.33,1,0.33,1,1],
[0.33,1,1,3,1,3,3],
[0.20,0.33,0.33,1,0.33,1,1],
[0.20,0.33,0.33,1,0.33,1,1]]
sum = np.sum(da, axis=0)
col_arv = da/sum
w = np.sum(col_arv, axis=1)
w_n = w/np.sum(w)
for i in w_n:
    print i
print np.max(nplg.eig(da)[0])