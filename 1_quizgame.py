print("Welcome to Anime Quiz!")
point = 0

#question no 1
print("First question: Character Named Monkey D Luffy is from which Anime Universe?")
a = 0
print("1: One Piece")
print("2: Naruto")
a = int(input("Answer:"))
if a == 1:
    print ("Correct answer")
    point = point + 1
else:
    print("Wrong Answer")

#question no 2
print("Second question: Who is better Marine?")
a = 0
print("1: Akainu")
print("2: Kizaru")
a = int(input("Answer:"))
if a == 2:
    print ("Correct answer")
    point = point + 1
else:
    print("Wrong Answer")

#question no 3
print("Third Question: Windstyle can enhance power of which style jutsu?")
a = 0
print("1: Fire")
print("2: Earth")
a = int(input("Answer:"))
if a == 1:
    print ("Correct answer")
    point = point + 1
else:
    print("Wrong Answer")

#question no 4
print("Who is the only female hokage up until now?")
a = 0
print("1: Kushina Uzumaki")
print("2: Tsunade Tsenju")
a = int(input("Answer:"))
if a == 2:
    print ("Correct answer")
    point = point + 1
else:
    print("Wrong Answer")

#question no 5
print("Who were the og legendary sanin?")
a = 0
print("1: Naruto ,Sakura, Sasuke")
print("2: Jiraya, Tsunade, Orochimaru")
a = int(input("Answer:"))
if a == 2:
    print ("Correct answer")
    point = point + 1
else:
    print("Wrong Answer")

print()
if point < 2:
    print("Score: "+ str(point))
    print("Better luck next time! :(")

else:
    print("Score: "+ str(point))
    print("Congratulation! :)")