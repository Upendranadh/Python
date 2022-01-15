# 💪 This is a Difficult Challenge 💪
# Instructions
# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. 

# Then check for the number of times the letters in the word LOVE occurs. 

# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."
# e.g.

# name1 = "Angela Yu"
# name2 = "Jack Bauer"



# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1=name1.lower()
name2=name2.lower()

True_Count=name1.count('t')+name1.count('r')+name1.count("u")+name1.count('e')+name2.count('t')+name2.count('r')+name2.count('u')+name2.count('e')

Love_Count=name1.count('l')+name1.count('o')+name1.count('v')+name1.count('e')+name2.count('l')+name2.count('o')+name2.count('v')+name2.count('e')

TcountStr=f'{True_Count}{Love_Count}'
Tcount=int(TcountStr)

if Tcount <10 or Tcount>90:
    print(f"Your score is {Tcount}, you go together like coke and mentos.")
elif Tcount>40 and Tcount<50:
    print(f"Your score is {Tcount}, you are alright together.")
else:
    print(f"Your score is {Tcount}.")



