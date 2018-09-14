from tkinter import *
from pathlib import Path
from random import randint
import random

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
	questions = []
	questions_used = []
	not_picked_answers = []
	pair = []
	answer_button_text = []
	num_of_lines = 0
	points_value = 0

	with open("./pairs/{0}.txt".format(proj_name.get()), "r") as file:
		for line in file:
			num_of_lines += 1
			# helps create question - answer links for later use
			pair.append(line[:-1])
			# cuts '|' and everything before it and \n character at the end of the line
			ans = line[line.find("|") + 1:-1]
			que = line[:line.find("|")]
			questions.append(que)

			# stop inserting answers into the list when it has 4 elements
			if len(random_answers) != 4:
				# randomizer returns 0 or 1 every cycle and decides if current line will be used
				randomizer = random.getrandbits(1)
				# if current line is not being used, put it into buffer 'not_picked_answers' list
				if randomizer == 0:
					not_picked_answers.append(ans)

				# decides if current line will be in the list
				random_answers.append(ans * randomizer)
				# cuts out empty elements
				random_answers = [x for x in random_answers if x != '']

				"""
				If 'random_answers' list is not full, fills it with
				a random (not already used) answer held in 'not_picked_answers' list.
				"""
				if num_of_lines > 4:
					while len(random_answers) < 4:
						npa_list_elem = random.choice(not_picked_answers)
						random_answers.append(npa_list_elem)
						not_picked_answers.remove(npa_list_elem)

	print("PAIRS:", pair)
	print("PICKED:", random_answers)

	random_question = random.choice(questions)
	# finds given question in pair list
	picked_pair = pair[questions.index(random_question)]
	# cuts out useless part (the question)
	correct_answer = picked_pair[picked_pair.find("|") + 1:]
	print("ANSWER IS:", correct_answer)

	# put correct answer into final list if not found there
	if correct_answer not in random_answers:
		# element's index
		random_element_to_replace = random.randint(0, len(random_answers))
		random_answers[random_element_to_replace] = correct_answer
		random.shuffle(random_answers)

	if random_question not in questions_used:
		Label(answer, text=random_question).grid(row=2, column=2)
		Label(answer).grid(row=3)

		print("QUESTON IS:", random_question, questions_used)
		# don't show the same question twice
		questions_used.append(random_question)

	Label(answer, text=points_value).grid(row=0, column=0, sticky=NW)
	Label(answer).grid(row=1)

	# shuffles and outputs answers
	random.shuffle(random_answers)
	ans1 = Button(answer, text=random_answers[0])
	ans1.grid(row=4, column=0, ipady=5, ipadx=5)

	ans2 = Button(answer, text=random_answers[1])
	ans2.grid(row=4, column=1, ipady=5, ipadx=5)

	ans3 = Button(answer, text=random_answers[2])
	ans3.grid(row=4, column=2, ipady=5, ipadx=5)

	ans4 = Button(answer, text=random_answers[3])
	ans4.grid(row=4, column=2, ipady=5, ipadx=5)

	# button's text
	answer_button_text.append(ans1.cget('text'))
	answer_button_text.append(ans2.cget('text'))
	answer_button_text.append(ans3.cget('text'))
	answer_button_text.append(ans4.cget('text'))

	# grab pushed button and check if answer is correct or not
	def check_result():
		# index of correct answer in list so specific button
		answer_button_text.index(correct_answer)
		# !!grab pressed button and print it's text

	Button(answer, text=random_answers[0], command=check_result).grid(row=4, column=0, ipady=5, ipadx=5)
	Button(answer, text=random_answers[1], command=check_result).grid(row=4, column=1, ipady=5, ipadx=5)
	Button(answer, text=random_answers[2], command=check_result).grid(row=4, column=2, ipady=5, ipadx=5)
	Button(answer, text=random_answers[3], command=check_result).grid(row=4, column=3, ipady=5, ipadx=5)

	welcome.destroy()
	answer.pack()


root = Tk()
root.title("Flashcards")
welcome = Frame(root)
answer = Frame(root)
manager = Frame()

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

manager.pack()
root.mainloop()