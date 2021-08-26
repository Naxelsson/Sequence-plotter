
import matplotlib.pyplot as plt

def remy(n): # see https://math.stackexchange.com/questions/3333684/computing-remy-sigrist-sequence-a279125 for details
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

