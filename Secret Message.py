'''

Andrey received a postcard from Irina. It contained only the words "Hello, Andrey!", and a strange string consisting of lowercase Latin letters, snowflakes and candy canes. Andrey thought that this string is an encrypted message, and decided to decrypt it.

Andrey noticed that snowflakes and candy canes always stand after the letters, so he supposed that the message was encrypted as follows. Candy cane means that the letter before it can be removed, or can be left. A snowflake means that the letter before it can be removed, left, or repeated several times.

For example, consider the following string:

                     h w ? a p * y n ? e w w * y e * a r

This string can encode the message «happynewyear». For this, candy canes and snowflakes should be used as follows:

candy cane 1: remove the letter w,
snowflake 1: repeat the letter p twice,
candy cane 2: leave the letter n,
snowflake 2: remove the letter w,
snowflake 3: leave the letter e.

Please note that the same string can encode different messages. For example, the string above can encode «hayewyar», «happpppynewwwwwyear», and other messages.

Andrey knows that messages from Irina usually have a length of k letters. Help him to find out if a given string can encode a message of k letters, and if so, give an example of such a message.

Input
The first line contains the string received in the postcard. The string consists only of lowercase Latin letters, as well as the characters «*» and «?», meaning snowflake and candy cone, respectively. These characters can only appear immediately after the letter. The length of the string does not exceed 200.

The second line contains an integer number k (1≤k≤200), the required message length.

Output
Print any message of length k that the given string can encode, or «Impossible» if such a message does not exist.

Examples :-

input :

hw?ap*yn?eww*ye*ar
12

output :

happynewyear

**************************

input :

ab?a
2

output :

aa

**************************

input :

ab?a
3

output :

aba

**************************

input :

ababb
5

output :

ababb

**************************

input :

ab?a
1

output :

Impossible

'''
word = []
for i in input() :
    word.append(i)
size = int(input())
n1 = 0
n2 = 0
z = 0
for i in range(-1,-len(word) - 1,-1) :
    if word[i] == '?' :
       n1 += 1
 
    elif word[i] == '*' :
         n2 += 1
if len(word) - 2*(n1 + n2) > size or (len(word) < size and n1 == 0 and n2 == 0) or ((size > len(word) - n1) and n2 == 0):
   print('Impossible')
elif n1 == 0 and n2 == 0 :
     for i in word : 
         print(i ,end = '')                                                
else:   
   if (len(word) - z) - (n1 + n2) > size :
      for i in range(len(word)) :
          if (len(word) - z) - (n1 + n2) > size :
             if word[i] == '?' :
                word[i] = []
                word[i-1] = []
                z += 2
                n1 -= 1
   if (len(word) - z) - (n1 + n2) > size : 
      for i in range(len(word)) :
          if (len(word) - z) - (n1 + n2) > size :
             if word[i] == '*' :
                word[i] = []
                word[i-1] = []
                z += 2
                n2 -= 1
   if (len(word) - z) - (n1 + n2) == size : 
      None        
   else :                   
      if len(word) - (n1 + n2) < size : 
         for i in range(-1,-len(word) - 1,-1) :
             if (len(word) - z) - (n1 + n2) < size :
                if word[i] == '*' :
                   word[i] = word[i - 1]
                   n2 -= 1
                   while len(word) - (n1 + n2) < size :
                         word.insert(i, word[i]) 
   for i in reversed(word) :
       if i == '?' or i == '*' or i == [] :
          word.remove(i)                   
   for i in word :
       print(i ,end = '')   
       
