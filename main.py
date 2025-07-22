BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *

window =  Tk()
window.title("Flashy")
window.config(padx= 50 , pady=50 , background=BACKGROUND_COLOR)

canva = Canvas(width=800 , height=526)
card_front_img = PhotoImage(file = "images/card_front.png")
canva.create_image(400 , 263 , image= card_front_img)
canva.create_text(400 , 150 , text="Title" , font=("Ariel" , 40 ,  "italic"))
canva.create_text(400 , 256  , text = "word" , font=("Ariel" , 68 ,  "bold"))
canva.config(background=BACKGROUND_COLOR, highlightthickness=0)
canva.grid(row=0, column=0 , columnspan=2)

Cross_buttonImage = PhotoImage(file="images/wrong.png")
cross_button = Button(image= Cross_buttonImage , highlightthickness=0 )
cross_button.grid(row=1 , column=0)

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image , highlightthickness=0)
check_button.grid(row = 1 ,  column=1)


window.mainloop()
