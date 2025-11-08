n=int(input('Please enter a number which you would like to cube:  '))
def c(n):
    print(n,'cubed is',n*n*n)
    x=n*n*n
    if int(x)%3==0:
        print('The cube of your original number (which =',x,') is divisible by three')
    if int(x)%3!=0:
        print('The cube of your original number (which =',x,') is not divisible by three')
c(n)
if n%3==0:
    print('Your original number (which is =',n,') is divisible by three.')
if n%3!=0:
    print('Your original number (which is =',n,') is not divisible by three.\n\n')