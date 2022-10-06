for num in range (20, 300):
    if all(num%k !=0 for k in range (2,num)):
        print(num)