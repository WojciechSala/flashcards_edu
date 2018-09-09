from tkinter import *
from pathlib import Path
from random import randint
import random

def goto_answer():
	welcome.destroy()
	answer.pack()

def create_new_pair(event):
	manager.destroy()
	welcome.pack()

	file = Path("./pairs/{0}.txt".format(proj_name.get()))

	# creates a pair only when entry boxes are not empty
	if question_text.get() and answer_text.get():
		# exists -> append
		if file.is_file():
			f = open("./pairs/{0}.txt".format(proj_name.get()), "a")

		else:
			f = open("./pairs/{0}.txt".format(proj_name.get()), "w+")

		f.write("{0}|{1}\n".format(question_text.get(), answer_text.get()))
		f.close()

		# pairs counter
		pairs_value = 0
		with open("./pairs/{0}.txt".format(proj_name.get()), "r") as file:
			for line in file:
				pairs_value += 1

			Label(welcome, text="{0} pairs created".format(pairs_value)).grid(row=5, column=1, sticky=SE)
			file.close()

def create_task():
	random_answers = []
	num_of_lines = 0

	with open("./pairs/{0}.txt".format(proj_name.get()), "r") as file:
		for line in file:
			if len(random_answers) != 4:
				num_of_lines += 1
				# cuts '|' and everything before it and \n character at the end of the line
				ans = line[line.find("|") + 1:-1]
				# randomizer returns 0 or 1 every cycle and decides if current line will be used
				randomizer = random.getrandbits(1)
				random_answers.append(ans * randomizer)
				# cuts out empty elements
				random_answers = [x for x in random_answers if x != '']
				print("PICKED:", randomizer, random_answers)


root = Tk()
root.title("Flashcards")
welcome = Frame(root)
answer = Frame(root)
manager = Frame()

points_value = 0
question_text = StringVar()
answer_text = StringVar()
proj_name = StringVar()


# MANAGER PROJECT FORM
Label(manager, text="Name of your new project: ").grid(row=0, column=0, sticky=W)
Entry(manager, textvariable=proj_name, width=30).grid(row=0, column=1, ipady=5)
Label(manager, text="Press ENTER when done").grid(row=1, column=1, sticky=E)


# WELCOME FORM
Label(welcome, text="Input both question and answer then press ENTER to create a pair.").grid(row=0, column=1)
Label(welcome, text="Question:").grid(row=1, column=0, sticky=W)
Entry(welcome, textvariable=question_text, width=50).grid(row=1, column=1, ipady=5)
# Label(welcome, text="{0} asdasd".format(value)).grid(row=3, column=0, sticky=W)

Label(welcome).grid(row=2)

Label(welcome, text="Answer:").grid(row=3, column=0, sticky=W)
Entry(welcome, textvariable=answer_text, width=50).grid(row=3, column=1, ipady=5)

Label(welcome).grid(row=4)

root.bind("<Return>", create_new_pair)
Button(welcome, text="Start learning", command=create_task).grid(row=5, column=1)


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