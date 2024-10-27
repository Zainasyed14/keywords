num=int(input("Enter your number : "))
for i in range(1,num+1):
    if(i%20==0):
        print("Twist")
        continue
    elif(i%15==0):
        pass
    elif(i%5==0):
        print("fizz")
    elif(i%3==0):
        print("buzz")
    else:
        print(i)