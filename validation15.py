import re

email = input("Enter email: ")
phone = input("Enter phone number: ")

if re.search(r'@.*\.', email):
    print("Valid Email")
else:
    print("Invalid Email")

if re.fullmatch(r'\d{10}', phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

log = "Transaction ID: TXN12345"
print("Transaction ID:", re.findall(r'TXN\d+', log))
