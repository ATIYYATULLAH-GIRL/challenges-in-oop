class Flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+"("+self.meaning +")"
flash=[]
print("Welcome to falshcard applications")
while True:
    word=input("Enter a word you want to add to the flashcard: ")
    meaning=input("Enter its meaning: ")
    flash.append(Flashcard(word,meaning))
    option=int(input("do you want to add more.Enter 0 to add more or 1 to exit"))
    if option:
        break
print("Your flashcards")
for i in flash:
    print("-->",i)