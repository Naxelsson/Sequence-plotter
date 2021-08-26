# https://math.stackexchange.com/questions/3333684/computing-remy-sigrist-sequence-a279125
# First we create a list full of zeroes. This list is used to store the bits which associate a number to a group
# (e.g. all numbers whose sequence value is 1). Each number is iterated through from 0−n in order and the program finds
# which value/group the number is associated to by using a bitwise AND (& in Python).
# When it has done so (the bitwise AND returns zero/False), this number is added to the same position in the list in order
# to store the bit pattern of this number. Then, to check if future numbers are within this group,
# the operation of bitwise AND will cause any number containing these bits to be identified
# (bitwise AND does not return zero/False in this case). The value of the number in the sequence is then yielded.


import matplotlib.pyplot as plt

def remy(n): # see https://math.stackexchange.com/questions/3333684/computing-remy-sigrist-sequence-a279125
    terms=[0]*n     
    for i in range(n+1):
        a=0
        while terms[a]&i:
            a+=1
        terms[a]+=i
        yield a

n = 10000   
xAxis = []           # creates the x-axis
for k in range(n+1):
    xAxis.append(k)
    
lst = []            # gets the values from the remy(n)-function
for i in remy(n):
    lst.append(i)

plt.scatter(xAxis, lst, s = 1, color='black', marker='.')
plt.xlabel('n')
plt.ylabel('A279125(n)')
plt.title('Sequence A279125 in the OEIS by Rémy Sigrist')
plt.show()

