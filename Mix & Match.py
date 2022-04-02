'''

You are given three strings s, t and p consisting of lowercase Latin letters. You may perform any number (possibly, zero) operations on these strings.

During each operation you choose any character from p, erase it from p and insert it into string s (you may insert this character anywhere you want: in the beginning of s, in the end or between any two consecutive characters).

For example, if p is aba, and s is de, then the following outcomes are possible (the character we erase from p and insert into s is highlighted):

aba → ba, de → ade;
aba → ba, de → dae;
aba → ba, de → dea;
aba → aa, de → bde;
aba → aa, de → dbe;
aba → aa, de → deb;
aba → ab, de → ade;
aba → ab, de → dae;
aba → ab, de → dea;

Your goal is to perform several (maybe zero) operations so that s becomes equal to t. Please determine whether it is possible.

Note that you have to answer q independent queries.

Input :
The first line contains one integer q (1≤q≤100) — the number of queries. Each query is represented by three consecutive lines.

The first line of each query contains the string s (1≤|s|≤100) consisting of lowercase Latin letters.

The second line of each query contains the string t (1≤|t|≤100) consisting of lowercase Latin letters.

The third line of each query contains the string p (1≤|p|≤100) consisting of lowercase Latin letters.

Output :
For each query print YES if it is possible to make s equal to t, and NO otherwise.

You may print every letter in any case you want (so, for example, the strings yEs, yes, Yes and YES will all be recognized as positive answer).

Example :
input :
4
ab
acxb
cax
a
aaaa
aaabbcc
a
aaaa
aabbcc
ab
baaa
aaaaa

output :
YES
YES
NO
NO 

Note :
In the first test case there is the following sequence of operation:

s= ab, t= acxb, p= cax;
s= acb, t= acxb, p= ax;
s= acxb, t= acxb, p= a. 


In the second test case there is the following sequence of operation:

s= a, t= aaaa, p= aaabbcc;
s= aa, t= aaaa, p= aabbcc;
s= aaa, t= aaaa, p= abbcc;
s= aaaa, t= aaaa, p= bbcc.

'''
s = []
t = []
p = []
n = 0
num =  int(input())
for z in range(num) :
    for i in input() :
        s.append(i)
    for i in input() :
        t.append(i)
    for i in input() :
        p.append(i)        
    if len(s) == len(t) :
       for i in range(len(s)) :
           if s[i] == t[i] :
              n += 1     
       if n == len(s) :
          print('YES')
          n = 0       
       else :
          print('NO')  
          n = 0 
    elif len(s) > len(t) :
         print('NO')
    elif len(s) < len(t) :     
         if len(s) + len(p) < len(t) :
            print('NO') 
         else :
            for i in range(len(s)) :
                for x in range(len(t)) : 
                    if s[i] == t[x] and i <= x :
                       n += 1 
                       t[x] = ' '
                       break
            if n != len(s) :
               print('NO')
               n = 0
            else :
               for i in p :
                   for x in range(len(t)) :
                       if i == t[x] :
                          s.insert(x, i)
                          t[x] = ' '
                          break
               if len(s) == len(t) :
                  print('YES') 
               else :
                  print('NO')  
               n = 0    
    s.clear()
    t.clear()
    p.clear()                                      
