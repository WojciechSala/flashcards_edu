from tkinter import *

def learning_form():
	welcome.destroy()
	answer.pack()


root = Tk()
root.title("Flashcards")


welcome = Frame(root)

pairs_value = 0
# q&a input in a loop
Label(welcome, text="Question:").grid(row=0, column=0, sticky=W)
question_value = Entry(welcome, width=50).grid(row=0, column=1, ipady=5)

Label(welcome).grid(row=1)

Label(welcome, text="Answer:").grid(row=2, column=0, sticky=W)
answer_value = Entry(welcome, width=50).grid(row=2, column=1, ipady=5)

Label(welcome).grid(row=3)

# outputs how how many pairs were already created
Label(welcome, text="{0} pairs created".format(pairs_value)).grid(row=4, column=1, sticky=SE)
start_learning = Button(welcome, text="Start learning", command=learning_form).grid(row=4)

welcome.pack()


answer = Frame(root)

points_value = 0
question_value = "sad"
Label(answer, text=points_value).grid(row=0, column=0, sticky=NW)
Label(answer).grid(row=1,)
Label(answer, text=question_value).grid(row=2, column=2)

Label(answer).grid(row=3)

# randomly picked answer_value in def, only one correct
Button(answer, text="ans1").grid(row=4, column=0, ipady=5, ipadx=5)
Button(answer, text="ans2").grid(row=4, column=1, ipady=5, ipadx=5)
Button(answer, text="ans3").grid(row=4, column=2, ipady=5, ipadx=5)
Button(answer, text="ans4").grid(row=4, column=3, ipady=5, ipadx=5)


root.mainloop()