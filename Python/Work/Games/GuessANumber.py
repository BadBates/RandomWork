import random
Y = True
while Y:
	x = range(0,1000)
	i = random.choice(x)
	chanes = 0
	level = input("Select difficulty(Easy/Normal/Hard/Insane): ")
	
	if level == "Easy": 
		chances = 20
	elif level == "Normal":
		chances = 10
	elif level == "Hard": 
		chances = 5
	else : chances = 1
	
	while chances >= 1:
		print(f"Tries Left {chances}")
		guess = int(input("Next Guess? :"))
	
		if i > guess:
			print("Number is higher than", guess)
			chances -=1
		
		elif i < guess:
			print("Number is lower than", guess)
			chances -=1
		
		elif i == guess:
			print("Number is ", guess," great job!!!")
			chances = 0
	if i != guess:
		print (f"no guess' left. Good Try. But the answer was {i}")


	Y = input("Wanna play number finder? (Yes/No)")
	if Y == "No":
		Y = False