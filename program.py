from unittest import result
import numpy as np

with open('Wordl/words.txt', 'r') as file:
    words = file.read()
    #words = [word.split(",") for word in words]

words = words.split(',')
#print(len(words))

def funcEntropy(dictionary):
    secretWord = 'skill'

    for word in dictionary:



def rate (word, key):
    result = np.zeros(5) 
    
    for i in range(5):
        if (key[i] == word[i]):
            result[i] = 1
        elif (key[i] in word):
            result[i] = 2 
    
    return result


def entropy(secretWord, key):

