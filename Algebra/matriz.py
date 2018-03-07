from numpy import linalg,matrix
from sympy import Matrix
a = matrix('1 3 5 ; 2 3 1 ; -1 1 1')
g = linalg.det(a)
print g
