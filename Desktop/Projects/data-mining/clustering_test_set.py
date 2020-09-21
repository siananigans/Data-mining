import pandas
import matplotlib.pyplot
import data_prep_no_mass as dp
import standardization as stnd
import random
import math


"""
Call with main().

Clusters meteor dataset.

get all d_i = point - mean_point

get mean_distance_from_mean

"""

clusters = []
old_clusters = []
iterations = 0

def euclidean_distance(centroid, entry):

	# Compute distance between two points.
	sums = []
	# append categorical distance to sums i.e fall, class
	reclass = compare_categorical(entry[0], centroid[0])
	fall = compare_categorical(entry[1], centroid[1])

	sums.append(reclass)
	sums.append(fall)

	i = 2
	while i < len(entry):

		# Get z score of the object at attribute i and centroid at attribute i.

		entry_z = stnd.z_score(float(entry[i]), i-2)
		centroid_z = stnd.z_score(float(centroid[i]), i-2)

		# Euclidean distance (x-y)^2
		tmp = (entry_z-centroid_z)**2
		# Append to sums list
		sums.append(tmp)

		# Increment
		i+=1

	total = 0

	# Total sums list for Euclidean distance
	for s in sums:
		total = total + s

	if total < 0:
		total = total*-1
	# Get square root of total as last part of formula
	euclidean = math.sqrt(total)



	return(euclidean)


def re_evaluate_centroid():

	#Find mean of new clusters
	
	newCentroids = []

	#print(len(clusters))
	for cluster in clusters:
		if len(cluster) != 0:
			 
			i = 0 # Attribute
			
			obj = cluster[i]
			centroid = []

			while i < len(obj):
				total = 0
				j = 0 # Object

				new_list = []
				while j < len(cluster):
					if i < 2:
						new_list.append(cluster[j][i])
						j+=1
					else:
						total = total + cluster[j][i]
						j +=1
				if i < 2:
					mean =  most_frequent(new_list)
				else:
					mean = total/(len(cluster))

				centroid.append(mean)

				i +=1

			newCentroids.append(centroid)
	return(newCentroids)

def most_frequent(List): 
    return max(set(List), key = List.count)

def compare_categorical(a, b):

	if a == b:
		return(0)

	else:
		return(1)



def put_in_cluster(centroids, entry):
	# Put entry into a cluster.
	d = []
	#print(len(clusters))
	#print(centroids)
	for centroid in centroids:
		# Find distance of point from centroid & append to the d list.
		#print(entry)
		d.append(euclidean_distance(centroid, entry))
	# m = min

	m = d[0]
	j = 0
	i = 0
	while i < len(d):
		# Find smallest distance location.
		if d[i] < m:
			# If distance at i is smaller than old min, min = distance[i].
			m = d[i]
			# Set j to be the cluster.
			j = i
		i+=1

	# Append entry to the appropriate cluster
	clusters[j].append(entry) #Global var



def cluster():
	#Get dataset
	
	dataset = dp.main()


	#Define number for k, lets say 4.
	k = 5
	stnd.column_standardize(dataset)
	#Find k values and use as center of clusters.
	#centroids = [dataset.iloc[random.randrange(0,7622,1)].tolist() for c in range(k)]

	centroids = [['L6', 'Fell', 1847.3822937625755, 30.723573515090525, -6.250401301810863], ['L6', 'Found', 2002.740698120445, 11.853286020233957, 7.56736650163024], ['L6', 'Found', 1993.7038371313672, -77.48196589209265, 146.32998204222278], ['H4', 'Found', 1983.3907108112348, -71.16395223081743, 14.32200271724516], ['L6', 'Found', 1937.0619539316917, 27.4433247561557, -31.123312524225565]]
	
	for centroid in centroids:
		clusters.append([])



	split_entries(centroids, dataset)

	objective = objective_function(centroids)


	lengths = lengths_func()
	print("Writing to file.")

	with open('./results.txt', mode='a') as results:
		results.write("\n--------------------------------------------------------")
		results.write("\nResults for Classifying Test-Set where k = " + str(k)+" .And centroids are predetermined\n")
		results.write("----------------------------------------------------------\n")
		results.write("\nCentroids = " + str(centroids) + "\n")
		results.write("\nLength of each centroid: " + lengths + "\n")
		results.write("\nObjective = " + str(objective) + "\n")
		results.write("\nNumber of iterations before fully clustered = " + str(iterations))

	print("Process complete.")

def split_entries(centroids, data):

	i = 0
	#print(centroids)
	while i < len(data):
		#print("Number of entries clustered: ", i)
		#print('IN')

		#print(data.iloc[i].tolist())
		put_in_cluster(centroids, data.iloc[i].tolist())
		i+=1

	
	return()


def objective_function(centroids):
	print("Calculating objective function.")
	total = 0
	i = 0

	while i < len(clusters):
		for entry in clusters[i]:
			total = total + (euclidean_distance(centroids[i], entry))**2
		i+=1

	return(total)


def lengths_func():
	cluster_lengths = ""
	i = 0
	while i < len(clusters):
		cluster_lengths = cluster_lengths + "\nCluster " + str(i+1) + " = " + str(len(clusters[i]))
		i+=1
		
	return(cluster_lengths)

def main():

	result = cluster()


if __name__ == '__main__':
	main()


