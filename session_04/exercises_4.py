# Session 4 Exercises

## Section A
# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list.
items = ["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]
print(items)


# 2. Add "Grapes" to the list and print the list.
items.append("Grapes")
print(items)


# 3. Change "Pears" to "Strawberries" and print the list.
items[2] = "Strawberries"
print(items)


# 4. Remove "Apples" from the list and print the list.
del(items[0])
print(items)


# 5. Print out the current length of the list.
print(len(items))


# 6. Order the list alphabetically.
items.sort()
print(items)


# 7. Print out the list again.




# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Loop through the list you created in section A and print each item out.
for fruit in items:
  print(fruit)


# 2. Print the numbers 1 to 100 (including the number 100).

# for n in range(1,101):
#   print(n)


# 3. Print all odd numbers from 1 to 100.
# for n in range(1,100,2):
#   print(n)


# 4. The modern olympics started in 1896, print the years they have been held (bonus points to skip the years it has not been held 1916, 1940, 1944, 2020).
not_held = [1916,1940,1944,2020]
for n in range(1896, 2023, 4):
  if not(n in not_held):
    print(n)


# 5. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.




# 6. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.



# 7. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".



# 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.



# 9. Create a list with five names in. Write a for loop which appends  Dr. to each name in the new list.



# 10. FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". 
#    For numbers which are multiples of both three and five, print "FizzBuzz".

#     ```
#     1
#     2
#     Fizz
#     4
#     Buzz
#     Fizz
#     7
#     8
#     Fizz
#     Buzz
#     11
#     Fizz
#     13
#     14
#     FizzBuzz
#     ```
