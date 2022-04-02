struc = []
for i in input('enter the the series of numbers separated by space : \n\n').split() :
    struc.append(int(i))
snackes = []
mixed = []
n ,k ,begin = 0 ,0 ,0
for i in range(len(struc)) :
    if len(str(struc[i])) > 1 :
        mixed.append(struc[i])
        struc[i] = 'a'
try :
    for i in range(len(struc)) :
        snackes.append([])
        for j in range(i+1) :
            snackes[i].extend(str(struc[n]))
            n += 1
except :
    n = 0  
for i in range(len(snackes)-1,-1,-1) :
    if len(snackes[i]) == 0 :
       snackes.remove(snackes[i])
for i in snackes[:len(snackes)] :
    for x in range(len(i)) :
        if len(snackes[len(snackes) - 2]) == len(snackes[len(snackes) - 1]) - 1 :
           break 
        snackes[len(snackes)-1].append(i[x])
        i[x] = None
    if len(snackes[len(snackes) - 1]) == len(snackes[len(snackes) - 1]) - 1 :
       break 
for i in snackes :
    for x in range(len(i)-1,-1,-1) :
        if i[x] == None :
           i.remove(i[x])
for i in range(len(snackes)-1,-1,-1) :
    if len(snackes[i]) == 0:
       snackes.remove(snackes[i])        
while True :
      for i in range(len(snackes)-1) :
          if len(snackes[i]) == len(snackes[i+1])-1 :
             n += 1
      if n != len(snackes) -1 :
         n = 0
         snackes.append([])
         for i in snackes[:len(snackes)] :
             for x in range(len(i)) :
                 if len(snackes[len(snackes) - 2]) == len(snackes[len(snackes) - 1]) - 1 :
                    break 
                 snackes[len(snackes)-1].append(i[x])
                 i[x] = None
             if len(snackes[len(snackes) - 2]) == len(snackes[len(snackes) - 1]) - 1 :
                break 
         for i in snackes :
             for x in range(len(i)-1,-1,-1) :
                 if i[x] == None :
                    i.remove(i[x])
         for i in range(len(snackes)-1,-1,-1) :
             if len(snackes[i]) == 0:
                snackes.remove(snackes[i])
      else :
             k = n
             n = 0
             break
begin = len(snackes[0])
for i in range(len(struc)) :
    if struc[i] == 'a' :
        struc[i] = mixed[n]
        n += 1     
n = k + 1
struc.sort()
struc.reverse()
try :
    while True :
          for x in range(n) :
              for j in range(k) :
                  print(end = ' ')
              k -= 1
              for i in range(begin) :
                  print(struc[i], end = '  ')
              print ('\r')
              for i in range(begin) :
                  struc.remove(struc[0])
              begin += 1
except :   
    begin = 0
