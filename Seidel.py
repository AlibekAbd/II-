import numpy as np
import random

n = int(input())
A = np.random.rand(n,n)
f = np.random.rand(n)

#diagonal dimension
for i in range(0,n):
	summa = 0
	for j in range(0,n):
		summa += abs(A[i][j])
	c = random.uniform(1,2)
	A[i][i] = summa + c
	
def Seidel(A,f,x,n):
	xnew = [0] * n
	for i in range(n):
		s = 0
		for i in range(i-1):
			s =np.sum(A[i][j] * xnew[j])
		for j in range(i+1,n):
			s = np.sum(A[i][j] * x[j])
		xnew[i] = (f[i] - s)/ A[i][i]
	return xnew

def solve(A, f, n, eps):
	x = np.random.rand(n)
	xnew = [0] * n
	while norma(x,xnew,n) > eps:
		x = xnew
		xnew = Seidel(A,f,x,n)
	return xnew

def norma(a, b, N):
    s= 0
    for i in range(N):
        s +=  np.square((a[i] - b[i]))
    s += np.sqrt(s)
    return s
x = solve(A, f, n, 0.0009)
print(x)
	
		
		
