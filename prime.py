num = int(input("Enter a number: "))

def prime(num):
    cnt = 0
    for i in range(2, num):
        if(num %i  == 0):
            cnt += 1
    if cnt == 0:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
        
prime(num)