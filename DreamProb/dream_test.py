import random
import matplotlib.pyplot as plt
import numpy as np
import progressbar

import concurrent.futures
import time

def getPearls():
	if random.random()*423 <= 20:
		quantity = (int)(random.random()*5)+4
		return quantity;
	else:
		return 0


def getIngots(goal):
	pearls = 0
	ingots = 0
	while pearls < goal:
		pearls += getPearls()
		ingots += 1
	return ingots

def getResults(goal, pbar=False):
	length = 200;
	results = np.zeros(length)
	repeats = 10**7

	if pbar is False:
		for i in range(repeats):
			ingots = getIngots(goal)
			if ingots < length:
				results[ingots] +=1
	else:
		for i in progressbar.progressbar(range(repeats)):
			ingots = getIngots(goal)
			if ingots < length:
				results[ingots] +=1

	results = [x/repeats for x in results]
	return results

def base():
	return np.mean([getPearls() for i in range(10**5)])

def main():
	x = range(200)
	total = np.sum([i for i in x])

	with concurrent.futures.ThreadPoolExecutor() as executor:
		baseFuture = executor.submit(base)
		future10 = executor.submit(getResults, 10, pbar=True)
		future11 = executor.submit(getResults, 11)
		future12 = executor.submit(getResults, 12)

		pearls_per_ingot = baseFuture.result()
		results10 = future10.result()
		results11 = future11.result()
		results12 = future12.result()

	plt.plot(x, results10)
	plt.plot(x, results11)
	plt.plot(x, results12)

	print("expected for 10: {}".format(10/pearls_per_ingot))
	print("actual: {}".format( np.argmax(results10) ))
	
	print("expected for 11: {}".format(11/pearls_per_ingot))
	print("actual: {}".format( np.argmax(results11) ))

	print("expected for 12: {}".format(12/pearls_per_ingot))
	print("actual: {}".format( np.argmax(results12) ))

	plt.show()



if __name__ == '__main__':
	main()