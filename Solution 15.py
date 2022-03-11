'''WAS to enter any number to print following pattern

 1
 2 3
 4 5 6
 7 8 9 10
 11 12 13 14 15
 16 17 18 19 20 21'''
i=6
n=1
for a in range(1,i+1):
    for b in range(1,a+1):
        print(n,end=" ")
        n=n+1
    print()
