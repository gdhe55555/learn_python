ten_things = "Apples Oranges Crows Telephone Light"

print "Wait there's not 10 things in that list"

stuff = ten_things.split(' ')

more_stuff = ['Day', 'Night', 'SOng', 'Frisbee', 'n']

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print"Adding :", next_one
	stuff.append (next_one)
	print "There's %d items now." % len(stuff)

print "There we go:" ,stuff

print  "Let's do some things with stuff"

print stuff[1]

print stuff[-1]

print stuff.pop()
print ''.join(stuff)
print '#'.join(stuff[3:5])


