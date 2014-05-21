
import csv
import math
import numpy
#import matplotlib
#import matplotlib.pyplot as plt

class Point:
	def __init__(self, x, y, state):
		self._x = x
		self._y = y
		self._state = state # 0=Fix, 1=Saccade, 3=unknown
	def dist_to_point(self, other):
		# 'Compute the Euclidean distance between two Point objects'
		delta_x = self._x - other._x
		delta_y = self._y - other._y
		return (delta_x ** 2 + delta_y ** 2) ** 0.5
	def angle_with_point(self, previous):
		delta_x = self._x - previous._x
		delta_y = self._y - previous._y
		return math.degrees(math.atan2(delta_y,delta_x))

def avg(list):
	sum = 0
	for elm in list:
		sum += elm
	return sum/(len(list)*1.0)

def load_data():
	points = []
	info = csv.reader(open('../data/05.csv'), delimiter=',')  
	for row in info :
		points.append(Point(float(row[0]), float(row[1]), int(row[2]))) 
	return points

def extract_length(points):
	distances = []
	for i in range(1,len(points)):
		distances.append(points[i].dist_to_point(points[i-1]))
	print distances
	
def extract_angle(points):
	angles = []
	for i in range(1,len(points)):
		print points[i-1]._x, points[i-1]._y
		print points[i]._x, points[i]._y
		#TODO problem: it not moved...
		#if (row[2] == "1"): #saccade
		angles.append(points[i].angle_with_point(points[i-1]))
		print angles[-1]
	#TODO mirror
	#TODO group into 3 groups
	return angles

def get_average_transition(points):
	transition_prob = numpy.zeros(shape=(2,2))
	for i in range(1,len(points)):
		#print i
		#print points[i]._x, points[i]._y, points[i]._state, type(points[i]._state)
		if points[i-1]._state == 3 or points[i]._state == 3: continue
		transition_prob[points[i-1]._state, points[i]._state] += 1
	return transition_prob

def get_average_lengths(points):
	avg_length = numpy.zeros(shape=(2,2))
	lists_of_lengths = [[   [],[]   ],[   [],[]   ]] # 2x2 matrix where each field contains a list with lengths that occured
	for i in range(1,len(points)):
		if points[i-1]._state == 3 or points[i]._state == 3: continue
		(lists_of_lengths[points[i-1]._state][points[i]._state]).append(points[i-1].dist_to_point(points[i]))
	for i in range(2):
		for j in range(2):
			avg_length[i,j] = avg(lists_of_lengths[i][j])
	return avg_length

def get_average_run_length(points):
	run_lengths = []
	current_state = points[0]._state #fixation
	current_run_length = 0
	for i in range(1,len(points)):
		if points[i]._state == 3: continue
		if current_state == points[i]._state:
			current_run_length += 1
		else:
			run_lengths.append(current_run_length)
			current_run_length = 0
			current_state = points[i]._state
	print run_lengths
	return avg(run_lengths)

### example usage ###
points  = load_data()

print "get_average_lengths: "
print get_average_lengths(points) 
print "get_average_transition: "
print get_average_transition(points)
print "get_average_run_length: "
print get_average_run_length(points)








#TODO: data structure where multiple features are stored


	# calculate histogram and show it
#	hist = numpy.histogram(distances, bins=[30,90,150])
#	plt.bar(center, hist, align='center', width=width)
#	plt.show()
