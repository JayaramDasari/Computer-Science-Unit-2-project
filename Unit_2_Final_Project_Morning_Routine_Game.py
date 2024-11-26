# importing time
import time

#Set attempts to 0
attempts = 0

#Create 3 attempts for the game, and if the attempts go above 3, break the loop
for attempts in range (1,4):
    awards = []
    score = 0
    carbon_footprint = 0

#Print intro to game:
    print("Hello Gamer! Get ready to go on a adventure in your daily morning routine, where you will need to make decisions to reduce your carbon footprint and help save our planet! Your current score is 0.")
    time.sleep(5)
#Ask the user if they want to shower of bath, if they say bath, remove 1 to score, if they say shower, add 1 to score and give them water saver reward. If they don't answer accordingly, keep asking them.
    bath_or_shower = ()
    while bath_or_shower == ("bath") or ("shower")
        bath_or_shower = input("It's early in the morning and you have just woken up. You're a bit stinky, and would like to freshen up. Would you like to shower or bath?").lower()
        if bath_or_shower == "shower":
            print("Good choice, a shower can save a lot of water. Your score is now 1, and you have just got a water saver reward!")
            score += 1
            awards.insert(0,"Water Saver")
        elif bath_or_shower == "bath":
            print("Oh no, taking a bath is such a waste of water!. You have just lost 1 point and your score is now -1")
            score -= 1
        else:
            print("Please enter a valid answer (shower or bath")

    time.sleep(30)



    if score > 5:
        print("Congrajulations you beat the game:")
        break

