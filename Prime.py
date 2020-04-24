
x=5
print('What number would you like to start at? Odd numbers only')
x= int(input())

while True:
    prime = True
    y=x-1
    for i in range(3,y):
        z = x % i
        if z == 0:
            prime = False
            break
            #print('false')
        
    if prime == True:
        print(x)

    x += 2
        
print('failed')
input()