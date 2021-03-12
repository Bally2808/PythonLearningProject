house_price = 1000000
good_down = str(1000000 / 100 * 10)
bad_down = str(1000000 / 100 * 20)
good_credit = True
bad_credit = False

if good_credit:
    print("You have a good credit")
    print("You only have to put " + good_down + " as down payment")

elif bad_credit:
    print("You have a bad credit")
    print("You have to deposit " + bad_down + ",")

print("Thank you for using our services. Have a great day")
