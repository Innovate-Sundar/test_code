def fibonaaci(n):
    if n<=1:
        return n
    else:
        return (fibonaaci(n-1)+fibonaaci(n-2))

n=int(input('Enter the Number:'))
print('Fibonaaci Series for the {0} is'.format(n))
for i in range(n):
    print(fibonaaci(i))
