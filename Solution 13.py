'''WAS to enter any number to print following pattern

 *****
  ****
   ***
    **
     * '''
n=int(input("enter any number"))
i = 1
while i <= n :
      j = n
      while j >= i:
         print("*", end=" ")
         j = j - 1
      print()
      i = i + 1
