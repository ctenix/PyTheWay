# _*_ coding: utf-8 _*_

import numpy as np
from RecommandLib import *
from sklearn.cluster import KMeans
import matplotlib as plt
k = 4 
dataSet = file2matrix("Data/4k2_far.txt","\t")
dataMat = Mat(dataSet[:, 1:])
# Run KMeans algorithm
kmeans = KMeans