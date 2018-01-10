# EENG450 - SEED
# Author: Robert Schreibman
# Exercise 1: Intro to Arduino and Raspberry Pi

##################################################################

import numpy as np

# Open File
with open('datafile.txt','r') as f:         
    b = eval(f.read())
f.close

##################################################################

'''iterates through data and finds largest and smallest values'''
biggest = b[0];
smallest = b[0];
for i in b:                                      
    if i > biggest:
        biggest = i
    if i < smallest:
        smallest = i

print "a) Maximum:", biggest
print "b) Minimum:", smallest
print "c) 33 is Indexed at:", b.index(33)

##################################################################

'''Uses a List Comprehension to find number of times each
value is repeated, then puts it into a set (deletes duplicates),
then iterates through set and keeps values that repeated'''
numOfOccur = [ (x,b.count(x)) for x in b]
unique = set(numOfOccur)

print "d) Repeated Numbers:\n", [ (x,y) for (x,y) in unique if y != 1]


# Lists the value that repeated the most and its repetition count
'''
maxOccur = max([b.count(x) for x in b])
numOfOccur = [ (x,b.count(x)) for x in b]
unique = set( [ (x,y) for (x,y) in numOfOccur if y == maxOccur] )
print unique
'''

##################################################################

'''Created Sorting function (uses quicksort)'''
def quicklySortThis(a):
    if len(a) <= 1:
        return a
    L = []
    E = []
    G = []
    select = a[0]
    for i in a:
        if i < select:
            L.append(i)
        elif i > select:
            G.append(i)
        elif i == select:
            E.append(i)
    return quicklySortThis(L) + E + quicklySortThis(G)

'''Converted to a numpy array and sorted it'''
a = np.array(b)
Sorted = quicklySortThis(a)

print "e) Sorted List:\n", Sorted

##################################################################

'''Finds all values that are even then uses sorting algorithm'''
even = [x for x in b if x%2 == 0]
evenSorted = quicklySortThis(even)

print "f) Even & in order:\n", evenSorted












