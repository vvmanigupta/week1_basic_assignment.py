# Taking the input from User separated by commas
# splitting the input by comma
userinput=input().split(",")
# assigning the  strings to variables 
name="Name: "
age="Age: "
color="Color: "
# For for loop we create count variable
count=0
# iterating the for loop in user input by increasing count variable 
# using if conditions combining the string and user input 
for i in userinput:
    if count==0:
        # printing the output by combining the strings
        print(name+i)
    if count==1:
        print(age+i)
    if count==2:
        print(color+i)
        # increasing the count variable for every iteration
    count+=1
        
        
        



