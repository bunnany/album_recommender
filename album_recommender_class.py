##
# album_recommender.py
# Asks the user to enter an album
# An album a title, artist, genre and rating
# The user can add, edit, delete and rate an album
# If the user rates an album, recommend them another album (from the same genre)


# Add function


# Edit function


# Delete function


# Display all


# Rate function


# Recommend function


def menu(albums):
    """
    Displays the options to the user and calls accordingly.
    """

    # Print the menu and loop until user quits
    while True:
        print("""
Welcome to the Album rater and recommender
(A)dd an album
(E)dit an album
(D)elete an album
(P)rint all albums
(R)ate an album
(Q)uit""")
        choice = input("Please enter your choice: ").upper()

        if choice == "A":
            pass
        elif choice == "E":
            pass
        elif choice == "D":
            pass
        elif choice == "P":
            pass
        elif choice == "R":
            pass
        elif choice == "Q":
            print("Goodbye!")
            break
        else:
            print("That is not an option you knucklehead!")


# Main routine
if __name__ == "__main__":
    # declaring the dictionary of dictionary of albums
    albums = {}
    menu(albums)






