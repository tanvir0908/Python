name = input("Enter your name: ")

match name:
    case "Tanvir" | "Hasan" | "Emon":
        print("Natore")
    case "Hablu":
        print("Dhaka")
    case _:
        print("Who?")

# if name == "Tanvir" or name == "Hasan" or name == "Emon":
#     print("Natore")
# elif name == "Hablu":
#     print("Dhaka")
# else:
#     print("Who?")
