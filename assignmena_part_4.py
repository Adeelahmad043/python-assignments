# # Certified Python Programming
#         # Assignment # 4
# '''
# Question1:
# Use a dictionary to store information about a person you know. Store their first name,
# last name, age, and the city in which they live. You should have keys such as first_name,
# last_name, age, and city. Print each piece of information stored in your dictionary.
# Add a new key value pair about qualification then update the qualification value to
# high academic level then delete it.'''

# infor={
#         'First_name:':" Kashif",
#         'Last_name :':" ALi",
#         'Age       :':" 23",
#         'City      :':" Faisalabad"
# }
# infor['qualification:']="BSCS"
# for inform_key,inform_value in infor.items():
#         print(inform_key+" "+inform_value)

# '''
# Question2:
# Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
# Create a dictionary of information about each city and include the country that the city
# is in, its approximate population, and one fact about that city. The keys for each
# city’s dictionary should be something like country, population, and fact.
# Print the name of each city and all of the information you have stored about it.
# '''
# cities = {
#         "Karachi" :{
#                 'country    :':'Pakistan',
#                 'population :':'15741000',
#                 'Fact :'      :'It is the sixth largest city in the world by city population ',
#         },
#         "Islamabad" :{
#                 'country    :':'Pakistan',
#                 'population :':'1095000',
#                 'Fact :'      :'Islamabad is the capital of the top adventurous place Pakistan',
#         },
#         "Faisalabad" :{
#                 'country    :':'Pakistan',
#                 'population :':'3385000',
#                 'Fact :'      :'Faisalabad was designed in 1896 almost more than 100 years ago. ',
#         },
# }
# cit_name=input("Enter your citie name =")
# for inform_key,inform_value in cities[cit_name.title()].items():
#         print(inform_key+" "+inform_value)
# '''
# Question3:
# A movie theater charges different ticket prices depending on a person’s age. If a person
# is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10;
# and if they are over age 12, the ticket is $15. Write a loop in which you ask users their 
# age, and then tell them the cost of their movie ticket.
# '''
# while True:
#         age=int(input("Enter your age"))
#         if age< 3:
#                 print("The ticket is free")
#         elif age<12:
#                 print('The ticket is $10')
#         elif age>12:
#                 print("the ticket is $15")
#         op =int (input("1.yes or 2 no "))
#         if op == 1:
#                 break

# '''
# Question4:
# Write a function called favorite_book() that accepts one parameter, title. The function 
# should print a message, such as One of my favorite books is Alice in Wonderland. Call the 
# function, making sure to include a book title as an argument in the function call
# '''
# def favorite_book(book):
#         print(f"\t\tTitalName :{book.title()}:")
#         print("Such as one of my favorite book in the wonderland")
# book_name=input("Enter your favorite book name ::")
# favorite_book(book_name)

'''Question5:
Guess the number game
Write a program which randomly generate a number between 1 to 30 and ask the user in
input field to guess the correct number. Give three chances to user guess the number and 
also give hint to user if hidden number is greater or smaller than the number he given to
input field.
''' 
import random
winner = random.randint(1,100)
# winner = 4
guess = 1
num= int(input("Enert a number : "))
game_over = False 
while not game_over:
    if num == winner:
        print (f"You win this game and gesses this number :{guess} try")
        game_over = True

    else:
        if num > winner :
            print("too high")
        else:
            print("too low")
        guess += 1
        num = int(input("Enter agian"))
