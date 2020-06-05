import numpy as np
from helpers.math import *
from helpers.file import *
from task.task import *

tasks = load("tasks.txt")
scale = [0, 0.5, 1, 2, 3, 5, 8, 13, 20, 40]

n = len(tasks)

comparison_matrix = [[ti.sp/tj.sp for ti in tasks] for tj in tasks]
comparison_matrix = np.array(comparison_matrix)

mrs = np.array([gmean(row) for row in list(comparison_matrix)])
mrs_ref = min(mrs)
t_ref = tasks[np.where(mrs == mrs_ref)[0][0]]

story_points = t_ref.sp/mrs_ref * mrs

inconsistency = std(comparison_matrix, mrs)**0.5
error = inconsistency/n**0.5
print(f"InconsistencyIndex: {inconsistency*100:.2f}%")
print(f"Error:              {error*100:.2f}%")

for task, sp in zip(tasks, story_points):
	task.sp = find_nearest(scale, sp)

[print(task) for task in tasks]
