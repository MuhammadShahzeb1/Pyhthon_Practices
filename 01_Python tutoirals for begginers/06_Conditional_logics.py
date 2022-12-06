# logical operators are either "yes" or "no", "true" or "false" or "0 or 1"
# eequal to                     ==
# not equal to                  !=
# less than                     <
# greater than                  >
# less than and eqaul to        <=
# greater than and equal to     >=

# is 4 equal to 4
print(4==4)  #will print true or false based on condtion  ||true
# is 4 greater than and equal to 6
print(4>=6)  #        ||false
# 4 is not equal to 4
print(4!=4)  #       ||false


## application of logical operators
# hamid_age=12
# age_at_school=5
# print(hamid_age>=age_at_school)

# input function and logical operator together
hamid_age=int(input("what is your age? "))   #putting age into integer function so we can compare it with school age ...we cn only compare variables of same data types 
age_at_school=5
print(hamid_age>=age_at_school)
