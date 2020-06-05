from task.task import Task

def load(name):
	tasks = []
	with open("tasks.txt") as file:
		for task in file:
			words = task.split()
			if str(words).find("#") != -1: 
				break
			sp = words[0]
			name = ' '.join(words[1:])
			tasks.append(Task(sp, name=name))
	return tasks
