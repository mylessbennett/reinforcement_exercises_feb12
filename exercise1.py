drama = "Titanic"
documentary = "March of the Penguins"
comedy = "Step Brothers"
dramedy = "Crazy, Stupid, Love"

user_drama = input("Do you like dramas? (answer y/n) ")
user_doc = input("Do you like documentaries? (answer y/n) ")
user_comedy = input("Do you like comedies? (answer y/n) ")

if user_drama == "y" and user_doc == "y" and user_comedy == "y":
    print("You might enjoy {}, {}, or {}".format(drama, documentary, comedy))
elif user_doc == "n" and user_drama == "y" and user_comedy == "y":
    print("You might enjoy {}".format(dramedy))
elif user_doc == "y" and user_drama != "y" and user_comedy != "y":
    print("You might enjoy {}".format(documentary))
elif user_comedy == "y" and user_doc != "y" and user_drama != "y":
        print("You might enjoy {}".format(comedy))
elif user_drama == "y" and user_doc != "y" and user_comedy != "y":
            print("You might enjoy {}".format(drama))
else:
    print("You might want to try a good book instead!")
