from api import *
from houseprint import *

class Artifact:
	def __init__(self, name):
		self.name = name
		self.description = getArtifactDesc(name)
		self.question = None
		# self.easyQuestion = None
		# self.hardQuestion = None
		self.solved = False

	def setQuestion(self, question):
		self.question = question

	def getDescription(self):
		return self.description

	# def setEasyQuestion(self, easier):
	# 	self.easyQuestion = easier


	# def setHardQuestion(self, harder):
	# 	self.hardQuestion = harder
		
class Room:
	def __init__(self, name, num_artifacts):
		self.artifacts = []
		self.name = name
		self.roomDesc, self.objects = getRoomDesc(name, num_artifacts)
		for artifact in self.objects:
			temp = Artifact(artifact)
			self.artifacts.append(temp)
		self.num_artifacts = num_artifacts
		self.num_solved = 0
		self.completed = False

	# Describes each room and the objects in it
	def describeRoom(self):
		print(self.roomDesc)

	# Lists the objects in the room
	def listPOI(self):
		count = 0
		for artifact in self.artifacts:
			if count == self.num_artifacts:
				break
			if artifact.solved == False:
				print(artifact.name)
				count += 1
		if self.completed == True:
			print("You have completed this room")
	def describeArtifact(self, artifact):
		print(artifact.getDescription())

	def runRoom(self):
		self.describeRoom()
		while self.completed == False:
			self.listPOI()
			x = input("Which artifact would you like to inspect (Please enter the exact name as listed above)? Enter /'exit/' to leave the room: ")
			if x == "exit":
				break
			for artifact in self.artifacts:
				if artifact.name == x:
					self.describeArtifact(artifact)
					if print(giveQuestion(artifact.easyQuestion())) == True:
						artifact.solved = True
						self.num_solved += 1
						if self.num_solved == self.num_artifacts:
							self.completed = True
				break

def getQuestion():
	# ai stuff here
	pass

