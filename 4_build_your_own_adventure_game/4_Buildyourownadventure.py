print("Welcome to The Adventure, hope you have a good time here!")
name = input("Enter your name: ")

def adventure():
    print("You started your day, completed your daily routine (brushing, bathing, breakfast, etc.)")
    answer = input("Now you are lying on your bed. Do you go to college or stay in your hostel? (college/hostel): ").lower()
    
    if answer == "college":
        print("You head to college and enter your first class.")
        answer = input("Your professor is running late. Do you chat with friends or scroll through your phone? (chat/phone): ").lower()
        
        if answer == "chat":
            print("You engage in an interesting conversation about weekend plans.")
            answer = input("Your friends suggest going to a new café. Do you invite me to join? (yes/no): ").lower()
            if answer == "yes":
                print("That's great! I was hoping we could spend some time together.")
                answer = input("Would you like to go for coffee first? (yes/no): ").lower()
                if answer == "yes":
                    print("Nice! Let’s grab some coffee and chat.")
                    answer = input("Should we also plan a movie later? (yes/no): ").lower()
                    if answer == "yes":
                        print("Perfect! A fun day it is.")
                        answer = input("Should we invite others or keep it just us? (invite/just us): ").lower()
                        if answer == "invite":
                            print("More the merrier! But I’d love to spend time with just you sometime too.")
                        else:
                            print("Great! I was hoping we’d get some one-on-one time.")
                    else:
                        print("No worries! Coffee is a great start.")
                else:
                    print("Alright, maybe a meal instead?")
            else:
                print("No worries! Maybe another time? I’d really like to hang out with you.")
        
        else:
            print("You see an interesting meme and decide to share it with me.")
            answer = input("I reply with a laughing emoji. Do you continue the conversation? (yes/no): ").lower()
            if answer == "yes":
                print("We keep talking, and I eventually ask: Would you like to go out with me sometime?")
                answer = input("Would you prefer a coffee date or something adventurous? (coffee/adventure): ").lower()
                if answer == "coffee":
                    print("Nice choice! A cozy café sounds perfect.")
                    answer = input("Should we make it a brunch too? (yes/no): ").lower()
                    if answer == "yes":
                        print("Awesome! Brunch and coffee it is.")
                    else:
                        print("Coffee alone is great too!")
                else:
                    print("Exciting! Let’s plan something adventurous together.")
            else:
                print("You miss the opportunity, but hey, I’d still love to go out with you!")
    
    else:
        print("You decide to stay in your hostel and relax.")
        answer = input("You feel hungry. Do you order food or go to the mess? (order/mess): ").lower()
        
        if answer == "order":
            print("While ordering, you remember we both like the same restaurant.")
            answer = input("Do you ask me if I want to order together? (yes/no): ").lower()
            if answer == "yes":
                print("That sounds fun! Maybe we could go out for a meal sometime too?")
                answer = input("Would you prefer a casual dinner or a fancy restaurant? (casual/fancy): ").lower()
                if answer == "casual":
                    print("Perfect! I know a great place for a relaxed meal.")
                else:
                    print("Great choice! Let’s dress up and enjoy a fancy dinner.")
            else:
                print("You eat alone, but honestly, I’d still love to go out with you sometime.")
        
        else:
            print("You see me in the mess and sit nearby.")
            answer = input("Do you start a conversation about the food or about classes? (food/classes): ").lower()
            if answer == "food":
                print("We both complain about the mess food and joke about eating out sometime. Actually, how about we do that for real?")
                answer = input("Would you rather go for a morning coffee or an evening hangout? (morning/evening): ").lower()
                if answer == "morning":
                    print("Sounds good! A fresh morning coffee date it is.")
                else:
                    print("Nice! An evening hangout will be fun.")
            else:
                print("I give you some class notes, and later you text me to thank me, which turns into a longer conversation. Maybe we should continue it over coffee?")
    
    answer = input("You get a text from me. Do you respond immediately or wait a while? (immediately/wait): ").lower()
    if answer == "immediately":
        print("Nice! We start chatting right away.")
    else:
        print("Playing it cool, huh? I’ll still be here to chat.")
    
    answer = input("I ask you if you’d like to go out this weekend. Do you say yes or suggest another day? (yes/another): ").lower()
    if answer == "yes":
        print("Awesome! Let’s plan something fun.")
    else:
        print("No worries! Let me know when you’re free.")
    
    print("So, here’s the real question:")
    answer = input("Would you like to go out on a date with me? (yes/no): ").lower()
    if answer == "yes":
        print("That's amazing! Let's plan something fun together.")
    else:
        print("No worries! I just wanted to ask. Thanks for playing this little adventure.")
    
    print("Either way, I’m glad we had this conversation!")
    
    input("Press Enter to exit the game.")
    
adventure()