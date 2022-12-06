# highly used in python

# python have while loops and for loops

# while loops

x=0
while(x<=5):   #will print upto 5 
    print(x)
    x=x+1  #we havw to add one so we can increment value to process loop othwrwise it will only print 1111 or 0000
# Imp Point : indexing in prorammming is start with 0.


# for loops
for x in range(5,10):
    print(x)

# Imp Point:
# difference between for and while loop
# for loop:in for loop the number of iterations to be done is already known and is used to obtain a certain result whereas 
# while loop:in while loop the command runs until a certain condition is reached and the statement is proved to be false.

# application for for loops
week=["Monday","Tuesday","Wednesday","Thusday","Friday","Sunday"]
for d in week:
    # if d=="Wednesday":break  #loop stops
    if d=="Wednesday":continue   #loop skip that value
    print(d)

# Imp point
# break:to stop the loop at specific point
# continue: to skip value from loop
