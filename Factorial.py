def c(x):
    if x==0 or x==1:
        return 1
    else:
        return x*c(x-1)


x=int(input('Please enter the number of which you would like to find its factorial:  '))

print('The factorial of',x,'is',c(x))