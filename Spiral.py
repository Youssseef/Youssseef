'''
Given an n∗m matrix.

Print all it's elements in spiral order.

See the figure below for more clarification.

Input
The first line contains two integers n,m represent the number of rows and columns of the matrix respectively where (1≤n,m≤103).

The next n lines each line cointain m integers Aij where each element (−1018≤Aij≤1018).

Output
Print the elements of the matrix in spiral order.

Example :-
input :
4 4
 1 2 3 4
12 13 14 5
11 16 15 6
 10 9 8 7

output :

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 

---------------------

1     ➡️    2   ➡️   3   ➡️     4    ⬇️
12    ➡️   13   ➡️  14   ⬇️     5    ⬇️
11    ⬆️   16   ⬅️  15   ⬅️     6    ⬇️
10    ⬆️    9   ⬅️   8   ⬅️     7    ⬅️  

---------------------
'''

spiral = []
for i in input().split() :
    spiral.append(i)
r = int(spiral[0])
c = int(spiral[1])
spiral.clear()
items = []
n = 0
for i in range(r) :
    items.append([])
    for x in input().split() :
        items[n].append(x)
    n += 1
while len(items) != 0 :
      try :
          for i in range(c) :
              spiral.append(items[0][i])
          items.remove(items[0])
          r -= 1
          for i in range(r) :
              spiral.append(items[i][c - 1])
          for i in range(r) :
              items[i].remove(items[i][c - 1]) 
          c -= 1      
          for i in range(-1,-c - 1,-1) :
              spiral.append(items[r - 1][i])
          items.remove(items[r - 1])
          r -= 1
          for i in range(-1,-r - 1,-1) :
              spiral.append(items[i][0])
          for i in range(-1,-r - 1,-1) :
              items[i].remove(items[i][0])
          c -= 1
      except :
          n = 0
for i in spiral :
              print(i ,end = ' ')  
