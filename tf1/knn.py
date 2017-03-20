import numpy as np
from math import sqrt
import warnings 
import collections
import pickle
import random


def knn(data, predict, k = 2):
	if len(data) >= k:
		warnings.warn('k is set to value less than total voting classes')
	distances = []
	for group in data:
		for features in data[group]:
			euclidean_distance = np.linalg.norm(np.array)