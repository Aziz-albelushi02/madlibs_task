





def main():
	# write your code here
		time = input("enter a number from 1 to 12? ")
		print(time)
		items = input("what were the items? ")
		print(items)
		name = input('who was the person? ')
		print(name)
		sentance = input("what was the sentance? ")
		print(sentance)
		verb = input("what did he do with his head?")
		print(verb)


		story = f''' It was {time} when I heard a knock at the door.
		I opened the door and there was a box full of {items} with a note saying "From {name}"
		Just as I closed the door I heard a scream "{sentance}"
		I froze in place and all I could do was {verb}.'''
		
		print(story)


if __name__ == '__main__':
    main()
