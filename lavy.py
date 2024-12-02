
print("\n\n\t\t-------welcome to profit calculation app------\t\t")

name=input("1.put your name:")
print(name)
job=input("2.identify job you work:")
print(job)
profit=input("3.put profit you get per day:")
print(profit)

while True:
    
    print("choose your option:")
    print("1.30days\n 2.31days\n 3.366days\n4. Break")
    op=input("ente your operation:")
     
    try:
        name= name
        job=job
        profit= float(profit)
        op=int(op)
    except:
        print("it doesn't match")
    
    if(op==1):
        sum= profit * 30
        print(profit, "*", 30, "=", sum)
    elif(op==2):
        sum=profit * 31
        print(profit, "*", 31, "=", sum)
    elif(op==3):
        sum=profit * 366
        print(profit, "*", 366, "=", sum)
    elif(op==4):
        break
    else:
        print("your type doesn't match" )
        break



