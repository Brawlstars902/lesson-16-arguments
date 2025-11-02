def tc(b,p):
    t=b*(1+0.01*p)
    t=round(t,2)
    print('The total money is $',t)

b=float(input('Please enter the bill price  :'))
p=float(input('Please enter the tip percentage  :'))

tc(b,p)