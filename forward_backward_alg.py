

from numpy import matrix
from numpy import linalg
from numpy import zeros
import numpy

import math
import random



def normalize_matrix(mat):
	(rows, cols) = mat.shape
	for i in range(rows): # for each row
		tmp_sum = sum((mat[i,j]) for j in range(N))
		for j in range(cols): 
			mat[i,j] /= tmp_sum
		

def backward_forward(A,B,PI,Y):
	### forward ###
	alpha = zeros(shape=(numStates,n))

	# define first column (t=0)
	for i in range(numStates):
		alpha[i, 0] = PI[0,i] * B[i, 0]
	# define other columns
	for j in range(numStates):
		for t in range(0,n-1):
			alpha[j, t+1] = B[j,Y[t+1]] * sum((alpha[i,t] * A[i,j]) for i in range(N))
			pass
	#print "alpha: "
	#print alpha

	### backward ###
	beta  = zeros(shape=(numStates,n))
	for i in range(numStates):
		beta[i, n-1] = 1.0
	for t in range(n-2,-1, -1):
		for i in range(numStates):
			beta[i,t] = sum((beta[j, t+1] * A[i,j] * B[j, Y[t+1]]) for j in range(N))
	#print "beta: "
	#print beta


	#Update
	gamma = zeros(shape=(numStates,n))
	for i in range(numStates):
		for t in range(n):
			gamma[i,t] = alpha[i,t] * beta[i,t] / sum((alpha[j,t] * beta[j,t]) for j in range(N))
	#print "gamma: "
	#print gamma

	ksi = zeros(shape=(numStates,numStates,n-1))
	for i in range(numStates):
		for j in range(numStates):
			for t in range(n-1):
				ksi[i,j,t] = alpha[i,t] * A[i,j] * beta[j, t+1] * B[j,Y[t+1]] / sum((alpha[k,t] * beta[k,t]) for k in range(N))
	#print "ksi: "
	#print ksi

	# PI update
	for i in range(numStates):
		PI[0,i] = gamma[i,0]
	#print "PI: "
	#print PI
	#print "PI check: "
	assert( sum((PI[0,i]) for i in range(numStates)) )


	# A update
	for i in range(numStates):
		for j in range(numStates):
			A[i,j] = sum((ksi[i,j,t]) for t in range(n-1)) / sum((gamma[i,t]) for t in range(n-1))
	#print "A: "
	#print A
	#print "A check: "
	for i in range(numStates):
		assert( sum ((A[i,j]) for j in range(numStates)) )


	# B update
	for i in range(numStates):
		for k in range(N):
			B[i,k] = sum(((1. if Y[t]==Y[k] else 0.) * gamma[i,t]) for t in range(n)) / sum((gamma[i,t]) for t in range(n))
			# what is v[k]?? -> I took Y[k] now
	#print "B: "
	#print B
	#print "B check: "
	normalize_matrix(B)
	for i in range(numStates):
		assert( sum((B[i,j]) for j in range(N)) )
	return (A,B,PI)
	

No=0
Egg=1
Y = [No,No,No,No,No,Egg,Egg,No,No,No]

### dimensions ###
N = 2 #observation space
n = len(Y) #observations
numStates = 2 #states -> TODO rename numStates


### data types declaration ###
A  = matrix([[0.5, 0.5], [0.3, 0.7]]) # state transition matrix
B  = matrix([[0.3, 0.7], [0.8, 0.2]]) # emission matrix
PI = matrix([[0.2,0.8]]) # prior probability

for iteration in range(10):
	print PI
	(A,B,PI) = backward_forward(A,B,PI,Y)
	

# TODO B update weird
# TODO too fast convergence