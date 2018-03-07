from numpy import matrix,linalg
a = matrix('2 1 1 ; 1 2 1 ; 1 1 2')
b = matrix('1; 2; 3')
u = linalg.solve(a,b)
print u
