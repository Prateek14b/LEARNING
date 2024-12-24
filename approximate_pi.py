# Authors   : Prateek Basavaraj, Tanvi Soni
# Emails    : pbasavaraj@umass.edu, tsoni@umass.edu
# Spire IDs : 34743797, 34558092

def piapproximate(n):
    sum=0
    i=1 #looping variable

    while i<=n:
        sum=sum+(1/(i**2))
        i=i+1

    print(f'sum = {sum}')
    approxval=((6*sum)**0.5)
    print(f'approximate value of pi is: {approxval}')

