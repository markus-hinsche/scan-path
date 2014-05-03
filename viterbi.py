from numpy import matrix
from numpy import linalg
from numpy import zeros

import math
import random

import feature_extraction



def fill_probability_matrix_randomly(mat):
	(rows, cols) = mat.shape
	for j in range(rows): # for each row
		for i in range(cols): 
			mat[j,i] = random.random()
		rowSum = mat.sum(axis=1)[j]
		# each row should sum to 1.0
		for i in range(cols):
			mat[j,i] /= rowSum



feature_extraction.extract_angle()
Y = [0,0,1,0,0,0,1,1,0,0] # observations (should be 0...k) for B's indexing to work

### dimensions ###
N = 3
n = len(Y)
k = 2


### data types declaration ###
A  = zeros(shape=(k,k)) # state transition matrix
B  = zeros(shape=(k,n)) # emission matrix
T1 = zeros(shape=(k,n)) 
T2 = zeros(shape=(k,n))
PI = zeros(shape=(1,k)) # prior probability


### random initialization ###
fill_probability_matrix_randomly(A)
print A
fill_probability_matrix_randomly(B)
print B
fill_probability_matrix_randomly(PI)
print PI

for i in range(k):
	T1[i,0] = math.log(PI[0,i] * B[i,Y[0]]) #how to initialize PI and B?
	T2[i,0] = 0
for i in range(1,n): #For i = 2 ... n do
	for j in range(k): # For each s_j do
		
		maximum_candidates = []
		for l in range(k):
			#print "l: " + str(l) #debugging
			maximum_candidates.append(T1[l,i-1] + math.log(A[l,j]*B[j,Y[i]]))
		#print maximum_candidates
		T1[j,i] = max(maximum_candidates)
		T2[j,i] = max(enumerate(maximum_candidates),key=lambda x: x[1])[0]
		#print T1[j,i]
		#print T2[j,i]
		#print "\n"

print T2
