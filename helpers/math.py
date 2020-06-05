import numpy as np
from math import log

def gmean(a: list):
	product = 1
	for ai in a:
		product *= ai
	return product**(1/len(a))

def std(comp_matrix, mrs):
	cm = list(comp_matrix)
	mrs = list(mrs)
	n = len(mrs)

	s = 0
	for j in range(n):
		for i in range(j):
			s += (log(cm[i][j]) - log(mrs[i]/mrs[j]))**2

	return s/(n*(n-1)/2 - (n-1))

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]
	