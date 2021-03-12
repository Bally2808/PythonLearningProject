high_income = True
good_credit = True
criminal_record = True

if good_credit and high_income and not criminal_record:
    print("Eligible for loan")

else:
    print("Sorry you are not eligible for loan")