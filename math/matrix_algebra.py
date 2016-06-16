# Matrix Algebra


from numpy import matrix, array, vdot, linalg
A = matrix([[1, 2, 3], [2, 7, 4]])
B = matrix([[1, -1], [0,1]])
C = matrix([[5, -1], [9, 1], [6, 0]])
D = matrix([[3, -2, -1], [1, 2, 3]])
u = array([6, 2, -3, 5])
v = array([3, 5, -1, 4])
w = matrix([[1], [8], [0], [5]])
alpha = 6

# Part 1
'''
1.1) 2x3
1.2) 2x2
1.3) 3x2
1.4) 2x3
1.5) 1x4
1.6) 4x1
'''
for m in [A, B, C, u, v, w]:
	print(m.shape)

# Part 2
'''
2.1) [ 9  7 -4  9]
2.2) [ 3 -3 -2  1]
2.3) [ 36  12 -18  30]
2.4) 51
2.5) sqrt(74) = 8.60232526704
'''
print(u + v)
print(u - v)
print(alpha * u)
print(vdot(u, v))
print(linalg.norm(u))

# Part 3
'''
3.1) ND
3.2)
[[-4 -7 -3]
 [ 3  6  4]]
3.3)
[[14  3  3]
 [ 2  7  9]]
3.4)
[[-1 -5 -1]
 [ 2  7  4]]
3.5) ND
3.6) ND
3.7)
[[ 5 -6]
 [ 9 -8]
 [ 6 -6]]
3.8)
[[ 1 -4]
 [ 0  1]]
3.9)
[[14 28]
 [28 69]]
3.10)
[[10 -4  0]
 [-4  8  8]
 [ 0  8 10]]
'''
try:
	print(A + C)
except:
	print('undefined')
print(A - C.T)
print(C.T + 3 * D)
print(B * A),
try:
	print(B * A.T)
except:
	print('undefined')
try:
	print(B * C)
except:
	print('undefined')
print(C * B)
print(B * B * B * B)
print(A * A.T)
print(D.T * D)