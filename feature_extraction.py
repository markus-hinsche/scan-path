
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

def load_data():
	points = []
	info = csv.reader(open('../data/05.csv'), delimiter=',')  
	for row in info :
		points.append(Point(float(row[0]), float(row[1]), int(row[2]))) 
	return points

def extract_length():
	points = load_data()
	distances = []
	for i in range(1,len(points)):
		distances.append(points[i].dist_to_point(points[i-1]))
	print distances
	
def extract_angle():
	points = load_data()
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

def get_average_transition():
	points = load_data()
	transition_prob = numpy.zeros(shape=(2,2))
	for i in range(1,len(points)):
		if points[i-1]==3 or points[i]==3:
			continue
		transition_prob[points[i-1]._state, points[i]._state] += 1
	return transition_prob
		#points[i-1]._state

print get_average_transition()


#TODO: data structure where multiple features are stored


	# calculate histogram and show it
#	hist = numpy.histogram(distances, bins=[30,90,150])
#	plt.bar(center, hist, align='center', width=width)
#	plt.show()
