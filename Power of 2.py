'''

You are given an integer N. In 1 step you can either delete any digit from the given number or include a digit to the right end of the number to make the given number a power of 2. You can perform the above operations any number of times. Find the minimum number of steps required to convert the given number to a power of 2.

Input Format :
First line of the input contains a single integer T denoting the number of testcases.
Each testcase consists of a single integer N.

Output Format :
Print a single integer for each testcase denoting the number of steps needed for converting the given number N into a power of 2.

Constraints :
1≤T≤1000
1≤N≤109

Sample Input 1 :
2
65
8888

Sample Output 1 :
2
3

Explanation :
For Testcase 1 :

Delete the digit 5 and number will become 6
Then include 4 at the right end of the number then the number will become 64 which is a power of 2

For Testcase 2 :

delete any of the digits 8 three times and result will be 8 which is a power of 2. 

'''
test_num = int(input())
for x in range(test_num) :
   num = []
   for i in input() :
       num.append(i)
   steps = 0
   while True :
         test = ''
         power = 0
         nearest = 0
         for i in range(len(num) - steps):
            test += num[i]
         while True :
               if 2 ** power > nearest and 2 ** power <= int(test) + 5 :
                  nearest = 2 ** power
               else :
                  break
               power += 1
         nearest = str(nearest)
         power = 0
         if int(test) == int(nearest) :
            break
         else :
            for i in range(len(nearest)) :
               if nearest[i] == test[i] :
                  power += 1
            if power == len(nearest) - 1 :
               steps += 2
               break
            elif steps == len(num) :
               steps += 1
               break
            else :
               steps += 1
   print(steps)
