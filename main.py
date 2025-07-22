import random

BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd


current_card = {}
to_learn = {}

try :
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card , timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canva.itemconfig(card_title , text="French" , fill = "black")
    canva.itemconfig(card_word , text=current_card["French"] , fill = "black")
    canva.itemconfig(card_image, image=card_front_img)
    timer = window.after(3000, flip_card)


def flip_card():
    canva.itemconfig(card_title , text="English" , fill="white")
    canva.itemconfig(card_word , text=current_card["English"] , fill = "white")
    canva.itemconfig(card_image , image = card_back_img)

def is_known():
    to_learn.remove(current_card)
    to_learn_df = pd.DataFrame(to_learn)
    to_learn_df.to_csv("data/words_to_learn.csv" , index=False)
    next_card()



################### UI ###############
window =  Tk()
window.title("Flashy")
window.config(padx= 50 , pady=50 , background=BACKGROUND_COLOR)
timer = window.after(3000 , flip_card)

canva = Canvas(width=800 , height=526)

card_front_img = PhotoImage(file = "images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_image = canva.create_image(400 , 263 , image= card_front_img)

card_title = canva.create_text(400 , 150 , text="" , font=("Ariel" , 40 ,  "italic"))
card_word = canva.create_text(400 , 256  , text = "" , font=("Ariel" , 68 ,  "bold"))

canva.config(background=BACKGROUND_COLOR, highlightthickness=0  , )
canva.grid(row=0, column=0 , columnspan=2)

Cross_buttonImage = PhotoImage(file="images/wrong.png")
cross_button = Button(image= Cross_buttonImage , highlightthickness=0 , command=next_card )
cross_button.grid(row=1 , column=0)

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image , highlightthickness=0 , command=is_known)
check_button.grid(row = 1 ,  column=1)

next_card()

window.mainloop()