class House:
	def __init__(self, difficulty):
		self.difficulty = difficulty
		# self.bedroom = Room("Bedroom", 1)
		self.office = Room("Office", 2)
		# self.bathroom1 = Room("Master Bathroom", 1)
		# self.garage = Room("Garage", 1)
		self.foyer = Room("Foyer", 1)
		self.livingRoom = Room("Living Room", 1)
		# self.kitchen = Room("Kitchen", 1)
		# self.diningRoom = Room("Dining Room", 1)
		# self.gameRoom = Room("Game Room", 1)
		# self.bathroom2 = Room("Bathroom", 1)
		self.basement = Room("Basement", 1)
		# self.laundry = Room("Laundry", 1)
		# self.closet = Room("Closet", 1)
		# self.attic = Room("Attic", 4)
		# self.rooms = [self.foyer, self.bedroom, self.office, self.bathroom1, self.garage, self.livingRoom, self.kitchen, self.diningRoom, self.gameRoom, self.bathroom2, self.basement, self.laundry, self.closet, self.attic]
		self.rooms = [self.foyer, self.livingRoom, self.office, self.basement]
		questionTemps = getQuestions(user_input, self.difficulty, age)
		#questionTemps = [('1. What is gum usually made from?\n   A. Potato\n   B. Plastic \n   C. Resin \n   D. Wood', 'C'), ('2. What is the traditional flavor of chewing gum?\n   A. Mint \n   B. Blueberry \n   C. Bubblegum\n   D. Cherry', 'A'), ('3. What common substance is often added to gum to help it stay soft?\n   A. Paint\n   B. Glycerin \n   C. Salt \n   D. Cornstarch', 'B'), ('4. In which year was the first commercial chewing gum produced?\n   A. 1912\n   B. 1763\n   C. 1850\n   D. 1869', 'D'), ('5. What is the act of blowing bubbles with gum called?\n   A. Popping \n   B. Gum Blowing \n   C. Bubble Blowing \n   D. Blobbing', 'C'), ("6. Which company produces the Wrigley's brand of gum?\n   A. Nestle\n   B. Mars, Inc.\n   C. McCormick & Company\n   D. Kraft Foods", 'B'), ('7. In which country did humans start chewing gum?\n    A. Greece\n    B. China\n    C. India\n    D. United States', 'A'), ('8. What is the world record for the largest gum bubble blown?\n    A. 6 inches\n    B. 20 inches \n    C. 15 inches \n    D. 23 inches', 'D'), ('9. What popular gum brand is known for its triangular prism shape?\n    A. Dentyne\n    B. Trident \n    C. Juicy Fruit \n    D. Eclipse', 'B'), ('10. Chewing gum can help to increase concentration and reduce what?\n    A. Weight\n    B. Stress\n    C. Hunger\n    D. Blood pressure', 'B'), ('11. Which popular chewing gum brand was the first to introduce sugar-free gum?\n    A. Juicy Fruit\n    B. Trident \n    C. Eclipse\n    D. Orbit', 'B'), ('12. Which war sparked the first major increase in chewing gum sales in the U.S.?\n    A. World War I \n    B. World War II \n    C. Civil War \n    D. Vietnam War', 'B'), ('13. Which sugar substitute is most commonly used in sugar-free chewing gum?\n    A. Saccharine\n    B. Stevia \n    C. Xylitol \n    D. Aspartame', 'C'), ('14. The name of which popular gum came from the slang term for a polite request?\n    A. Orbit\n    B. Eclipse\n    C. Trident\n    D. Juicy Fruit', 'A'), ('15. Which chewing gum brand released a famous ad featuring a smiling girl and the slogan, “A minty pick up for 5 cents”?\n    A. Wrigley’s Spearmint \n    B. Trident \n    C. Dentyne \n    D. Chiclets', 'A'), ('16. What is a primary reason chewing gum is not allowed in many schools?\n    A. It is a distraction.\n    B. It makes noise.\n    C. It is bad for teeth. \n    D. It is expensive.', 'A'), ('17. Bubble gum is usually what color?\n    A. Green\n    B. Yellow \n    C. Blue\n    D. Pink', 'D'), ('18. What happens to gum when it is exposed to extremely cold temperatures?\n    A. It becomes softer.\n    B. It becomes brittle. \n    C. It changes color. \n    D. It dissolves.', 'B'), ('19. What was the first tape gum created in 1988 by Wrigley’s?\n    A. Bubble Tape \n    B. Orbit \n    C. Big League Chew \n    D. Eclipse', 'A'), ('20. Which famous ancient civilization used to chew a gum-like substance extracted from trees?\n    A. The Greeks \n    B. The Egyptians \n    C. The Mayans \n    D. The Romans', 'C'), ("21. What does the term 'chewing the fat' mean?\n    A. Eating fast \n    B. Gaining weight \n    C. Having a casual conversation \n    D. Chewing a lot of gum", 'C'), ('22. What is the main flavor of Juicy Fruit gum?\n    A. Strawberry \n    B. Banana\n    C. Apple\n    D. None of the above', 'D'), ('23. In which decade was bubble gum first invented?\n    A. 1940s\n    B. 1920s \n    C. 1960s \n    D. 1980s', 'B'), ('24. Chewing gum after eating can help reduce what?\n    A. Calorie intake \n    B. Blood pressure \n    C. Acid reflux \n    D. Weight gain', 'C'), ('25. What brand of chewing gum was named after a popular game played in the 1800s?\n    A. Orbit \n    B. Trident\n    C. Big League Chew \n    D. Chiclets', 'C'), ('26. What gum brand uses the slogan, "Long lasting flavor"?\n    A. Orbit\n    B. Trident\n    C. Extra \n    D. Juicy Fruit', 'C'), ('27. Which famous figure said, "I hope we have once again reminded people that man is not free unless government is limited. There\'s a clear cause and effect here that is as neat and predictable as a law of physics: as government expands, liberty contracts."?\n    A. William Wrigley Jr.\n    B. Ronald Reagan\n    C. Barack Obama\n    D. Neil Armstrong', 'B'), ('28. Most chewing gum wrappers are made out of what material?\n    A. Plastic \n    B. Foil \n    C. Paper \n    D. Cotton', 'B'), ("29. Which gum brand's name is derived from ‘dental hygiene’?\n    A. Dentyne\n    B. Orbit\n    C. Trident \n    D. Chiclets", 'A'), ('30. What is the primary purpose of gum base in chewing gum?\n    A. To give flavor\n    B. To produce bubbles\n    C. To add color\n    D. To provide chewiness', 'D'), ('31. The ingredient xylitol used in chewing gum is sourced from what?\n    A. Corn \n    B. Sugar cane \n    C. Minced meat \n    D. Wheat', 'A'), ('32. How long does the flavor of the average chewing gum last?\n    A. 5 minutes\n    B. 15-25 minutes \n    C. 1 hour \n    D. The entire day', 'B'), ("33. What is the average stick of gum's calorie count?\n    A. 100 calories\n    B. 20 calories \n    C. 10 calories \n    D. 50 calories", 'C'), ('34. Who was the inventor of the bubble gum?\n    A. Walter Diemer\n    B. Thomas Adams \n    C. William Wrigley Jr. \n    D. Frank Henry Fleer', 'A'), ('35. Chewing gum commercial production started in which US state?\n    A. New York\n    B. Texas \n    C. Pennsylvania \n    D. Florida', 'A'), ('36. Which gum brand advertises with the slogan "Eat, Drink, Chew"?\n    A. Extra\n    B. Juicy Fruit\n    C. Orbit \n    D. Trident', 'A'), ("37. The world's first gum factory was established in which country?\n    A. UK\n    B. China \n    C. USA \n    D. Canada", 'C'), ('38. What does chewing gum traditionally symbolize in Turkey?\n    A. Declaration of love\n    B. Engagement \n    C. Fertility \n    D. Good luck', 'B'), ("39. Which company makes Big Red chewing gum?\n    A. Mars, Inc. \n    B. Cadbury \n    C. Wrigley's \n    D. Hershey's", 'C'), ('40. How many pieces of gum does the average American chew in a year?\n    A. Around 50 pieces\n    B. Around 200 pieces \n    C. Around 300 pieces \n    D. More than 500 pieces', 'C'), ('41. Who sang the song "Does Your Chewing Gum Lose Its Flavor on the Bedpost Overnight"?\n    A. Frank Sinatra \n    B. The Beatles \n    C. Lonnie Donegan \n    D. Elvis Presley', 'C'), ('42. What is the main ingredient of traditional Chios mastic gum?\n    A. Rubber latex \n    B. Chiclets \n    C. Mastic tree resin \n    D. Peppermint leaves', 'C'), ('43. What is the main disadvantage mentioned regarding sugar-free gum?\n    A. It makes you hungry \n    B. It can cause digestive problems \n    C. It leads to weight gain \n    D. It leads to dental decay', 'B'), ('44. What type of natural gum is harvested from the sap of acacia trees?\n    A. Gum arabic \n    B. Gum tragacanth \n    C. Xanthan gum \n    D. Guar gum', 'A'), ('45. Before modern gum, what substance was chewed by Native Americans?\n    A. Tree bark\n    B. Chicle\n    C. Gum resin \n    D. Spruce sap', 'D'), ('46. What is the name of the common polishing agent used in gum that is also found in toothpaste and car wax?\n    A. Carnauba wax \n    B. Beeswax \n    C. Paraffin wax \n    D. Candelilla wax', 'A'), ('47. What is the appropriate way to dispose of used chewing gum?\n    A. Throw it on the sidewalk\n    B. Swallow it \n    C. Wrap it in paper and put it in a trash bin \n    D. Stick it under a table', 'C'), ('48. Where is the headquarters of the Wrigley Company located?\n    A. London, UK\n    B. Chicago, USA \n    C. Toronto, Canada \n    D. Switzerland', 'B'), ('49. Who introduced the practice of including trading cards with gum in the package?\n    A. William Wrigley Jr.\n    B. Frank Fleer\n    C. John Curtis\n    D. Thomas Adams', 'D'), ('50. What is the largest number of sticks of gum ever chewed at once by a person?\n    A. 39 sticks\n    B. 97 sticks\n    C. 150 sticks\n    D. 542 sticks', 'B')]
		#print(len(questionTemps))
		i = 0
		for room in self.rooms:
			for artifact in room.artifacts:
				curQuestion = Question(questionTemps[i][0],questionTemps[i][1])
				artifact.setQuestion(curQuestion)
				i = i + 1
		#self.rooms = [Room("Bedroom", 2), Room("Office", 1), Room("Master Bathroom", 1), Room("Garage", 2), Room("Foyer", 1), Room("Living Room", 2), Room("Kitchen", 3), Room("Dining Room", 2), Room("Game Room", 3), Room("Bathroom", 1), Room("Basement", 3), Room("Laundry", 1), Room("Closet", 1), Room("Attic", 4)]
		# self.foyerConnection = [self.garage, self.diningRoom, self.livingRoom, self.bedroom]
		# self.bedroomConnection = [self.bathroom2, self.foyer, self.office]
		# self.bathroom2Connection = [self.bedroom]
		# self.officeConnection = [self.bedroom, self.attic]
		# self.atticConnection = [self.office]
		# self.garageConnection = [self.kitchen, self.foyer]
		# self.livingRoom = [self.foyer, self.diningRoom]
		# self.kitchenConnection = [self.closet, self.garage, self.diningRoom, self.gameRoom]
		# self.diningRoomConnection = [self.bathroom1, self.foyer, self.livingRoom, self.kitchen]
		# self.gameRoomConnection = [self.kitchen, self.bathroom1, self.laundry]
		# self.bathroom1Connection = [self.gameRoom, self.diningRoom]
		# self.laundryConnection = [self.gameRoom, self.basement]
		# self.basementConnection = [self.laundry]
		# self.roomConnections = [foyerConnection, bedroomConnection, officeConnection, bathroom1Connection, garageConnection, livingRoomConnection, kitchenConnection, diningRoomConnection, gameRoomConnection, bathroom2Connection, basementConnection, laundryConnection, closetConnection, atticConnection]
		
	def roomToInt(self):
		if self.name == "Foyer":
			return 0
		elif self.name == "Bedroom":
			return 1
		elif self.name == "Office":
			return 2
		elif self.name == "Master Bathroom":
			return 3
		elif self.name == "Garage":
			return 4
		elif self.name == "Living Room":
			return 5
		elif self.name == "Kitchen":
			return 6
		elif self.name == "Dining Room":
			return 7
		elif self.name == "Game Room":
			return 8
		elif self.name == "Bathroom":
			return 9
		elif self.name == "Basement":
			return 10
		elif self.name == "Laundry":
			return 11
		elif self.name == "Closet":
			return 12
		elif self.name == "Attic":
			return 13
		else:
			return -1
		

	#def setQuestions():
				# artifact.setEasyQuestion(questionTemps.pop())
				# artifact.setHardQuestion(questionTemps.pop())

		
		# easyQuestions = getQuestions(user_input, "easy", age)
		# hardQuestions = getQuestions(user_input, "hard", age)
		# i = 0
		# for room in self.rooms:
		# 	for artifact in room.artifacts:
		# 		curEasyQuestion = Question(easyQuestions[i][0],easyQuestions[i][1])
		# 		curHardQuestion = Question(hardQuestions[i][0],hardQuestions[i][1])
		# 		i = i + 1 
		# 		artifact.setEasyQuestion(curEasyQuestion)
		# 		artifact.setHardQuestion(curHardQuestion)

