import time

time.sleep(3)
car_or_bike = ()
carbon_footprint = 0
score = 0
awards = []
feedback = []
while True:
    feedback_yes_no = input("Would you like to know how your feedback is calculated?").lower()
    if feedback_yes_no == "yes":
        print("Here is your feedback")
        print(feedback)
        print("This gives you a total carbon foorpint of", carbon_footprint)
        break
    elif feedback_yes_no == "no":
        print("Okay we won't show you")
        break
    else:
        print("Enter a valid response (yes or no)")
