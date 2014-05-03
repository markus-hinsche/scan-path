
import csv
import math
import numpy
#import matplotlib
#import matplotlib.pyplot as plt

class Point:
	def __init__(self, x, y):
		self._x = x
		self._y = y
	def dist_to_point(self, other):
		# 'Compute the Euclidean distance between two Point objects'
		delta_x = self._x - other._x
		delta_y = self._y - other._y
		return (delta_x ** 2 + delta_y ** 2) ** 0.5


def load_data():
	points = []
	info = csv.reader(open('../data/05.csv'), delimiter=',')  
	for row in info :
		if (row[2] == "1"): #saccade
			points.append(Point(float(row[0]), float(row[1]))) #row[2] not taken into consideration
	return points

def extract_angle():
	points = load_data()
	distances = []
	for i in range(1,len(points)):
		distances.append(points[i].dist_to_point(points[i-1]))

	print distances
	
	# calculate histogram and show it
#	hist = numpy.histogram(distances, bins=[30,90,150])
#	plt.bar(center, hist, align='center', width=width)
#	plt.show()
