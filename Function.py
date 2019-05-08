from random import seed
from random import random

# simple sampling with boolean value
def sampling(trueValue):
    seed()
    value = random()
    # print(value)
    
    if value <= trueValue:
        # return true
        return 1
    else:
        # return false
        return 0

# compute sample weighting
def computWeighting(sample, evidence, adjMatrix, cpTables):

    # define function variable
    value = 0
    key = ''
    weight = 1

    # for every evidence compute the probability conditional on parents based on sampling
    for e in evidence:
        # get evidence value 
        value = evidence.get(e)
        # search for possible evidence parents and create a key for correct cpt tables extraction 
        for i in range(0, len(adjMatrix)):
            if adjMatrix[int(e)][i] == 1:
                key += str(sample[i])
        # if evidence is without parent take true or false value 
        if key == '':
            if value == 1:
                weight *= cpTables[int(e)].get('NoP')
            else:
                weight *= (1 - cpTables[int(e)].get('NoP'))
        # otherwise get correct cpt table row
        else:
            if value == 1:
                weight *= cpTables[int(e)].get(key)
            else: 
                weight *= (1 - cpTables[int(e)].get(key))
        key = ''
        
    return weight

# core function, it create sample with basic sampling, compute weigth and print true and false probability about query 
def LikelihoodWeighting(adjMatrix, cpTables, evidence, query, nSamples):

    # define function variable
    sample = [None]*len(adjMatrix)
    key = ''
    answerWeight = 0
    totalWeight = 0

    # compute the likelihood sampling for all times that required
    while nSamples > 0:
        # for every variable in bayesian network
        for i in range(0, len(adjMatrix)):
            # if a certain variable is a evidence is not necessary sampling, it take it value and go on
            if str(i) in evidence.keys():
                sample[i] = evidence[str(i)]
                continue
            # otherwise create a key for a correct cpt table extraction
            else:
                for j in range(0, len(adjMatrix)):
                    if adjMatrix[i][j] == 1:
                        key += str(sample[j])
            # if the variable is without parents it use 'NoP' value
            if key == '':
                sample[i] = sampling(cpTables[i].get('NoP'))
            else:
                sample[i] = sampling(cpTables[i].get(key))

        # if query variable is true it saves also on numerator
        if sample[query] == 1:
            answerWeight += computWeighting(sample, evidence, adjMatrix, cpTables)

        totalWeight += computWeighting(sample, evidence, adjMatrix, cpTables)

        nSamples -= 1
        key = ''

    # print final probabilities with a good format
    print("{:>19} {:>6}".format("True probability: ", str(round(answerWeight/totalWeight * 100, 1))+'%'))
    print("{:>19} {:>6}".format("False probability: ", str(round((1 - answerWeight/totalWeight) * 100, 1))+ '%'))

