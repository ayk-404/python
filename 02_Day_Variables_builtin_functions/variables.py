
# Variables in Python

first_name = 'Andrey'
last_name = 'Kudryavtsev'
country = 'Germany'
city = 'Berlin'
age = 28
year = 2026
is_married = False
is_true = True
is_light_on = False
skills = ['SQL', 'Python']
person_info = {
    'firstname': 'Andrey',
    'lastname': 'Kudryavtsev',
    'country': 'Germany',
    'city': 'Berlin'
}

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line
like_coffee, favorite_color = True, 'blue'

# Level 2:
print(
    type(first_name),
    type(skills) # ... and so on
)
print(len(first_name), len(last_name))

num_one, num_two = 5, 4

variable_total = num_one + num_two
var_diff = num_one - num_two
var_product = num_one * num_two
var_division = num_one / num_two
var_remainer = num_one % num_two
var_exp = num_one ** num_two
var_floor_division = num_one // num_two 
# calculate radius 
area_of_circle = 3.14 * 30 **2
circum_of_circle = 2 * 3.14 * 30
#radius = input('Enter radius of a circle: ')
#area_of_circle = 3.14 * float(radius) ** 2
print('Area of the circle:', area_of_circle)
# get input from user 
#name = input("What is your name? ")
#country = input("Which country do you live in? ")
#age = input("How old are you? ") 

help('False')


