# importing time
import time

#Set attempts to 0
attempts = 0

#Create 3 attempts for the game, and if the attempts go above 3, break the loop
for attempts in range (1,4):
    awards = []
    score = 0
    carbon_footprint = 0
    feedback = []

#Print intro to game:
    print("Hello Gamer! Get ready to go on a adventure in your daily morning routine, where you will need to make decisions to reduce your carbon footprint and help save our planet! Your current score is 0.")


#Ask the user if they want to shower of bath, if they say bath, remove 1 to score, if they say shower, add 1 to score and give them water saver reward. If they don't answer accordingly, keep asking them.
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
            feedback.append("Showering saves water")
            carbon_footprint = carbon_footprint + 1.6
            break
        else:
            print("Please enter a valid answer (shower or bath)")
        time.sleep(3)

# If the user says shower, ask them how long they want to shower. If the time is > 10, make them loose a point and if it is < 10, give them a point. Add 1 kg of footptint as well.
    if bath_or_shower == "shower":
        time.sleep(3)
        time_shower = int(input("How long would you like to shower (min)"))
        if time_shower <= 10:
            score += 1
            print("Thats a ideal time for showering, here is a point for you. Your score is now" , score)
        elif time_shower >= 10:
            score -= 1
            print("Taking a shower for more than 10 minutes is a waste of time, so you lost a point and your score is now" , score)
            feedback.append("Taking shower for more than 10 minutes waste water")
            carbon_footprint = carbon_footprint + 1

# Ask the user if they want to check for running faucets, if they say check, remove 1 to score, if they say don't check, add 1 to score and give them water saver reward. If they don't answer accordingly, keep asking them.
    time.sleep(3)
    check_or_notcheck = ()
    while True:
        check_or_notcheck = input("You have finished " + bath_or_shower + "ing would you like to check all your faucets to see if they are properly closed? (check or not check)").lower()
        if check_or_notcheck == "check":
            score += 1
            print("Good choice, checking for faucets can save water! You have gotten 1 to your score making your score" , score)
            if ("Water Saver") in awards == True:
                awards.insert(0, "Water Saver")
            break
        elif check_or_notcheck == "not check":
            score -= 1
            print("Oh oh, it's always good to check if faucets are running. It saves the planet and your money! Your score is now" , score)
            feedback.append("Checking for leaking faucets saves water")
            carbon_footprint = carbon_footprint + 0.4
            break
        else:
            print("Please enter a valid answer (check or not check)")
            time.sleep(3)

# Ask the user if they want to turn the lights on or leave them on, if they say on, remove 1 to score, if they say off, add 1 to score and give them energy saver reward. If they don't answer accordingly, keep asking them.
    time.sleep(3)
    lights_of_on = ()
    while True:
        lights_of_on = input("Now, you need to get ready to go to school. You are exiting your room, do you want to turn the lights off or leave them on?").lower()
        if lights_of_on == "off":
            score += 1
            print("Great, turning lights of saves lots of electricity. You gained one point to your score and you got a electro saver reward. Your score is now!" , score)
            awards.insert(0, "Electro saver")
            break
        elif lights_of_on == "on":
            score -= 1
            print("Yikes, it's always best to turn lights off when not using them! You score is now " , score)
            feedback.append("You decided to leave your lights on even when not using")
            carbon_footprint = carbon_footprint + 5.6
            break
        else:
            print("Please enter a valid answer (off or on)")

    if score > 5:
        print("Congrajulations you beat the game:")
        break
    else:
        print("Looks like you used up all your rewards and your final score is", score,
              "It's not bad, but it certainly can improve. You have 2 attempts left to make your score above 5, try this game again and see how low you can get your carbon score!")
        time.sleep(10)



