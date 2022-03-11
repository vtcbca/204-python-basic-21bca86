#WAS to enter any number and print from which number from 0 to 9 it is divisible.
n1=1
n2=10
n=int(input("Enter the number to be divided by : "))
for i in range(n1,n2):
    if n%i==0:
        print(i)
