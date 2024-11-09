import random
from tkinter import *
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
try:
    words = pd.read_csv("words_to_learn.csv")
except(FileNotFoundError):
    words = pd.read_csv("data/french_words.csv")
finally:
    word_fr = random.choice(words.French)

def turn_french():
    global word_en
    fr = words[words.French == word_fr]
    word_en = fr["English"].values[0]
    canvas.itemconfig(start_card, image=card_front)
    canvas.itemconfig(en_title, text="English")
    canvas.itemconfig(en_words, text=word_en)
def count_down():
    window.after(3000, turn_french)

def right():
    global word_fr
    global word_en
    global words
    clear = words[words.English == word_en].index[0]
    words = words.drop(clear)
    words.to_csv("words_to_learn.csv")
    print(len(words.English))
    print(len(words.French))
    canvas.itemconfig(start_card, image=card_back)
    canvas.itemconfig(en_title,text="French")
    word_fr = random.choice(words.French)
    canvas.itemconfig(en_words,text=word_fr)
    count_down()

def wrong():
    global word_fr
    global word_en
    canvas.itemconfig(start_card, image=card_back)
    word_fr = random.choice(words.French)
    canvas.itemconfig(en_title, text="French")
    canvas.itemconfig(en_words, text=word_fr)
    count_down()




window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg="#B1DDC6")
canvas = Canvas(width=800, height=600, bg="#B1DDC6", highlightthickness=0)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
start_card = canvas.create_image(400, 263, image=card_back)
canvas.grid(row=0, column=0, columnspan=2)
yes_tick = PhotoImage(file="images/right.png")
yes_button = Button(image=yes_tick, highlightthickness=0,command=right)
yes_button.grid(row=1,column=0)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=wrong)
wrong_button.grid(row=1, column=1)
en_title = canvas.create_text(400, 150, text="French")
en_words = canvas.create_text(400, 263, text=word_fr)
count_down()

window.mainloop()