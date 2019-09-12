import this

message = "Hello Python Crash Course reader!"
print(message)

print("---------------------------")

name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print("name.upper() : ", name.upper())
print("name.lower() : ", name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

print(f"Hello, {full_name.title()}!")
print("full_name : ",full_name)

print("Languages:\n\tPython\n\tC\n\tJavaScript")


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print('bicycles[1] : ', bicycles[1])
print('bicycles[3] : ', bicycles[3])
print('bicycles[-1] : ', bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}."

print(message)


motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

#Numerical Comparisons
answer = 17
if answer != 42:
	print("That is not the correct answer. Please try again!")

#Checking Whether a Value Is Not in a List
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(f"{user.title()}, you can post a response if you wish.")


#Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
                         'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have {requested_topping}.")


print("\nFinished making your pizza!")



alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
# This must be a fast alien.
	x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")



favorite_languages = {
   'jen': 'python',
   'sarah': 'c',
   'edward': 'ruby',
   'phil': 'python',
   }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

#Looping Through All the Keys in a Dictionary
for name in favorite_languages.keys():
	print(name.title())

#Using get() to Access Values
alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)


#Looping Through All Key-Value Pairs
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
}

for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")



# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
	print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

