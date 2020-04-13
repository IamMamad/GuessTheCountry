import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from countryGame import countryG


gui = tk.Tk()
gui.title('Guess the Country')
gui.iconbitmap('F:/Users/Mohammad/Documents/Sources/GuessTheCountry/icon.ico')


def create_Widgets():

    gameData = countryG()

    def displayData():
        right_label.config(text=gameData.rightGuesses)
        wrong_label.config(text=gameData.wrongGuesses)

        if gameData.isGameOver():
            country = gameData.country
            result = messagebox.askyesno("Game Over", "Answer is "+country+". Do you want to play again?")

            if result:
                right_label.destroy()
                wrong_label.destroy()
                create_Widgets()


    def submit():
        guessValue = guess_str.get()
        if guessValue == "":
            messagebox.showerror("Empty Guess", "Guess Can't Be Empty! Please Type in your guess.")
        else:
            guessValue = guessValue[0]
            guessValue = guessValue.lower()
            gameData.check(guessValue)
            displayData()
        guess_str.set("")


    def hint():
        result = messagebox.askyesno("Hint", "Are you sure? This will Cost you 2 Guesses!", icon='warning')

        if result:
            hint = gameData.hint()
            gameData.check(hint)
            displayData()

    monoSpacedFont = font.Font(family='Consolas', size=20)

    right_label = tk.Label(gui, text="rightGuesses", font=monoSpacedFont)
    right_label.grid(column=0, row=0, columnspan=3, padx=5, pady=5, sticky="W")

    wrong_label = tk.Label(gui, text="rightGuesses", font=monoSpacedFont)
    wrong_label.grid(column=0, row=1, columnspan=3, padx=5, pady=5, sticky="W")

    guess_label = tk.Label(gui, text="Type in Your Guess (only one letter):")
    guess_label.grid(column=0, row=2, columnspan=3, padx=5, pady=5)

    guess_str = tk.StringVar()  
    guess = ttk.Entry(gui, width=10, textvariable=guess_str)  
    guess.grid(column=0, row=3, pady=5, padx=5, sticky="E")

    submitBttn = ttk.Button(gui, text="Submit", command=submit)
    submitBttn.grid(column=1, row=3, padx=5, pady=5)

    hintBttn = ttk.Button(gui, text="Hint", command=hint)
    hintBttn.grid(column=2, row=3, padx=5, pady=5)

    displayData()


create_Widgets()
gui.mainloop() 