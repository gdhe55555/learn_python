cities = {
	'CA':'San Francisco', 'MI':'Detroit', 'FL':'Jcksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
	if state in themap:
		return themap[state]
	else:
		return "Not fount."

#ok pay attention

cities ['_find'] = find_city

while True:
	print "state?(ENTER TO quit)"

	state = raw_input(">")

	if not state: break

	city_found = cities['_find'](cities, state)

	print city_found


