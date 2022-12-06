# Statement are used to make decisions or for selections etc.
required_age_at_school=5
hamid_age= int(input("What is your age"))

# question : can hamid go to school

# use of if ,elif and else
if hamid_age==required_age_at_school:
    print("Congratulations! you are admitted to school ")
# we can adda ny number of elif its basically other than if else statement for some specific reasons or values output
elif hamid_age==2:
    print("Babies just need to play! ")
elif hamid_age==20:
    print("You should be in university ! ")
elif hamid_age > required_age_at_school:
    print("You are over age you should join secondary school")

else:
    print("Sorry! you are under age ")

# Imp point: order of statment is also matter in python as it is inteprator based progeamming language whoch execute code line by line

