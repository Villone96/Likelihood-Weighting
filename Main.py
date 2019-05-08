from Function import LikelihoodWeighting
import numpy as np

cpTables = list()

# i adopt in all structure the follow topological order
# 0 : RushHour
# 1 : BadWeather
# 2 : Accident
# 3 : TrafficJam

# define a adjacency matrix with this structure 
# [[0. 0. 0. 0.] 
# [0. 0. 0. 0.]
# [0. 1. 0. 0.]
# [1. 1. 1. 0.]]
adjMatrix = np.zeros((4, 4))

adjMatrix[2][1] = 1
adjMatrix[3][0] = 1
adjMatrix[3][1] = 1
adjMatrix[3][2] = 1

# print(adjMatrix)

# define cpt Tables, with NoP as key i say "No Parents", otherwise i define the probability conditional on parents
# of course the order is like the bayesian network order 
cptRushHour = {'NoP': .2}

cptBadWeather = {'NoP': .05}

cptAccident = {'1': .1, 
               '0': .3}

cptTrafficJam = {'111': .95,
                 '110': .95,
                 '101': .95,
                 '100': .95,
                 '011': .5,
                 '010': .3,
                 '001': .6,
                 '000': .1}

# i create a list of dictionary following the topological order for dict inserting
cpTables.append(cptRushHour)
cpTables.append(cptBadWeather)
cpTables.append(cptAccident)
cpTables.append(cptTrafficJam)

# print(cpTables)

# here is possible define evidence, key is the variable id, value is 0 (false) or 1 (true)
evidence = {'2':1}

# print(evidence)

# here is possible define query using variable id
query = 3

# number of sample, 1.000 is enough, with 100.000 the result is equale to exact inference 
nSamples = 5000

# call core function for likelihood weighting sampling
LikelihoodWeighting(adjMatrix, cpTables, evidence, query, nSamples)