#	def __init__ adjacentRoomsAndStairs

class Question:
	def __init__(self, generated, corAns):
		self.generated = generated
		self.corAns = corAns
		self.isUsed = False
		self.answeredcorrectly = False
	def setUsed(self):
		self.isUsed = True
	def update(self):
		print(self.generated)
		self.setUsed()
		#print(self.corAns)
		user_input = input("What is your answer: ")
		result = self.checkAnswer(user_input, False)
		if result == -1:
			user_input = input("Try Again: ")
			return self.checkAnswer(user_input, True)
		elif result == 1:
			return True
		else:
			return False
		
	def checkAnswer(self, input, multiple):
		input = input.upper()
		if input == self.corAns:
			self.answeredcorrectly = True
			print("Good job! You answered correctly")
			return 1
		elif len(input) > 1 or (input != 'A' and input !='B' and input != 'C' and input != 'D'):
			if not multiple:
				print("Please use the correct format")
				return -1
			else:
				print("Incorrect. You have entered the incorrect format again. Please make sure to use the correct format in future questions")
				return 0
		else:
			self.answeredcorrectly = False
			print("You answered incorrectly")
			return 0
	# # def giveQuestion(self):
	# # 	print(self.generated)
	# # 	result = self.update()
	# # 	return result
		
def main():
	print("""Welcome to "The Enigma Residence," an immersive, interactive escape game.\n\n Upon receiving a cryptic phone call, you've been led to an unsettlingly quiet house. After entering, the front door slams shut behind you, locking you inside. Solve a diverse array of challenging riddles and answer riveting questions as you traverse into the depths of this peculiar abode. Each correct response earns you handy tools and insightful clues, indispensable in navigating a path to your escape.\n\nStrap yourself in for a roller coaster of emotion, decisiveness, patience, and intellectual agility. \nYour freedom is only a puzzle away.	\nCan you decipher the enigma of the house and regain your freedom? \nLet’s find out.""")
	global user_input
	num_wrong = 0
	user_input = input("What topic would you like: ")
	print("You entered: " + user_input)
	global age
	age = input("What is your age: ")
	difficulty = input("What difficulty would you like: ")
	printhouse()
	house = House(difficulty)
	# house.rooms[0].describeRoom()								
	# house.rooms[0].listPOI()
	#house.setQuestions()
	for i in range(len(house.rooms)):
		house.rooms[i].describeRoom()								
		house.rooms[i].listPOI()
		valid = False
		while (valid == False):
			x = input("Which artifact would you like to inspect (Please enter the exact name as listed above): ")
			for artifact in house.rooms[i].artifacts:
				if artifact.name == x:
					valid = True
					house.rooms[i].describeArtifact(artifact)
					done = False
					while (done == False ):
						if (artifact.question.update() == True):
							artifact.solved = True
							done = True
							house.rooms[i].num_solved += 1
							house.rooms[i].completed = True
							print("You have completed the " + house.rooms[i].name)
						else:
							num_wrong += 1
						if num_wrong == 2:
							print("You have answered two incorrect answers. You failed to escape the house. Better luck next time :)")
							exit(0)

	# for artifact in house.rooms[0].artifacts:
	# 	if artifact.name == x:
	# 		house.rooms[0].describeArtifact(artifact)
	# 		while (True):
	# 			if (artifact.question.update() == True):
	# 				artifact.solved = True
	# 				house.rooms[0].num_solved += 1
	# 				house.rooms[0].completed = True
	# 				break
	print("Congratulations! You have won the game!")
	# currentRoom = 0
	# print("You have completed the foyer")
	# while house.basement.completed == False:
	# 	# print next available rooms using connections
	# 	print("Next available rooms: \n")
	# 	for room in house.roomConnections[currentRoom]:
	# 		print(room.name)
	# 		print("\n")
	# 	location = input("Which room would you like to go to: ")
	# 	for room in house.roomConnections[currentRoom]:
	# 		if room.name == location:
	# 			location = room
	# 			room.runRoom()
	# 			currentRoom = location.roomToInt
	# 			break
	# if house.basement.completed == True:
	# 	print("You have completed the basement")
	# else:
	# 	print("You have completed the attic")
	# print("You have completed the game")
	exit(0)


if __name__ == "__main__":
    main()
