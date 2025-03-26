from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
import random

# Define the game logic as functions
class AdventureGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 10
        self.padding = 20
        self.name = ""
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = Label(
            text="Welcome to The Adventure",
            font_size=24,
            bold=True,
            size_hint=(1, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.title_label)

        # Intro Label
        self.intro_label = Label(
            text="You started your day, completed your daily routine (brushing, bathing, breakfast, etc.)",
            font_size=14,
            size_hint=(1, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)

        # Name Entry
        self.name_entry_label = Label(
            text="Enter your name:",
            font_size=14,
            size_hint=(1, None),
            height=30,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.name_entry_label)

        self.name_entry = TextInput(
            multiline=False,
            size_hint=(1, None),
            height=40,
            foreground_color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.name_entry)

        # Start Button
        self.start_button = Button(
            text="Start Adventure",
            font_size=14,
            size_hint=(1, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.start_button.bind(on_press=self.start_adventure)
        self.add_widget(self.start_button)

    def start_adventure(self, instance):
        self.name = self.name_entry.text
        if not self.name:
            self.show_popup("Input Error", "Please enter your name!")
            return
        self.clear_widgets()
        self.show_intro()

    def show_intro(self):
        self.intro_label = Label(
            text=f"Welcome, {self.name}!\nYou are lying on your bed. Do you go to college or stay in your hostel?",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)

        self.continue_button = Button(
            text="College",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button.bind(on_press=self.go_college)
        self.add_widget(self.continue_button)

        self.continue_button2 = Button(
            text="Hostel",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button2.bind(on_press=self.go_hostel)
        self.add_widget(self.continue_button2)

    def go_college(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="You head to college and enter your first class.\nYour professor is running late. Do you chat with friends or scroll through your phone?",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)

        self.continue_button = Button(
            text="Chat",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button.bind(on_press=self.chat_with_friends)
        self.add_widget(self.continue_button)

        self.continue_button2 = Button(
            text="Scroll Phone",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button2.bind(on_press=self.scroll_phone)
        self.add_widget(self.continue_button2)

    def go_hostel(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="You decide to stay in your hostel and relax.\nYou feel hungry. Do you order food or go to the mess?",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)

        self.continue_button = Button(
            text="Order",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button.bind(on_press=self.order_food)
        self.add_widget(self.continue_button)

        self.continue_button2 = Button(
            text="Mess",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button2.bind(on_press=self.go_mess)
        self.add_widget(self.continue_button2)

    def chat_with_friends(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="You engage in an interesting conversation about weekend plans.\nYour friends suggest going to a new café. Do you invite me to join?",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)

        self.continue_button = Button(
            text="Yes",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button.bind(on_press=self.invite_me)
        self.add_widget(self.continue_button)

        self.continue_button2 = Button(
            text="No",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button2.bind(on_press=self.no_invite)
        self.add_widget(self.continue_button2)

    def invite_me(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="That's great! I was hoping we could spend some time together.\nWould you like to go for coffee first?",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)

        self.continue_button = Button(
            text="Yes",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button.bind(on_press=self.go_for_coffee)
        self.add_widget(self.continue_button)

        self.continue_button2 = Button(
            text="No",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button2.bind(on_press=self.no_coffee)
        self.add_widget(self.continue_button2)

    def go_for_coffee(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="Nice! Let’s grab some coffee and chat.\nShould we also plan a movie later?",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)

        self.continue_button = Button(
            text="Yes",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button.bind(on_press=self.plan_movie)
        self.add_widget(self.continue_button)

        self.continue_button2 = Button(
            text="No",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button2.bind(on_press=self.no_movie)
        self.add_widget(self.continue_button2)

    def plan_movie(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="Perfect! A fun day it is.\nShould we invite others or keep it just us?",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)

        self.continue_button = Button(
            text="Invite",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button.bind(on_press=self.invite_others)
        self.add_widget(self.continue_button)

        self.continue_button2 = Button(
            text="Just Us",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button2.bind(on_press=self.just_us)
        self.add_widget(self.continue_button2)

    def invite_others(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="More the merrier! But I’d love to spend time with just you sometime too.",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)
        self.end_game()

    def just_us(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="Great! I was hoping we’d get some one-on-one time.",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)
        self.end_game()

    def no_invite(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="No worries! Maybe another time? I’d really like to hang out with you.",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)
        self.end_game()

    def no_coffee(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="Alright, maybe a meal instead?",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)
        self.end_game()

    def no_movie(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="No worries! Coffee is a great start.",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)
        self.end_game()

    def scroll_phone(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="You see an interesting meme and decide to share it with me.\nI reply with a laughing emoji. Do you continue the conversation?",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)

        self.continue_button = Button(
            text="Yes",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button.bind(on_press=self.continue_conversation)
        self.add_widget(self.continue_button)

        self.continue_button2 = Button(
            text="No",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button2.bind(on_press=self.no_conversation)
        self.add_widget(self.continue_button2)

    def continue_conversation(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="We keep talking, and I eventually ask: Would you like to go out with me sometime?\nWould you prefer a coffee date or something adventurous?",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)

        self.continue_button = Button(
            text="Coffee",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button.bind(on_press=self.coffee_date)
        self.add_widget(self.continue_button)

        self.continue_button2 = Button(
            text="Adventure",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button2.bind(on_press=self.adventure_date)
        self.add_widget(self.continue_button2)

    def coffee_date(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="Nice choice! A cozy café sounds perfect.\nShould we make it a brunch too?",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)

        self.continue_button = Button(
            text="Yes",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button.bind(on_press=self.brunch_yes)
        self.add_widget(self.continue_button)

        self.continue_button2 = Button(
            text="No",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button2.bind(on_press=self.brunch_no)
        self.add_widget(self.continue_button2)

    def brunch_yes(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="Awesome! Brunch and coffee it is.",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)
        self.end_game()

    def brunch_no(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="Coffee alone is great too!",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)
        self.end_game()

    def adventure_date(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="Exciting! Let’s plan something adventurous together.",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)
        self.end_game()

    def no_conversation(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="You miss the opportunity, but hey, I’d still love to go out with you!",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)
        self.end_game()

    def order_food(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="While ordering, you remember we both like the same restaurant.\nDo you ask me if I want to order together?",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)

        self.continue_button = Button(
            text="Yes",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button.bind(on_press=self.order_together)
        self.add_widget(self.continue_button)

        self.continue_button2 = Button(
            text="No",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button2.bind(on_press=self.order_alone)
        self.add_widget(self.continue_button2)

    def order_together(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="That sounds fun! Maybe we could go out for a meal sometime too?\nWould you prefer a casual dinner or a fancy restaurant?",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)

        self.continue_button = Button(
            text="Casual",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button.bind(on_press=self.casual_dinner)
        self.add_widget(self.continue_button)

        self.continue_button2 = Button(
            text="Fancy",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button2.bind(on_press=self.fancy_dinner)
        self.add_widget(self.continue_button2)

    def casual_dinner(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="Perfect! I know a great place for a relaxed meal.",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)
        self.end_game()

    def fancy_dinner(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="Great choice! Let’s dress up and enjoy a fancy dinner.",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)
        self.end_game()

    def order_alone(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="You eat alone, but honestly, I’d still love to go out with you sometime.",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)
        self.end_game()

    def go_mess(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="You see me in the mess and sit nearby.\nDo you start a conversation about the food or about classes?",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)

        self.continue_button = Button(
            text="Food",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button.bind(on_press=self.talk_about_food)
        self.add_widget(self.continue_button)

        self.continue_button2 = Button(
            text="Classes",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button2.bind(on_press=self.talk_about_classes)
        self.add_widget(self.continue_button2)

    def talk_about_food(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="We both complain about the mess food and joke about eating out sometime. Actually, how about we do that for real?\nWould you rather go for a morning coffee or an evening hangout?",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)

        self.continue_button = Button(
            text="Morning",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button.bind(on_press=self.morning_coffee)
        self.add_widget(self.continue_button)

        self.continue_button2 = Button(
            text="Evening",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button2.bind(on_press=self.evening_hangout)
        self.add_widget(self.continue_button2)

    def morning_coffee(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="Sounds good! A fresh morning coffee date it is.",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)
        self.end_game()

    def evening_hangout(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="Nice! An evening hangout will be fun.",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)
        self.end_game()

    def talk_about_classes(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="I give you some class notes, and later you text me to thank me, which turns into a longer conversation. Maybe we should continue it over coffee?",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)
        self.end_game()

    def end_game(self):
        self.clear_widgets()
        self.intro_label = Label(
            text="So, here’s the real question: Would you like to go out on a date with me?",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)

        self.continue_button = Button(
            text="Yes",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button.bind(on_press=self.date_yes)
        self.add_widget(self.continue_button)

        self.continue_button2 = Button(
            text="No",
            font_size=14,
            size_hint=(0.5, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button2.bind(on_press=self.date_no)
        self.add_widget(self.continue_button2)

    def date_yes(self, instance):
        self.clear_widgets()
        self.intro_label = Label(
            text="That's amazing! Let's plan something fun together.",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)
        self.final_message()

    def date_no(self, instance):
        # Move the "No" button to a random position
        self.continue_button2.pos_hint = {
            "x": random.uniform(0, 0.8),
            "y": random.uniform(0, 0.8)
        }

    def final_message(self):
        self.clear_widgets()
        self.intro_label = Label(
            text=f"Either way, I’m glad we had this conversation!\nThanks for playing, {self.name}!",
            font_size=14,
            size_hint=(1, None),
            height=100,
            color=(0, 0, 0, 1))  # Black text
        self.add_widget(self.intro_label)

        self.continue_button = Button(
            text="Exit",
            font_size=14,
            size_hint=(1, None),
            height=50,
            color=(0, 0, 0, 1))  # Black text
        self.continue_button.bind(on_press=self.exit_game)
        self.add_widget(self.continue_button)

    def exit_game(self, instance):
        App.get_running_app().stop()

    def show_popup(self, title, message):
        popup = Popup(
            title=title,
            content=Label(text=message, color=(0, 0, 0, 1)),  # Black text
            size_hint=(0.8, 0.4))
        popup.open()

    def clear_widgets(self):
        super().clear_widgets()


class AdventureGameApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)  # Set background color to white
        return AdventureGame()


if __name__ == "__main__":
    AdventureGameApp().run()