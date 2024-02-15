# While Loops
x=0
while(x<5):
    print(x)
    x+=1
#For Loop

for x in range(5,10):
    print(x)

#array
fruits = ["apple","banana","cherry","watermelon","mango"]
for f in fruits:
    if (f=="watermelon"):break # break including watermelon and above
    if (f=="cherry"):continue # skips cherry
    print(f)


