# importing time
import time

#Create 3 attempts for the game
for attempts in range (1,4):

#Define all variables that will be manipulated
    awards = []
    score = 0
    carbon_footprint = 0
    feedback = []

#Print intro to game:
    print("Hello Gamer! Get ready to go on a adventure in your daily morning routine, where you will need to make decisions to reduce your carbon footprint and help save our planet! Your current score is 0.")


#Ask the user if they want to shower of bath, if they say bath, remove 1 to score and add 1.6 to carbon footprint.
# If they say shower, add 1 to score and give them water saver reward. If they don't answer accordingly, keep asking them.
    time.sleep(5)
    bath_or_shower = ()
    while True:
        bath_or_shower = input("It's early in the morning and you have just woken up. You're a bit stinky, and would like to freshen up. Would you like to shower or bath?").lower()
        if bath_or_shower == "shower":
            print("Good choice, a shower can save a lot of water. Your score is now 1, and you have just got a water saver reward!")
            score += 1
            awards.insert(0,"Water Saver")
            break
        elif bath_or_shower == "bath":
            print("Oh no, taking a bath is such a waste of water!. You have just lost 1 point and your score is now -1")
            score -= 1
            feedback.append("Showering saves water adding 1.6kg")
            carbon_footprint = carbon_footprint + 1.6
            break
        else:
            print("Please enter a valid answer (shower or bath)")
        time.sleep(1)

# If the user says shower, ask them how long they want to shower.
# If the time is > 10, make them loose 1 point and add 1 to carbon footprint. If it is < 10, give them a point.
    if bath_or_shower == "shower":
        time.sleep(3)
        time_shower = int(input("How long would you like to shower (min)"))
        if time_shower <= 10:
            score += 1
            print("Thats a ideal time for showering, here is a point for you. Your score is now" , score)
        elif time_shower >= 10:
            score -= 1
            print("Taking a shower for more than 10 minutes is a waste of time, so you lost a point and your score is now" , score)
            feedback.append("Taking shower for more than 10 minutes waste water adding 1 kg.")
            carbon_footprint = carbon_footprint + 1

# Ask the user if they want to check for running faucets, if they say not check, remove 1 to score and add 0.4 to carbon footprint.
# If they say check, add 1 to score and give them water saver reward. If they don't answer accordingly, keep asking them.
    time.sleep(3)
    check_or_notcheck = ()
    while True:
        check_or_notcheck = input("You have finished " + bath_or_shower + "ing would you like to check all your faucets to see if they are properly closed? (check or not check)").lower()
        if check_or_notcheck == "check":
            score += 1
            print("Good choice, checking for faucets can save water! You have gotten 1 to your score making your score" , score)
            if ("Water Saver") in awards == False:
                awards.insert(0, "Water Saver")
            break
        elif check_or_notcheck == "not check":
            score -= 1
            print("Oh oh, it's always good to check if faucets are running. It saves the planet and your money! Your score is now" , score)
            feedback.append("Checking for leaking faucets saves water adding 0.4 kg.")
            carbon_footprint = carbon_footprint + 0.4
            break
        else:
            print("Please enter a valid answer (check or not check)")
            time.sleep(1)

# Ask the user if they want to turn the lights on or leave them on, if they say on, remove 1 to score and add 5.6 to carbon footprint.
# If they say off, add 1 to score and give them energy saver reward. If they don't answer accordingly, keep asking them.
    time.sleep(3)
    lights_of_on = ()
    while True:
        lights_of_on = input("Now, you need to get ready to go to school. You are exiting your room, do you want to turn the lights off or leave them on?").lower()
        if lights_of_on == "off":
            score += 1
            print("Great, turning lights of saves lots of electricity. You gained one point to your score and you got a electro saver reward. Your score is now!" , score)
            awards.insert(0, "Electro Saver")
            break
        elif lights_of_on == "on":
            score -= 1
            print("Yikes, it's always best to turn lights off when not using them! You score is now " , score)
            feedback.append("You decided to leave your lights on even when not using adding 5.6kg.")
            carbon_footprint = carbon_footprint + 5.6
            break
        else:
            print("Please enter a valid answer (off or on)")
            time.sleep(1)

