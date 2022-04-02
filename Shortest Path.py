'''

Consider a two dimensional array of numbers comprehended between 0 and 9(as shown below). The Matrix can be traversed following any orthogonal direction (i.e., north, south, east and west). Considering that each cell represents a cost, Your task is to find the minimum cost value to go from the top-left corner to the bottom-right corner of a given number array of size NxM where 1 <= N, M <= 999. Note that the solution for the given example is 24.


		0	3	1	2	9

		7	3	4	9	9

		1	7	5	5	3

		2	3	4	2	5


Input :
The input contains several Test cases. Each test case is defined by: one line with the number of rows, N; one line with the number of columns, M; and N lines, one per each row of the Matrix, containing the numbers separated by spaces. Terminate the input with (no. of rows)N=0.

Output :
For each maze, output one line with the required minimum value.

Example
Input:
4
5
0 3 1 2 9
7 3 4 9 9
1 7 5 5 3
2 3 4 2 5
1
6
0 1 2 3 4 5
0

Output:
24
15

'''
try :
    while True :
          rows = int(input())
          coulms = int(input())
          road = []
          for i in range(rows) :
              road.append([])
              for c in input().split() :
                  road[i].append(int(c))  
          shortest = []
          t1 ,t2 ,t3 ,t4 = [] ,[] ,[] ,[]
          r ,c = 0, 0
          if rows != 1 and coulms != 1 :
             shortest.append(road[r][c])
             shortest.append(road[rows - 1][coulms - 1])
             road[rows - 1][coulms - 1] = 0
          while True :
                if rows == 1 or coulms == 1 :
                   break  
                if r == 0 and c == coulms - 1 :
                   shortest.append(road[r + 1][c])
                   r += 1
                elif r == rows - 1 and c == 0 :
                     shortest.append(road[r][c + 1])
                     c += 1
                elif (r == rows - 2 and c == coulms - 1) or (r == rows - 1 and c == coulms - 2) :
                     break
                elif r == 0 or c == 0 or r == rows - 1 or c == coulms - 1 :
                     if r == rows - 1 :
                        if road[r - 1][c] == 10^4 :
                           shortest.append(road[r][c + 1]) 
                           break
                        else :   
                           c += 1
                           t1.append(road[r][c] + road[r][c + 1])
                           t1.append(road[r][c] + road[r - 1][c])
                           c -= 1
                           r -= 1
                           t2.append(road[r][c] + road[r][c + 1])
                           t2.append(road[r][c] + road[r - 1][c])
                           t2.append(road[r][c] + road[r][c - 1])
                           r += 1
                     elif r == 0 : 
                          if c == 0 : 
                             c += 1
                             t1.append(road[r][c] + road[r][c + 1])
                             t1.append(road[r][c] + road[r + 1][c])
                             c -= 1       
                             r += 1
                             t2.append(road[r][c] + road[r][c + 1])
                             t2.append(road[r][c] + road[r + 1][c])
                             r -= 1
                          elif road[r + 1][c] == 10^4 :
                               shortest.append(road[r][c + 1]) 
                               break  
                          else :
                             c += 1
                             t1.append(road[r][c] + road[r][c + 1])
                             t1.append(road[r][c] + road[r + 1][c])
                             c -= 1       
                             r += 1
                             t2.append(road[r][c] + road[r][c + 1])
                             t2.append(road[r][c] + road[r + 1][c])
                             t2.append(road[r][c] + road[r][c - 1])
                             r -= 1
                     elif c == 0 :
                          if road[r][c + 1] == 10^4 :
                             shortest.append(road[r + 1][c])
                             break
                          else :   
                             c += 1
                             t1.append(road[r][c] + road[r][c + 1])
                             t1.append(road[r][c] + road[r + 1][c])
                             t1.append(road[r][c] + road[r - 1][c])
                             c -= 1       
                             r += 1
                             t2.append(road[r][c] + road[r][c + 1])
                             t2.append(road[r][c] + road[r + 1][c])
                             r -= 1
                     else :
                          if road[r][c - 1] == 10^4 :
                             shortest.append(road[r + 1][c])
                             break
                          else :   
                             c -= 1
                             t1.append(road[r][c] + road[r][c - 1])
                             t1.append(road[r][c] + road[r + 1][c])
                             t1.append(road[r][c] + road[r - 1][c])
                             c += 1       
                             r += 1
                             t2.append(road[r][c] + road[r][c - 1])
                             t2.append(road[r][c] + road[r + 1][c])
                             r -= 1     
                     if min(t1) < min(t2) :
                        c += 1
                        shortest.append(road[r][c])
                        road[r][c] = 10^4
                     else :
                          r += 1
                          shortest.append(road[r][c]) 
                          road[r][c] = 10^4  
                     t1.clear()
                     t2.clear() 
                elif r == 1 and c == 1 :
                     c += 1
                     t1.append(road[r][c] + road[r][c + 1])
                     t1.append(road[r][c] + road[r - 1][c])
                     t1.append(road[r][c] + road[r + 1][c])
                     c -= 1
                     r += 1
                     t2.append(road[r][c] + road[r][c + 1])
                     t2.append(road[r][c] + road[r + 1][c])
                     t2.append(road[r][c] + road[r][c - 1])
                     r -= 1
                     c -= 1
                     t3.append(road[r][c] + road[r - 1][c])
                     t3.append(road[r][c] + road[r + 1][c])
                     c += 1
                     r -= 1
                     t4.append(road[r][c] + road[r][c + 1])
                     t4.append(road[r][c] + road[r][c - 1])
                     r += 1
                     if min(t1) < min(t2) and min(t1) < min(t3) and min(t1) < min(t4):
                        c += 1
                        shortest.append(road[r][c])
                        road[r][c] = 10^4
                     elif min(t2) < min(t1) and min(t2) < min(t3) and min(t2) < min(t4):
                          r += 1
                          shortest.append(road[r][c]) 
                          road[r][c] = 10^4  
                     elif min(t3) < min(t1) and min(t3) < min(t2) and min(t3) < min(t4):
                          c -= 1
                          shortest.append(road[r][c]) 
                          road[r][c] = 10^4
                     elif min(t4) < min(t1) and min(t4) < min(t3) and min(t4) < min(t2):
                          r -= 1
                          shortest.append(road[r][c]) 
                          road[r][c] = 10^4              
                     t1.clear()
                     t2.clear()
                     t3.clear()
                     t4.clear() 
                elif r == 1 and c == coulms - 2 :
                     c += 1
                     t1.append(road[r][c] + road[r - 1][c])
                     t1.append(road[r][c] + road[r + 1][c])
                     c -= 1
                     r += 1
                     t2.append(road[r][c] + road[r][c + 1])
                     t2.append(road[r][c] + road[r + 1][c])
                     t2.append(road[r][c] + road[r][c - 1])
                     r -= 1
                     c -= 1
                     t3.append(road[r][c] + road[r - 1][c])
                     t3.append(road[r][c] + road[r + 1][c])
                     t3.append(road[r][c] + road[r][c - 1])
                     c += 1
                     r -= 1
                     t4.append(road[r][c] + road[r][c + 1])
                     t4.append(road[r][c] + road[r][c - 1])
                     r += 1
                     if min(t1) < min(t2) and min(t1) < min(t3) and min(t1) < min(t4):
                        c += 1
                        shortest.append(road[r][c])
                        road[r][c] = 10^4
                     elif min(t2) < min(t1) and min(t2) < min(t3) and min(t2) < min(t4):
                          r += 1
                          shortest.append(road[r][c]) 
                          road[r][c] = 10^4  
                     elif min(t3) < min(t1) and min(t3) < min(t2) and min(t3) < min(t4):
                          c -= 1
                          shortest.append(road[r][c]) 
                          road[r][c] = 10^4
                     elif min(t4) < min(t1) and min(t4) < min(t3) and min(t4) < min(t2):
                          r -= 1
                          shortest.append(road[r][c]) 
                          road[r][c] = 10^4              
                     t1.clear()
                     t2.clear()
                     t3.clear()
                     t4.clear()  
                elif r == rows - 2 and c == coulms - 2 :
                     c += 1
                     t1.append(road[r][c] + road[r - 1][c])
                     t1.append(road[r][c] + road[r + 1][c])
                     c -= 1
                     r += 1
                     t2.append(road[r][c] + road[r][c + 1])
                     t2.append(road[r][c] + road[r][c - 1])
                     r -= 1
                     c -= 1
                     t3.append(road[r][c] + road[r - 1][c])
                     t3.append(road[r][c] + road[r + 1][c])
                     t3.append(road[r][c] + road[r][c - 1])
                     c += 1
                     r -= 1
                     t4.append(road[r][c] + road[r][c + 1])
                     t4.append(road[r][c] + road[r][c - 1])
                     t4.append(road[r][c] + road[r - 1][c])
                     r += 1
                     if min(t1) < min(t2) and min(t1) < min(t3) and min(t1) < min(t4):
                        c += 1
                        shortest.append(road[r][c])
                        road[r][c] = 10^4
                     elif min(t2) < min(t1) and min(t2) < min(t3) and min(t2) < min(t4):
                          r += 1
                          shortest.append(road[r][c]) 
                          road[r][c] = 10^4  
                     elif min(t3) < min(t1) and min(t3) < min(t2) and min(t3) < min(t4):
                          c -= 1
                          shortest.append(road[r][c]) 
                          road[r][c] = 10^4
                     elif min(t1) and min(t4) < min(t3) and min(t4) < min(t2):
                          r -= 1
                          shortest.append(road[r][c]) 
                          road[r][c] = 10^4              
                     t1.clear()
                     t2.clear()
                     t3.clear()
                     t4.clear() 
                elif r == rows - 2 and c == 1 :
                     c += 1
                     t1.append(road[r][c] + road[r - 1][c])
                     t1.append(road[r][c] + road[r + 1][c])
                     t1.append(road[r][c] + road[r][c + 1])
                     c -= 1
                     r += 1
                     t2.append(road[r][c] + road[r][c + 1])
                     t2.append(road[r][c] + road[r][c - 1])
                     r -= 1
                     c -= 1
                     t3.append(road[r][c] + road[r - 1][c])
                     t3.append(road[r][c] + road[r + 1][c])
                     c += 1
                     r -= 1
                     t4.append(road[r][c] + road[r][c + 1])
                     t4.append(road[r][c] + road[r][c - 1])
                     t4.append(road[r][c] + road[r - 1][c])
                     r += 1
                     if min(t1) < min(t2) and min(t1) < min(t3) and min(t1) < min(t4):
                        c += 1
                        shortest.append(road[r][c])
                        road[r][c] = 10^4
                     elif min(t2) < min(t1) and min(t2) < min(t3) and min(t2) < min(t4):
                          r += 1
                          shortest.append(road[r][c]) 
                          road[r][c] = 10^4  
                     elif min(t3) < min(t1) and min(t3) < min(t2) and min(t3) < min(t4):
                          c -= 1
                          shortest.append(road[r][c]) 
                          road[r][c] = 10^4
                     elif min(t4) < min(t1) and min(t4) < min(t3) and min(t4) < min(t2):
                          r -= 1
                          shortest.append(road[r][c]) 
                          road[r][c] = 10^4              
                     t1.clear()
                     t2.clear()
                     t3.clear()
                     t4.clear()                          
                elif r == 1 or c == 1 or r == rows - 2 or c == coulms - 2 :
                     if r == rows - 2 :
                        c += 1
                        t1.append(road[r][c] + road[r - 1][c])
                        t1.append(road[r][c] + road[r + 1][c])
                        t1.append(road[r][c] + road[r][c + 1])
                        c -= 1
                        r += 1
                        t2.append(road[r][c] + road[r][c + 1])
                        t2.append(road[r][c] + road[r][c - 1])
                        r -= 1
                        c -= 1
                        t3.append(road[r][c] + road[r - 1][c])
                        t3.append(road[r][c] + road[r + 1][c])
                        t3.append(road[r][c] + road[r][c - 1])
                        c += 1
                        r -= 1
                        t4.append(road[r][c] + road[r][c + 1])
                        t4.append(road[r][c] + road[r][c - 1])
                        t4.append(road[r][c] + road[r - 1][c])
                        r += 1
                     elif r == 1 : 
                          c += 1
                          t1.append(road[r][c] + road[r - 1][c])
                          t1.append(road[r][c] + road[r + 1][c])
                          t1.append(road[r][c] + road[r][c + 1])
                          c -= 1
                          r += 1
                          t2.append(road[r][c] + road[r][c + 1])
                          t2.append(road[r][c] + road[r][c - 1])
                          t2.append(road[r][c] + road[r + 1][c])
                          r -= 1
                          c -= 1
                          t3.append(road[r][c] + road[r - 1][c])
                          t3.append(road[r][c] + road[r + 1][c])
                          t3.append(road[r][c] + road[r][c - 1])
                          c += 1
                          r -= 1
                          t4.append(road[r][c] + road[r][c + 1])
                          t4.append(road[r][c] + road[r][c - 1])
                          r += 1
                     elif c == 1 : 
                          c += 1
                          t1.append(road[r][c] + road[r - 1][c])
                          t1.append(road[r][c] + road[r + 1][c])
                          t1.append(road[r][c] + road[r][c + 1])
                          c -= 1
                          r += 1
                          t2.append(road[r][c] + road[r][c + 1])
                          t2.append(road[r][c] + road[r][c - 1])
                          t2.append(road[r][c] + road[r + 1][c])
                          r -= 1
                          c -= 1
                          t3.append(road[r][c] + road[r - 1][c])
                          t3.append(road[r][c] + road[r + 1][c])                
                          c += 1
                          r -= 1
                          t4.append(road[r][c] + road[r][c + 1])
                          t4.append(road[r][c] + road[r][c - 1])
                          t4.append(road[r][c] + road[r - 1][c])
                          r += 1
                     else : 
                          c += 1
                          t1.append(road[r][c] + road[r - 1][c])
                          t1.append(road[r][c] + road[r + 1][c])
                          c -= 1
                          r += 1
                          t2.append(road[r][c] + road[r][c + 1])
                          t2.append(road[r][c] + road[r][c - 1])
                          t2.append(road[r][c] + road[r + 1][c])
                          r -= 1
                          c -= 1
                          t3.append(road[r][c] + road[r - 1][c])
                          t3.append(road[r][c] + road[r + 1][c]) 
                          t3.append(road[r][c] + road[r][c - 1])               
                          c += 1
                          r -= 1
                          t4.append(road[r][c] + road[r][c + 1])
                          t4.append(road[r][c] + road[r][c - 1])
                          t4.append(road[r][c] + road[r - 1][c])
                          r += 1  
                     if min(t1) < min(t2) and min(t1) < min(t3) and min(t1) < min(t4):
                        c += 1
                        shortest.append(road[r][c])
                        road[r][c] = 10^4
                     elif min(t2) < min(t1) and min(t2) < min(t3) and min(t2) < min(t4):
                          r += 1
                          shortest.append(road[r][c]) 
                          road[r][c] = 10^4  
                     elif min(t3) < min(t1) and min(t3) < min(t2) and min(t3) < min(t4):
                          c -= 1
                          shortest.append(road[r][c]) 
                          road[r][c] = 10^4
                     elif min(t4) < min(t1) and min(t4) < min(t3) and min(t4) < min(t2):
                          r -= 1
                          shortest.append(road[r][c]) 
                          road[r][c] = 10^4              
                     t1.clear()
                     t2.clear()
                     t3.clear()
                     t4.clear()
                else :
                     c += 1
                     t1.append(road[r][c] + road[r - 1][c])
                     t1.append(road[r][c] + road[r + 1][c])
                     t1.append(road[r][c] + road[r][c + 1])
                     c -= 1
                     r += 1
                     t2.append(road[r][c] + road[r][c + 1])
                     t2.append(road[r][c] + road[r][c - 1])
                     t2.append(road[r][c] + road[r + 1][c])
                     r -= 1
                     c -= 1
                     t3.append(road[r][c] + road[r - 1][c])
                     t3.append(road[r][c] + road[r + 1][c]) 
                     t3.append(road[r][c] + road[r][c - 1])               
                     c += 1
                     r -= 1
                     t4.append(road[r][c] + road[r][c + 1])
                     t4.append(road[r][c] + road[r][c - 1])
                     t4.append(road[r][c] + road[r - 1][c])
                     if min(t1) < min(t2) and min(t1) < min(t3) and min(t1) < min(t4):
                        c += 1
                        shortest.append(road[r][c])
                        road[r][c] = 10^4
                     elif min(t2) < min(t1) and min(t2) < min(t3) and min(t2) < min(t4):
                          r += 1
                          shortest.append(road[r][c]) 
                          road[r][c] = 10^4  
                     elif min(t3) < min(t1) and min(t3) < min(t2) and min(t3) < min(t4):
                          c -= 1
                          shortest.append(road[r][c]) 
                          road[r][c] = 10^4
                     elif min(t4) < min(t1) and min(t4) < min(t3) and min(t4) < min(t2):
                          r -= 1
                          shortest.append(road[r][c]) 
                          road[r][c] = 10^4              
                     t1.clear()
                     t2.clear()
                     t3.clear()
                     t4.clear() 
          if len(shortest) == 0 and rows == 1 and coulms != 1 :
             shortest.append(sum(road[0]))  
          elif len(shortest) == 0 and coulms == 1 and rows != 1 :
               for i in road :
                   shortest.append(sum(i)) 
          print(sum(shortest))
except :
    pass
