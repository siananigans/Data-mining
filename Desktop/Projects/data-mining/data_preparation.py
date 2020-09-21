import pandas
import matplotlib.pyplot


def drop_location_nulls(data):

	# drop null values from data

	newdata = data.dropna(how='any', subset=['GeoLocation'])

	return(newdata)

def drop_unused_attributes(data):

	# drop attributes we don't need

	del_attributes = ['nametype', 'name', 'id', 'GeoLocation', 'fall']

	data = data.drop(columns = del_attributes)


	return(data)


#def prepare_location_class(data):

	# prepare locadtion 

#for location in Geolocation:

#		tupl = location
#		newtupl = tupl.split(',')
#
#		lat = newtupl[0][1:]
#		lon = newtupl[1][0:-1]




	return(data)

def binary_fall(data):

	# Make fall a binary variable.


	fall = data['fall']

	newFall = []

	for entry in fall:

		if entry == 'Fell':
			newFall.append(1)
		else:
			newFall.append(0)

	data['newFall'] = newFall

	return(data)






def main():

	data = pandas.read_csv('meteorite-landings.csv')

	#Del Null
	no_null = drop_location_nulls(data)


	# Del useless attributes
	fall_update = binary_fall(no_null)

	# Del unused attributes
	final_attributes = drop_unused_attributes(fall_update)

	return(final_attributes)


if __name__ == '__main__':
	main()