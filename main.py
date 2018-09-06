from tkinter import *

root = Tk()
root.title("Flashcards")

Label(root, text="Question:").grid(row=0, column=0, sticky=W)
Entry(root, width=50).grid(row=0, column=1, ipady=5)

Label(root).grid(row=1)

Label(root, text="Answer:").grid(row=2, column=0, sticky=W)
Entry(root, width=50).grid(row=2, column=1, ipady=5)

Label(root).grid(row=3)

Button(root, text="Start learning").grid(row=4)


root.mainloop()