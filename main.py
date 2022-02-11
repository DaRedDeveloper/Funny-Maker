# Imports
import random

# Colors
Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m" 
black = "\033[0;30m"
black = "\033[0;90m"
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
cyan = "\033[0;96m"
white = "\033[0;97m"
cyan_back="\033[0;46m"
pink_back="\033[0;45m"
white_back="\033[0;47m"
blue_back="\033[0;44m"
orange_back="\033[0;43m"
green_back="\033[0;42m"
red_back="\033[0;41m"
grey_back="\033[0;40m"
bold = "\033[1m"
underline = "\033[4m"
italic = "\033[3m"
darken = "\033[2m"
reset = "\033[0m"

# List of Funny Phrases
listoffuny = ["You can improve your ","Tired of making ", "Top 10 Moments of ", "Help me ", "This is so funny ", "Make $1,000 per day using ", "The lazy way to ", "Best book of the year is... ", "Get rid of ", "Today, you can lose money by ", "A suprising tool to make ", "Haha! This is so funny ", "Learn how to start ", "Listen to your customers, they will teach you about ", "What You Should Have Asked Your Teachers About ", "Winning tactics of ", "Make money using ", "Tired of having seizures? Use our new tylenol, ", "How to make a ", "Why you really need a ", "Top 3 Ways To Buy A Used ", "Don't Just Sit There! Start ", "Best 50 Tips For ", "7 and a Half Very Simple Things You Can Do To Save ", "Here Is A Method That Is Helping ", "Here Is What You Should Do For Your ", "Avoid The Top 10 Mistakes Made By Beginning ", "Want A Thriving Business? Focus On ", "The Secret of ", "What Everyone Ought To Know About ", "The Ultimate Deal On ", "Why Most People Will Never Be Great At ", "The Truth Is You Are Not The Only Person Concerned About ", "The Anthony Robins Guide To ", "Warning: These 9 Mistakes Will Destroy Your "]

# When Run..
print(green + "--------" + magenta + "Funny" + green + " Maker V3.5" + green + "--------" )
print(yellow + "Made by DaxCodes")

# Loop
while True:
  print(Green + "")
  funy = input(bold + "Enter a Noun: ")
  randomthing = random.choice(listoffuny)
  print(" ")
  print(green + "-----------------")
  print(green + randomthing + funy)
  print(green + "-----------------")