import random
class FruitQuiz:
    def __init__(self):
        self.fruits={
            "apple":"red",
            "cucumber":"green",
            "pineapple":"yellow",
            "banana":"yellow",            
            "orange":"orange",
            "avocado":"avocado",
            "strawberry":"red"
        }
    def quiz(self):
        while True:
            fruit,color=random.choice(list(self.fruits.items()))
            print("What is the color of",fruit)
            user_answer=input()
            if user_answer.lower()==color:
                print("Correct answer")
            else:
                print("Wrong answer")
            option=input("Enter to 0 to continue or enter 1 to exit")
            if option:
                break
print("Welcome to fruit quiz")
fq=FruitQuiz()
fq.quiz()