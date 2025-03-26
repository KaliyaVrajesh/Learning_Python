import tkinter as tk
from tkinter import messagebox
import random

# Define the game logic as functions
class AdventureGame:
    def __init__(self, root):
        self.root = root
        self.root.title("The Adventure Game")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")
        self.root.resizable(True, True)  # Allow window resizing
        
        self.name = ""
        self.continue_button2 = None  # Initialize as None
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Welcome to The Adventure", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333")
        self.title_label.pack(pady=20)

        self.intro_label = tk.Label(self.root, text="You started your day, completed your daily routine (brushing, bathing, breakfast, etc.)", font=("Arial", 12), bg="#f0f0f0", fg="#333")
        self.intro_label.pack(pady=10)

        self.name_entry_label = tk.Label(self.root, text="Enter your name:", font=("Arial", 12), bg="#f0f0f0", fg="#333")
        self.name_entry_label.pack()
        
        self.name_entry = tk.Entry(self.root, font=("Arial", 14))
        self.name_entry.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start Adventure", font=("Arial", 14), command=self.start_adventure)
        self.start_button.pack(pady=20)

    def start_adventure(self):
        self.name = self.name_entry.get()
        if not self.name:
            messagebox.showwarning("Input Error", "Please enter your name!")
            return
        self.name_entry_label.pack_forget()
        self.name_entry.pack_forget()
        self.start_button.pack_forget()

        self.show_intro()

    def show_intro(self):
        self.intro_label.config(text=f"Welcome, {self.name}!\nYou are lying on your bed. Do you go to college or stay in your hostel?")
        self.continue_button = tk.Button(self.root, text="College", font=("Arial", 14), command=self.go_college)
        self.continue_button.pack(side="left", padx=10)

        self.continue_button2 = tk.Button(self.root, text="Hostel", font=("Arial", 14), command=self.go_hostel)
        self.continue_button2.pack(side="right", padx=10)

    def go_college(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="You head to college and enter your first class.\nYour professor is running late. Do you chat with friends or scroll through your phone?")
        self.continue_button = tk.Button(self.root, text="Chat", font=("Arial", 14), command=self.chat_with_friends)
        self.continue_button.pack(side="left", padx=10)

        self.continue_button2 = tk.Button(self.root, text="Scroll Phone", font=("Arial", 14), command=self.scroll_phone)
        self.continue_button2.pack(side="right", padx=10)

    def go_hostel(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="You decide to stay in your hostel and relax.\nYou feel hungry. Do you order food or go to the mess?")
        self.continue_button = tk.Button(self.root, text="Order", font=("Arial", 14), command=self.order_food)
        self.continue_button.pack(side="left", padx=10)

        self.continue_button2 = tk.Button(self.root, text="Mess", font=("Arial", 14), command=self.go_mess)
        self.continue_button2.pack(side="right", padx=10)

    def chat_with_friends(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="You engage in an interesting conversation about weekend plans.\nYour friends suggest going to a new café. Do you invite me to join?")
        self.continue_button = tk.Button(self.root, text="Yes", font=("Arial", 14), command=self.invite_me)
        self.continue_button.pack(side="left", padx=10)

        self.continue_button2 = tk.Button(self.root, text="No", font=("Arial", 14), command=self.no_invite)
        self.continue_button2.pack(side="right", padx=10)

    def invite_me(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="That's great! I was hoping we could spend some time together.\nWould you like to go for coffee first?")
        self.continue_button = tk.Button(self.root, text="Yes", font=("Arial", 14), command=self.go_for_coffee)
        self.continue_button.pack(side="left", padx=10)

        self.continue_button2 = tk.Button(self.root, text="No", font=("Arial", 14), command=self.no_coffee)
        self.continue_button2.pack(side="right", padx=10)

    def go_for_coffee(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="Nice! Let’s grab some coffee and chat.\nShould we also plan a movie later?")
        self.continue_button = tk.Button(self.root, text="Yes", font=("Arial", 14), command=self.plan_movie)
        self.continue_button.pack(side="left", padx=10)

        self.continue_button2 = tk.Button(self.root, text="No", font=("Arial", 14), command=self.no_movie)
        self.continue_button2.pack(side="right", padx=10)

    def plan_movie(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="Perfect! A fun day it is.\nShould we invite others or keep it just us?")
        self.continue_button = tk.Button(self.root, text="Invite", font=("Arial", 14), command=self.invite_others)
        self.continue_button.pack(side="left", padx=10)

        self.continue_button2 = tk.Button(self.root, text="Just Us", font=("Arial", 14), command=self.just_us)
        self.continue_button2.pack(side="right", padx=10)

    def invite_others(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="More the merrier! But I’d love to spend time with just you sometime too.")
        self.end_game()

    def just_us(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="Great! I was hoping we’d get some one-on-one time.")
        self.end_game()

    def no_invite(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="No worries! Maybe another time? I’d really like to hang out with you.")
        self.end_game()

    def no_coffee(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="Alright, maybe a meal instead?")
        self.end_game()

    def no_movie(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="No worries! Coffee is a great start.")
        self.end_game()

    def scroll_phone(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="You see an interesting meme and decide to share it with me.\nI reply with a laughing emoji. Do you continue the conversation?")
        self.continue_button = tk.Button(self.root, text="Yes", font=("Arial", 14), command=self.continue_conversation)
        self.continue_button.pack(side="left", padx=10)

        self.continue_button2 = tk.Button(self.root, text="No", font=("Arial", 14), command=self.no_conversation)
        self.continue_button2.pack(side="right", padx=10)

    def continue_conversation(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="We keep talking, and I eventually ask: Would you like to go out with me sometime?\nWould you prefer a coffee date or something adventurous?")
        self.continue_button = tk.Button(self.root, text="Coffee", font=("Arial", 14), command=self.coffee_date)
        self.continue_button.pack(side="left", padx=10)

        self.continue_button2 = tk.Button(self.root, text="Adventure", font=("Arial", 14), command=self.adventure_date)
        self.continue_button2.pack(side="right", padx=10)

    def coffee_date(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="Nice choice! A cozy café sounds perfect.\nShould we make it a brunch too?")
        self.continue_button = tk.Button(self.root, text="Yes", font=("Arial", 14), command=self.brunch_yes)
        self.continue_button.pack(side="left", padx=10)

        self.continue_button2 = tk.Button(self.root, text="No", font=("Arial", 14), command=self.brunch_no)
        self.continue_button2.pack(side="right", padx=10)

    def brunch_yes(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="Awesome! Brunch and coffee it is.")
        self.end_game()

    def brunch_no(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="Coffee alone is great too!")
        self.end_game()

    def adventure_date(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="Exciting! Let’s plan something adventurous together.")
        self.end_game()

    def no_conversation(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="You miss the opportunity, but hey, I’d still love to go out with you!")
        self.end_game()

    def order_food(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="While ordering, you remember we both like the same restaurant.\nDo you ask me if I want to order together?")
        self.continue_button = tk.Button(self.root, text="Yes", font=("Arial", 14), command=self.order_together)
        self.continue_button.pack(side="left", padx=10)

        self.continue_button2 = tk.Button(self.root, text="No", font=("Arial", 14), command=self.order_alone)
        self.continue_button2.pack(side="right", padx=10)

    def order_together(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="That sounds fun! Maybe we could go out for a meal sometime too?\nWould you prefer a casual dinner or a fancy restaurant?")
        self.continue_button = tk.Button(self.root, text="Casual", font=("Arial", 14), command=self.casual_dinner)
        self.continue_button.pack(side="left", padx=10)

        self.continue_button2 = tk.Button(self.root, text="Fancy", font=("Arial", 14), command=self.fancy_dinner)
        self.continue_button2.pack(side="right", padx=10)

    def casual_dinner(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="Perfect! I know a great place for a relaxed meal.")
        self.end_game()

    def fancy_dinner(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="Great choice! Let’s dress up and enjoy a fancy dinner.")
        self.end_game()

    def order_alone(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="You eat alone, but honestly, I’d still love to go out with you sometime.")
        self.end_game()

    def go_mess(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="You see me in the mess and sit nearby.\nDo you start a conversation about the food or about classes?")
        self.continue_button = tk.Button(self.root, text="Food", font=("Arial", 14), command=self.talk_about_food)
        self.continue_button.pack(side="left", padx=10)

        self.continue_button2 = tk.Button(self.root, text="Classes", font=("Arial", 14), command=self.talk_about_classes)
        self.continue_button2.pack(side="right", padx=10)

    def talk_about_food(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="We both complain about the mess food and joke about eating out sometime. Actually, how about we do that for real?\nWould you rather go for a morning coffee or an evening hangout?")
        self.continue_button = tk.Button(self.root, text="Morning", font=("Arial", 14), command=self.morning_coffee)
        self.continue_button.pack(side="left", padx=10)

        self.continue_button2 = tk.Button(self.root, text="Evening", font=("Arial", 14), command=self.evening_hangout)
        self.continue_button2.pack(side="right", padx=10)

    def morning_coffee(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="Sounds good! A fresh morning coffee date it is.")
        self.end_game()

    def evening_hangout(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="Nice! An evening hangout will be fun.")
        self.end_game()

    def talk_about_classes(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="I give you some class notes, and later you text me to thank me, which turns into a longer conversation. Maybe we should continue it over coffee?")
        self.end_game()

    def end_game(self):
        self.intro_label.config(text="So, here’s the real question: Would you like to go out on a date with me?")
        self.continue_button = tk.Button(self.root, text="Yes", font=("Arial", 14), command=self.date_yes)
        self.continue_button.pack(side="left", padx=10)

        self.continue_button2 = tk.Button(self.root, text="No", font=("Arial", 14), command=self.date_no)
        self.continue_button2.pack(side="right", padx=10)

    def date_yes(self):
        self.continue_button.pack_forget()
        if self.continue_button2:
            self.continue_button2.pack_forget()

        self.intro_label.config(text="That's amazing! Let's plan something fun together.")
        self.final_message()

    def date_no(self):
        # Move the "No" button to a random position
        x = random.randint(0, 500)
        y = random.randint(0, 350)
        self.continue_button2.place(x=x, y=y)

    def final_message(self):
        self.intro_label.config(text=f"Either way, I’m glad we had this conversation!\nThanks for playing, {self.name}!")
        self.continue_button = tk.Button(self.root, text="Exit", font=("Arial", 14), command=self.root.quit)
        self.continue_button.pack(pady=20)


# Main Program
root = tk.Tk()
game = AdventureGame(root)
root.mainloop()