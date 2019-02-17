from random import *
import time
import os

class NotPositiveError(ValueError):
    pass

continue_game = "Y"
line = 0

name = input("Hello! What is your name? ")
print ("Hello " + name + "! Are you ready for a challenge?")

time.sleep(1)
ready = input("Y or N? ")
if ready not in ['Y', 'Yes', 'y', 'yes']:
    shut_down = input("Are you sure? This will close the program. " )
    if shut_down not in ['N', 'No', 'n', 'no']:
        print ("Ok. see you later when you're ready. Bye!")
        time.sleep(2)
        raise SystemExit
    else:
        ready = input ("Are you ready or not? Yes or no? " )

print ("The challenge is... Drumroll please...")
time.sleep(1)
print ("Guess the Number! You have to guess a number within 1 and 100, within 5 guesses!")

while continue_game in ['Y', 'Yes', 'y', 'yes']:
    time.sleep(1.7)
    multiplayer = input ("Would you like to play 1 or 2 player? ")
    while multiplayer == "1":
        correctNumber = randint(1, 100) 
        guessesTaken = 0
        change = input("I can give you a choice to change the amount of guesses you get. This can make it harder or easier for yourself. Would you like that? ")
        if change in ['Y', 'Yes', 'y', 'yes']:
            custom = input("Choose how many guesses you want: ")
            while True:
                try:
                    custom = int(custom)
                    if custom <= 0:
                            raise NotPositiveError
                    break
                except ValueError:
                        print("This was not a number, please try again. ")
                        custom = input("Choose how many guesses you want: ")
                except NotPositiveError:
                        print("The number was not positive, please try again. ")
                        custom = input("Choose how many guesses you want: ") 

            while guessesTaken < custom:
                while guessesTaken < (custom - 1):
                    time.sleep(1)
                    x = int(input("Guess: "))
        
                    guessesTaken = guessesTaken + 1

                    if x < correctNumber:
                        print ("Your guess is too low. Try again")

                    if x > correctNumber:
                        print ("Your guess is too high. Try again")

                    if x == correctNumber:
                        break

                if x == correctNumber:
                    break

                time.sleep(0.65)
                print ("Woah, you're on your last guess now. Make it count...")
                x = int(input("Guess: "))
                guessesTaken = guessesTaken + 1

                if x < correctNumber:
                    print ("Your guess was too low. ")
                    break
                if x > correctNumber:
                    print ("Your guess was too high.")
                    break
                if x == correctNumber:
                    break

            if x == correctNumber:
                guessesTaken = str(guessesTaken)
                print ("Congratulations " + name + "! You guessed the number in " + guessesTaken + " guesses!" )
                break    

            if x != correctNumber:
                correctNumber = str(correctNumber)
                print ("Sorry, you couldn't complete the challenge. The number I was thinking of was " + correctNumber)
                break

        else:
            while guessesTaken < 5:
                while guessesTaken < 4:
                    time.sleep(1)
                    x = int(input("Guess: "))
        
                    guessesTaken = guessesTaken + 1

                    if x < correctNumber:
                        print ("Your guess is too low. Try again")

                    if x > correctNumber:
                        print ("Your guess is too high. Try again")

                    if x == correctNumber:
                        break

                if x == correctNumber:
                    break

                time.sleep(0.65)
                print ("Woah, you're on your last guess now. Make it count...")
                x = int(input("Guess: "))
                guessesTaken = guessesTaken + 1

                if x < correctNumber:
                    print ("Your guess was too low. ")
                    break
                if x > correctNumber:
                    print ("Your guess was too high.")
                    break
                if x == correctNumber:
                    break

            if x == correctNumber:
                guessesTaken = str(guessesTaken)
                print ("Congratulations " + name + "! You guessed the number in " + guessesTaken + " guesses!" )
                break    

            if x != correctNumber:
                correctNumber = str(correctNumber)
                print ("Sorry, you couldn't complete the challenge. The number I was thinking of was " + correctNumber)
                break
        
    while multiplayer == "2":
        max_num = 101
        min_num = 0
        Player1 = input("What is your name Player 1? ")
        Player2 = input("What is your name player 2? ")
        print ("Hello " + Player1 + " and " + Player2 + "!")
        print ("The challenge this time is that Player 1 (" + Player1 +  ") will type in a number without you looking. ")
        print ("After that Player 2 (" + Player2 + ") will try to guess the number within 5 guesses!" )
        print ( Player2 + ", time to look away now!")
        time.sleep(1)
        secret_num = int(input(Player1 + ", please tell me your secret number within 1 and 100: "))
        while secret_num > 101 or secret_num < 0:
                try:
                    secret_num = int(secret_num)
                    if secret_num <= 0:
                            raise NotPositiveError
                    break
                except ValueError:
                        print("This was not a number, please try again. ")
                        secret_num = input("Please tell me your secret number: ")
                except NotPositiveError:
                        print("The number was not positive, please try again. ")
                        secret_num = input("Please tell me your secret number: ")
        while max_num > secret_num > min_num:
            while 85 > line:
                print(" ")
                line = line + 1
            print (Player2 + ", you can look now. Guess what you think the number is.")
            guessesTaken = 0
            while guessesTaken < 5:
                while guessesTaken < 4:
                    time.sleep(1)
                    x = int(input("Guess: "))
    
                    guessesTaken = guessesTaken + 1

                    if x < secret_num:
                        print ("Your guess is too low. Try again")

                    if x > secret_num:
                        print ("Your guess is too high. Try again")

                    if x == secret_num:
                        break

                if x == secret_num:
                    break

            if x == secret_num:
                break

                time.sleep(0.65)
                print ("Woah, you're on your last guess now. Make it count...")
                x = int(input("Guess: "))
                guessesTaken = guessesTaken + 1

                if x < secret_num:
                    print ("Your guess was too low. ")
                    break
                if x > secret_num:
                    print ("Your guess was too high.")
                    break

                if x == secret_num: 
                    break

        if x == secret_num:
            guessesTaken = str(guessesTaken)
            print ("Congratulations " + Player2 + "! You guessed the number in " + guessesTaken + " guesses!" )
            break
        
        if x != secret_num:
            secret_num = str(secret_num)
            print ("Sorry, you couldn't complete the challenge. The number " + Player1 + " was thinking of was " + secret_num)
            break

    
    while multiplayer != "1" or "2":
        try:
            multiplayer = int(multiplayer)
            if multiplayer <= 0:
                raise NotPositiveError
            break
            if multiplayer > 2:
                print("There isn't a game mode for more than 2 players.")
                multiplayer = int(input("Choose how many players you want: "))
            break
        except ValueError:
            print("This was not valid, please try again. ")
            multiplayer = int(input("Choose how many players you want: "))
            break
        except NotPositiveError:
            print("The number was not positive, please try again. ")
            multiplayer = int(input("Choose how many players you want: "))
            break

    continue_game == input("Want another game? ")
    if continue_game in ['Y', 'Yes', 'y', 'yes']:
        continue    
