#  for reusbailty of code make code easy 

# # print is also a function
# print("hi i am Muhammad Sxhahzeb")
# print("hi i am Muhammad Shxahzeb")
# print("hi i am Muhammad Shxahzeb")
# print("hi i am Muhammad 2 xShahzeb")
# print("hi i am Muhammad Shxahzeb")
# print("hi i am Muhammad Shxahzeb")
# if we want to print a line several times we will write it again and again and if ,mistakes happen any where we have to chnage it accordingly it maeks working hectic 
# so to avoid this we use function than we only have to change something in function and it will chnage in whole code


# method 1 defining function
# def name():
#     print("hi i am Muhammad Shahzeb")
#     print("hi i am Muhammad Shahzeb")
#     print("hi i am Muhammad Shahzeb")

# name()

# method 2
# def name():
#     text="hi i am Muhammad Shahzeb from FUSST"
#     print(text)
#     print(text)
#     print(text)

# name()

# method 3
# def name(text):
#     print(text)
#     print(text)
#     print(text)

# name("HI im Shaibi")


# defining a function with if,else,elif

def school_age_calc(age):
    if age==5:
        print("Congratulations! you are admitted to school ")
    elif age==2:
        print("Babies just need to play! ")
    elif age >5:
        print("You are over age you should join secondary school")
    else:
        print("Sorry! you are under age ")

# we just need to enter age as a passing parameter to call age calclation function
school_age_calc(23)
school_age_calc(2)
school_age_calc(5)

def future_age(age):
    new_age=age+10
    return new_age
    print(new_age)

age_predictor=future_age(33)
print(age_predictor)