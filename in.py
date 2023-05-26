Age= int(input("Enter the age: "))
Citizenship=input("Enter Citizenship: ")
Countries=["Kenyan","Ugandan","Tanzanian"]
if Age>=18 and Citizenship in Countries:
    print("Citizen is eligible to vote")
else:
    print("Not a citizen, not eligible to vote")