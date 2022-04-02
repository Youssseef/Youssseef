'''

Value of an array is defined as the sum of the absolute differences between pairs of consecutive elements in the array. Formally, for a given array A = {A1, A2, A3, ... , An}, value(A) = |A1 - A2| + |A2 - A3| + |A3 - A4| + ... + |An-1 - An|, where |x| means the absolute value of x.

You will be given an array A of n integers and q updates. Each update will have two integers x and y. For this update, you should replace all the occurrences of element x in the array with y and output the value of the new array.

Input :
Input starts with an integer T, denoting the number of test cases.

The first line of each case contains two integers n and q. The next line contains n space separated integers A1, A2, A3, ... , An forming the initial array.

Each of next q lines contains two space-separated integers x and y.

Output :
For each test case, print "Case t:" (without quotes. t is the test case number) in the first line. Then print q lines. The ith line should contain the value of the array after the ith update.

Constraints :
1 ≤ T ≤ 10
1 ≤ n, q ≤ 100000
1 ≤ Ai, x, y ≤ 100000

Example:
Input:
1
5 3
1 2 3 4 5
1 3
3 4
5 1

Output:
Case 1:
4
5
7

Explanation :
After the first update,

A ={3, 2, 3, 4, 5}, Value(A) = |3-2| + |2-3| + |3-4| + |4-5| = 4

After the second update,

A ={4, 2, 4, 4, 5}, Value(A) = |4-2| + |2-4| + |4-4| + |4-5| = 5

After the third update,

A ={4, 2, 4, 4, 1}, Value(A) = |4-2| + |2-4| + |4-4| + |4-1| = 7

'''
array = []
updates = 0
x ,y ,vlaue = 0 ,0 ,0
cases = int(input())
for z in range(cases) :
    print('case {}:'.format(z+1))
    for i in input().split() :
        updates = int(i)
    for i in input().split() :
        array.append(i)    
    for i in range(updates) :
        for c in input().split() :
            array.append(c)
        x = array[len(array) - 2]
        y = array[len(array) - 1]
        array.pop()
        array.pop()
        for c in range(len(array)) :
            if array[c] == x :
               array[c] = y
        for c in range(len(array)-1) :
            vlaue += abs(int(array[c])-int(array[c+1]))    
        print(vlaue) 
        vlaue = 0 
    array.clear() 
