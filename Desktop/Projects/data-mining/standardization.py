import pandas
import matplotlib.pyplot
import new_data_prep as dp

"""
Call the z_score() function with a dataset attribute value and a index.

"""

mads = []
means = []


def find_mads(data):
	# Calculate Mean absolute deviation.

	mads.append(data.mad(axis = 0, skipna = True).tolist())


def find_means(data):
	#Calculate mean.

	means.append(data.mean(axis = 0, skipna = True).tolist())


#def categorical_value():



def z_score(point, column):
	#Calculate the z-score for a point given.

	#print(data)

	mad = mads[0][column]
	mean = means[0][column]
	#print("Test", mads)
	z = (point - mean)/mad
	return(z)
	#print(z)
	
def column_standardize(data):

	#Standardize the columns for distance
	find_mads(data)
	find_means(data)
	print(means, mads)


def main():

	z_score(3, 1)

if __name__ == '__main__':
	main()