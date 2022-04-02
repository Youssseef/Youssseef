'''
You are given the sequence a1,a2,…,an. You can choose any subset of elements and then reorder them to create a "saw".

The sequence b1,b2,…,bm is called a "saw" if the elements satisfy one of the following series of inequalities: b1 > b2 < b3 > b4 < … or b1 < b2 > b3 < b4 > … 

Find the longest saw which can be obtained from a given array.

Note that both the given sequence a and the required saw b can contain duplicated (non-unique) values.

Input :
The first line contains an integer t (1≤t≤105) — the number of test cases in the input. Then the descriptions of the t test cases follow. Each test case begins with a line containing integer n (1≤n≤2⋅105). Then a line containing n integers a1,a2,…,an (1≤ai≤109) follows.

It's guaranteed that ∑n doesn't exceed 2⋅105.

Output :
For each test case, print two lines: print the length of the longest saw in the first line, and the saw itself in the second line. If there are several solutions, print any of them.

Example :-
input :
3
10
10 9 8 7 6 5 4 3 2 1
7
1 2 2 2 3 2 2
3
100 100 100

output :
10
1 6 2 7 3 8 4 9 5 10 
4
2 1 3 2 
1
100 
'''
test_cases = int(input())
for i in range(test_cases) :
    nums = []
    counter = input()
    for i in input().split() :
        nums.append(int(i))
    counter = {i:nums.count(i) for i in nums}
    z = [list(i) for i in counter.items()]
    y = []
    test ,t2 ,counter= 0 ,0 ,0
    for i in z :
        i = i.reverse()
    z.sort()
    z.reverse()
    if len(z) > 1 :
        for i in range(len(z)) :
            if z[i][0] > 1 :
                t2 += z[i][0]
            else :
                counter += z[i][0]
        if t2 > counter and t2 > 1 :  
            t2 ,counter = 0 ,0     
            for i in range(len(z)) :
                if z[i][0] == 1 :
                    z[0][0] -= z[i][0]
                    z[i][0] = 0 
                    t2 += 1      
            while True :      
                  if z[test][0] > 0 and t2 != len(z) - 1:
                        for i in range(1,len(z)) :
                            if z[i][0] != 0 :
                              if z[test][0] - z[i][0] >= 0 :
                                  z[test][0] = z[test][0] - z[i][0]
                                  z[i][0] = 0
                                  t2 += 1
                              elif z[test][0] != 0 and z[test][0] - z[i][0] < 0 :
                                    z[i][0] -= z[test][0]
                                    z[test][0] = 0
                            if z[test][0] == 0 :
                              test += 1 
                              break
                  else :
                      break              
            for i in range(len(z)) : 
                if z[i][0] != 0 :
                    for x in range(z[i][0]) :
                        counter = z[i][1]
                        nums.remove(z[i][1])
        else :                
            t2 ,counter = 0 ,0      
        nums.sort()
        z.clear()
        for i ,x in zip(nums[:len(nums)//2] ,nums[len(nums)//2:]) :
            z.append(i)
            z.append(x)
        for i ,x in zip(nums[:len(nums)//2] ,nums[len(nums)//2:]) :
            y.append(x)
            y.append(i)
        if len(nums) % 2 != 0 :
            t2 += 1  
            z.append(nums[len(nums) - 1])
            y.append(nums[len(nums) - 1])    
        if counter != 0 and counter > z[len(z) - 1] and t2 == 1:
            z.append(counter) 
        elif counter != 0 and counter < z[len(z) - 1] and t2 == 0 :
              z.append(counter)
        if counter != 0 and counter < y[len(y) - 1] and t2 == 1 :  
            y.append(counter)  
        elif counter != 0 and counter > y[len(y) - 1] and t2 == 0 :
            y.append(counter)
        t2 = 2 
        for i in range(1,len(z) - 1):
            if (z[i - 1] > z[i] and z[i] < z[i + 1]) or (z[i - 1] < z[i] and z[i] > z[i + 1]) :
                test += 1
        if test != len(z) - 2 :
            z.clear()
            t2 -= 1  
        test = 0   
        for i in range(1,len(y) - 1):
            if (y[i - 1] > y[i] and y[i] < y[i + 1]) or (y[i - 1] < y[i] and y[i] > y[i + 1]) :
                test += 1
        if test != len(y) - 2 :
            y.clear()
            t2 -= 1
        nums.clear()  
        if t2 == 2 : 
            print(len(y))
            print(" ".join(str(x) for x in y))
            z.clear()
            y.clear()
        elif t2 == 1 and len(z) == 0 :
              print(len(y))
              print(" ".join(str(x) for x in y))
              y.clear()
        elif t2 == 1 and len(y) == 0 :
              print(len(z))
              print(" ".join(str(x) for x in z))  
              z.clear()
    else :
        print(1)
        print(nums[0])    
        nums.clear() 
