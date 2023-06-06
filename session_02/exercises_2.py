# Session 2 Exercises

## Section A
# 1. Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable. 
width=5
height=10
area=width*height
# Print out the string: `Rectangle of width <x> and height <y> has an area of <area>`.

print(f'Rectangle of width {width} and height {height} has an area of {area}')

# 2. Write code that prints the length of the string, 'python'.
print(len("python"))


# 3. Print out the first and third letter of the word 'python'.
print("python"[0:3:2])


# 4. Ask the user to enter their name, and print out `Hello, <name>`.
name=input("enter your name: ")
print(f'Hello, {name}')


# 5. Ask the user to enter their age, tell them how old they will be in 15 years time.
age = int(input("please enter your age: "))
print(f'in 15 years time you will be {age+15}')


# 6. Combine the two input statements above and print out the message `Hello, <name>, you are currently <age> years old. 
#   In 15 years time you will be <age_in_15_years_time>`.

print(f'Hello, {name}, you are currently {age} years old.\nIn 15 years time you will be {age+15}.')

# 7. Ask the user to enter their hometown, print it out in uppercase letters.
hometown = input("Please enter your hometown: ")
print(hometown.upper())



# 8. Ask the user to enter their favourite colour and find out the length of the colour they input.
favourite_colour = input("please enter your favourite color: ")
print(len(favourite_colour))


# 9. Ask the user to enter the weather and the month. Print out the string, `It is <month> and it is <weather> today`.



# 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string: 
#   `It is <month> and the average temperature is <average_temperature> degrees celsius`.
temperatures = []
for x in range (1,6,1):
  next_num = input(f'input temperature number {x}: ')
  temperatures.append(int(next_num))
print(f'the average temperature is {sum(temperatures) / len(temperatures)}')

# 11. Print out the above sentence but make the month upper case.



# 12. Create a variable that holds your favourite animals and print it out. 
#    Make sure the animals are all on different lines and tabbed.



# 13. Ask the user to enter their name as well as a number. 
#    Print out the uppercase character at that position in the string.



# 14. Slice the string with steps of 2, excluding the first and last characters of the string "WelcometoPython".
