drama = "Titanic"
documentary = "March of the Penguins"
comedy = "Step Brothers"
dramedy = "Crazy, Stupid, Love"

user_drama = int(input("Rate genre on a scale of 1-5: Dramas "))
user_doc = int(input("Rate genre on a scale of 1-5: Documentaries "))
user_comedy = int(input("Rate genre on a scale of 1-5: Comedies "))

if user_doc >= 4 and user_drama >= 4 and user_comedy >= 4:
    print("You might enjoy {}, {}, or {}".format(drama, comedy, documentary))
elif user_doc <= 3 and user_drama >= 4 and user_comedy >= 4:
    print("You might enjoy {}".format(dramedy))
elif user_doc >= 4 and user_drama <= 3 and user_comedy <=3:
    print("You might enjoy {}".format(documentary))
elif user_drama >= 4 and user_doc <= 3 and user_comedy <=3:
    print("You might enjoy {}".format(drama))
elif user_comedy >= 4 and user_drama <= 3 and user_doc <=3:
    print("You might enjoy {}".format(comedy))
else:
    print("You might want to try a good book instead!")
