#1
def printer():
    # Print "Hello, World!" to console
    print("Hello, World!")

# Call the printer function
printer()

#2

# Parameterized
def func(text):
    print(text)
func("hello world")

#3
def school_age(text,age):
    if age==5:
        print(text,"Your school studnet")
    elif age>5:
        print(text,"your a college student")
    else:
        print(text,"you are still in elementary school")
school_age("Hello Dear !, ",15)

#4
def pridicted_age(age):
    new_age=20+age
    print(new_age)
pridicted_age(10)



