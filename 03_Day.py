# List
fruit = ['Apple', 'Banana', 'Mango', 'Grapes'] 
print(fruit)
print(fruit[1])
fruit[1] = 'Cake'
print(fruit)
# Tuple
index = (1.2, 3.2, 3.3)
print(index)
print(index[1])
# Set
food_set = {'Baryani', 'Dall', 'Chiken'}
print(food_set)
food_set.add('Dehi')
print(food_set)
# Dictionary
Cars = {'Brande':'Toyota', 'Model':'GLI', 'Year':'2020'}
print(Cars)
Cars['Year'] = 2023
print(Cars)
print(Cars['Year'])
# Conditional Statements :
# For
x = 8
if x == 6:
    print('Both are equal')
elif x != 7 :
    print('not equal')
else :
    print('none')  
# For Loop :
fruits = ['Banana', 'Apple', 'Mango', 'Graps', 'Orange']
for i in fruits:
    print(i)

# While loop :
x = 1
while x < 100:
    print(x)
    x = x+1

# Break , Continue, Pass:
for i in 'Pakistan':
    if i == 'i':
        break
    print(i)

for x in 'Indonatia':
    if x == 't':
        continue
    print(x)


for y in 'AnasKhan':
    if y == 'K':
        pass
    print(y)


# Nested for loop :
#country = ['Pakistan', 'India', 'China']
#index = [1, 2, 3]
#for j in index:
 #   for i in country:
  #      print(i, j) 
       # print(j)            
# Nested while loop :
x = 1
while x < 10:
    y = 1
    while y < 10 :
        print(x, y)
        y = y+2
    x = x+2

# for loop in while :
x = 1
while x < 5 :
    for y in range (4):
        print(x, y)
    x += 1        

# While in for loop :
x = 8
for x in range(1):
    while y < 5 :
        print(x, y)
    x = x+1    
