import collections
import numpy as np
import random

random.seed(0)

def simulate(p):
	pass_list = []
	for i in range(10):
		r = random.random()
		if r < p:
			pass_list.append('w' if r < 0.5 else 'm')
	counter = collections.Counter(pass_list)
	return len(pass_list) if counter['w'] >= 2 else None

if __name__ == '__main__':
	pass_results = []
	for i in range(100000):
		sim_res = simulate(0.9)
		if sim_res is not None:
			pass_results.append(sim_res)

	print(sum(pass_results) / len(pass_results))