
n = int(input(()))
numbers=[]
Sword=[]

for i in range(n):
    numbers.append(input())

for i in range (n):

    Sword.clear()
    Sword[:0] =str(numbers[i])
    word = ""
    if len(numbers[i])==1:
        if numbers[i]=='9':
            print(11)
            continue
        else:
            print(1+int(numbers[i]))
            continue

    sayac =0
    l=0
    for l in range (len(Sword)):

         if  '9' ==str(Sword[len(Sword) - l - 1]) and len(Sword)!=1:
             Sword[len(Sword) - l - 1] = str('0')
             s=1
             while sayac==0:
                 if str(Sword[len(Sword)-s-l-1]) == '9':
                     Sword[len(Sword)-s-l-1] = str('0')
                     sayac +=1
                     if len(Sword)-1-s==0:
                         Sword.append(str('1'))
                         Sword[0]=str('1')
                         break
                     s += 1
                 else:
                     Sword[len(Sword) - s - l - 1] = str(int(Sword[len(Sword) - s - l - 1] )+1)
                     sayac +=1
                     break
             continue
         else:
             if sayac>0:
                 break

             Sword[len(Sword) - l - 1] = str(int(str(Sword[len(Sword) - l - 1]))+1)
             break

    j = 2
    for p in range (int(len(Sword)/2)):
        j = 2
        if int(Sword[p]) < int(Sword[len(Sword) - 1 - p]):
            Sword[len(Sword) - 1 - p] = Sword[p]
            while j >= 2:
                if 10 == int(Sword[len(Sword) - j - p]) + 1:
                     Sword[len(Sword) - j - p] = str('0')
                     j+=1
                else:
                     Sword[len(Sword) - j - p] =str(int(Sword[len(Sword) - j - p]) + 1)
                     break
        if int(Sword[p]) > int(Sword[len(Sword) - 1 - p]):
            Sword[len(Sword) - 1 - p] = Sword[p]
    o=0
    for o in range (len(Sword)):
        if str(Sword[0])=='0':
            del Sword[0]
            del Sword[len(Sword)-1]
            continue
        break
    word = ""
    for k in range(len(Sword)):
        word += str(Sword[k])
    numbers[i] = word
    print(numbers[i])
