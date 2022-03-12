a = [('car',99.99),('bike',0.01),('truck',0.00)]
for i in range(3):
    b ="{0:<10}{1}{2:<}{3}".format(a[i][0],":",a[i][1],"%")
    print(b)