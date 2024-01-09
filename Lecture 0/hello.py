# remove white space from string and capitalize users name
name = input("Enter your name: ").strip().title()

# split users name into firstName and lastName
firstName, lastName = name.split(" ")

print("Hello,", firstName)
