from sys import exit

def gold_room():
	print "This room is full of gold, How much do you want"

	next = raw_input(">")

	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type a number")

	if how_much < 50:
		print "Nice,you're not greedy, you win!"
		exit(0)

	else:
		dead("You greedy bastard!")


def bear_room():
	print "There is a bear here"
	print "How are you going to move the bear?"

	bear_moved = False

	while True:
		next = raw_input(">")

		if next == "take honey":
			dead("The bear looks at you then slaps your face")

		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door, you can "
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed")

		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea"

def cthulhu_room():
	print "Here"
	print "He"
	print "Do you flee for your life"

	next = raw_input(">")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty")
	else:
		cthulhu_room()


def dead(why):
	print why,"GOOD JOB"
	exit(0)

def start():
	print "you are"
	print "There is a door"
	print "which one do you take"

	next = raw_input("?")

	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("YOu")

start()

		
	