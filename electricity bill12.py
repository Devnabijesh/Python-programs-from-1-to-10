
try:
    units = int(input("Enter units consumed: "))

    if units < 0:
        raise ValueError("Negative units not allowed")

except ValueError as e:
    print("Error:", e)

else:
    bill = units * 5
    print("Electricity Bill: Rs.", bill)

finally:
    print("Thank you!")

