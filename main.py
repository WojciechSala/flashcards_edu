from tkinter import *

def learning_form():
	welcome.destroy()
	answer.pack()

def goto_pairs(event):
	manager.destroy()
	welcome.pack()

def create_new_pair():
	print (question_text.get(), answer_text.get())

root = Tk()
root.title("Flashcards")
welcome = Frame(root)
answer = Frame(root)
manager = Frame(root)

pairs_value = 0
points_value = 0
question_text = StringVar()
answer_text = StringVar()
proj_name = StringVar()


# MANAGER PROJECT FORM
Label(manager, text="Name of your new project: ").grid(row=0, column=0, sticky=W)
Entry(manager, textvariable=proj_name, width=30).grid(row=0, column=1, ipady=5)
root.bind("<Return>", goto_pairs)
Label(manager, text="Press enter when done").grid(row=1, column=1, sticky=E)


# WELCOME FORM
Label(welcome, text="Question:").grid(row=0, column=0, sticky=W)
Entry(welcome, textvariable=question_text, width=50).grid(row=0, column=1, ipady=5)
# Label(welcome, text="{0} asdasd".format(value)).grid(row=3, column=0, sticky=W)

Label(welcome).grid(row=1)

Label(welcome, text="Answer:").grid(row=2, column=0, sticky=W)
Entry(welcome, textvariable=answer_text, width=50).grid(row=2, column=1, ipady=5)

Label(welcome).grid(row=3)

# outputs how how many pairs were already created
Label(welcome, text="{0} pairs created".format(pairs_value)).grid(row=4, column=1, sticky=SE)
Button(welcome, text="Create next one", command=create_new_pair).grid(row=4)
start_learning = Button(welcome, text="Start learning", command=learning_form).grid(row=4, column=1)


# ANSWER FORM
Label(answer, text=points_value).grid(row=0, column=0, sticky=NW)
Label(answer).grid(row=1,)
Label(answer, text=question_text).grid(row=2, column=2)

Label(answer).grid(row=3)

# randomly picked answer_value in def, only one correct
Button(answer, text="ans1").grid(row=4, column=0, ipady=5, ipadx=5)
Button(answer, text="ans2").grid(row=4, column=1, ipady=5, ipadx=5)
Button(answer, text="ans3").grid(row=4, column=2, ipady=5, ipadx=5)
Button(answer, text="ans4").grid(row=4, column=3, ipady=5, ipadx=5)

manager.pack()
root.mainloop()