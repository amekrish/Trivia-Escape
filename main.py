class Room:
    def __init__(self, name, num_questions):
        self.name = name
        self.num_questions = num_questions
        self.questions = {}
    def describeDoorsAndStairs():
        # describes all the rooms and the stairs
    def describeRoom():
        # describe the things you can do in the current room
    objectList = []

class Object:
    def returnText():
    string objText = ""

def getQuestion():
    # ai stuff here

class House:
    def __init__():
        bedroom = Room("Bedroom", 4)
        office = Room("Office", 2)
        bathroom1 = Room("Master Bathroom", 1)
        garage = Room("Garage", 3)
        foyer = Room("Foyer", 1)
        livingRoom = Room("Living Room", 2)
        kitchen = Room("Kitchen", 3)
        diningRoom = Room("Dining Room", 5)
        gameRoom = Room("Game Room", 4)
        bathroom2 = Room("Bathroom", 2)
        basement = Room("Basement", 5)
        laundry = Room("Laundry", 2)
        closet = Room("Closet", 1)
        attic = Room("Attic", 7)
        self.rooms = [bedroom, office, bathroom1, garage, foyer, livingRoom, kitchen, diningRoom, gameRoom, bathroom2, basement, laundry, closet, attic]
        def setQuestions():
            # generate questions and assign them to rooms
    
class Question:
    def __init__(self, prompt, answer1, answer2, answer3, answer4, corAns):
        self.prompt = prompt
        self.answers = []
        self.answers.append(answer1)
        self.answers.append(answer2)
        self.answers.append(answer3)
        self.answers.append(answer4)
        self.corAns = corAns
        self.isUsed = False
    
    def setUsed(self):
        self.isUsed = True

def main():
    print("""Welcome to "The Enigma Residence,"
    an immersive, interactive escape game. 
    Upon receiving a cryptic phone call, 
    you've been led to an unsettlingly quiet house. 
    Upon entering, the front door slams shut behind you, 
    locking you inside. Solve a diverse array of challenging riddles 
    and answer riveting questions as you traverse into the depths of this 
    peculiar abode. Each correct response earns you handy tools and insightful clues, 
    indispensable in navigating a path to your escape. 
    Strap yourself in for a roller coaster of emotion, decisiveness, patience, and intellectual agility. 
    Your freedom is only a puzzle away. Can you decipher the enigma of the house and regain your freedom? 
    Let’s find out.""")
    
if __name__ == "__main__":
    main()