# Ask the user if they want to use a car or bike to go to school, if they say car, remove 1 to score, add 16kg of carbonfootprint, and give feedback
# If they say bike, give them 1 score and give them sustainable travel reward. If they don't answer with these two options, keep asking them
    time.sleep(3)
    car_or_bike = ()
    while True:
        car_or_bike = input("Now you are exiting your house, will you ask your parents to drop you off with a car or will you walk/bike to school?").lower()
        if car_or_bike == "bike" or car_or_bike == "walk":
            score += 1
            print("Great choice, walking is a much more sustainable than using a car which emits a lot of carbon. Your score is now " , score , " and you gained a sustainable travel reward!")
            awards.insert(0, "Sustainable Travel")
            break
        elif car_or_bike == "car":
            score -= 1
            print("Next time, try using a bike or walk. It can save A LOT of energy. You score is now" , score)
            feedback.append("You have decided to use a car adding 16 kg.")
            carbon_footprint = carbon_footprint + 16
            break
        else:
            print("Please enter a valid answer (car or walk/bike)")
            time.sleep(1)

# Print the game ending
    time.sleep(5)
    print("This is the end of the game. Thank you for playing it and making an effort to improve your morning routine. Here are the results of your gameplay")

# Print the score
    time.sleep(2)
    print("Your score is" , score)

# Print carbon footprint
    time.sleep(2)
    print("Your carbon footprint is" , carbon_footprint , "kg")

# Ask them if they want to know how their carbon footprint is calculated. If they say yes, print the feedback, if they say no, continue with the code
    while True:
        feedback_yes_no = input("Would you like to know how your carbonfoorpint is calculated?").lower()
        if feedback_yes_no == "yes":
            print("Here is your carbon footprint calculations")
            print(feedback)
            print("This gives you a total carbon foorpint of" , carbon_footprint)
            break
        elif feedback_yes_no == "no":
            print("Okay we won't show you")
            break
        else:
            print("Enter a valid response (yes or no)")

# Print their awards
    print("Here are all the awards you gained:")
    print(awards)

#Ask them if they want to use their awards. If they say yes, ask them which ones and add 0.5 to their score for every award they use. Delete award after it is used.
    while True:
        use_no_use = input("Would you like to use any of your awards (yes or no). Each reward can give you 0.5 to your score?").upper()
        if use_no_use == "YES":
            while True:
                which_one1 = input("Which award would you like to use").lower()
                if which_one1 == "sustainable travels":
                    score += 0.5
                    print("Your new score is" , score)
                    awards.remove("Sustainable Travels")
                    break
                elif which_one1 == "electro saver":
                    score += 0.5
                    print("Your new score is", score)
                    awards.remove("Electro Saver")
                    break
                elif which_one1 == "water saver":
                    score += 0.5
                    print("Your new score is", score)
                    awards.remove("Water Saver")
                    break
                else:
                    print("Enter a valid answer, it has to be one of your rewards")
            while True:
                if awards.len() > 0:
                    which_one2 = input("Which other award would you like to use").lower()
                    print("You have these awards", awards)
                    if which_one2 == "sustainable travel":
                        score += 0.5
                        print("Your new score is", score)
                        print("anything else?")
                        awards.remove("Sustainable Travel")
                        break
                    elif which_one2 == "electro saver":
                        score += 0.5
                        print("Your new score is", score)
                        print("anything else?")
                        awards.remove("Electro Saver")
                        break
                    elif which_one2 == "water saver":
                        score += 0.5
                        print("Your new score is", score)
                        print("anything else?")
                        awards.remove("Water Saver")
                        break
                    else:
                        print("Enter a valid answer, it has to be one of your rewards")
                else:
                    print("You do not have anymore awards")
                    break
            while True:
                if awards.len() > 0:
                    which_one3 = input("Which other award would you like to use").lower()
                    print("You have these awards", awards)
                    if which_one3 == "sustainable travels":
                        score += 0.5
                        print("Your new score is", score)
                        print("anything else?")
                        awards.remove("sustainable travels")
                        break
                    elif which_one3 == "electro saver":
                        score += 0.5
                        print("Your new score is", score)
                        print("anything else?")
                        rewards.remove("Electro Saver")
                        break
                    elif which_one3 == "water saver":
                        score += 0.5
                        print("Your new score is", score)
                        print("anything else?")
                        rewards.remove("Water Saver")
                        break
                    else:
                        print("Enter a valid answer, it has to be one of your rewards")
                else:
                    print("You do not have any more rewards")
                    break
        elif use_no_use == "NO":
            print("Okay, your awards have not been used and your final score is" , score)
            break
        else:
            print("Enter a valid value (yes or no)")

# If their score is more than 5 after using all their awards, then congrajulate them and break the loop for the number of tries.
    if score > 5:
        print("Congrajulations you beat the game!!!!")
        break
# If their score is not above 5, print game ending and make them repeat the game
    else:
        print("Looks like you used up all your rewards and your final score is", score, "It's not bad, but it certainly can improve. You have 2 attempts left to make your score above 5, try this game again and see how low you can get your carbon score!")
        time.sleep(10)



