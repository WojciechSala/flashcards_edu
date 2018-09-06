from tkinter import *

def learning_form():
	welcome.destroy()
	answer.pack()


root = Tk()
root.title("Flashcards")


welcome = Frame(root)

Label(welcome, text="Question:").grid(row=0, column=0, sticky=W)
question_value = Entry(welcome, width=50).grid(row=0, column=1, ipady=5)

Label(welcome).grid(row=1)

Label(welcome, text="Answer:").grid(row=2, column=0, sticky=W)
answer_value = Entry(welcome, width=50).grid(row=2, column=1, ipady=5)

Label(welcome).grid(row=3)

start_learning = Button(welcome, text="Start learning", command=learning_form).grid(row=4)

welcome.pack()


answer = Frame(root)

points_value = 0
question = "sad"
Label(answer, text=points_value).grid(row=0, column=0, sticky=NW)
Label(answer).grid(row=1,)
Label(answer, text=question_value).grid(row=2, column=2)

Label(answer).grid(row=3)

# randomly picked answer_value in def
Button(answer).grid(row=4, column=0)


root.mainloop()