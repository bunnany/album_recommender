##
# album_recommender.py
# Asks the user to enter an album
# An album a title, artist, genre and rating
# The user can add, edit, delete and rate an album
# If the user rates an album, recommend them another album (from the same genre)


# Add function
def add(albums):
    """
    Adds an album to the albums collection
    Asks user for title, artist, genre and rating
    Returns the updated album
    """
    # Add a title, artist and genre which are strings
    title = input("Title: ")
    artist = input("Artist: ")
    genre = input("Genre: ")

    # Add a rating between 1 and 5 and force input
    MIN_RATING = 1
    MAX_RATING = 5
    while True:
        try:
            rating = int(input("Rating {}-{}: ".format(MIN_RATING, MAX_RATING)))
            if rating < MIN_RATING or rating > MAX_RATING:
                print("Rating must be between {}-{}: ".format(MIN_RATING, MAX_RATING))
            else:
                break
        except:
            print("Rating must be between {}-{}: ".format(MIN_RATING, MAX_RATING))

    # Add the values to the album dictionary
    album = {"title":title, "artist":artist, "genre":genre, "rating":rating}

    # Add our album to our albums collection
    albums.append(album)

    return albums
        
# Edit function


# Delete function


# Display all
def display_all(albums):
    """
    Print out all the albums in the collection
    """
    # Print out each album
    for album in albums:
        # Print out the details of each album
        print("Title: ", album["title"])
        print("Artist:", album["artist"])
        print("Genre:", album["genre"])
        print("Rating:", album["rating"])
        print()     # New line after each album

# Rate function


# Recommend function


def menu(albums):
    """
    Displays the options to the user and calls accordingly.
    """

    # Print the menu and loop until user quits
    choice = None
    while choice != "Q":
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
            albums = add(albums)
        elif choice == "E":
            pass
        elif choice == "D":
            pass
        elif choice == "P":
            display_all(albums)
        elif choice == "R":
            pass
        elif choice == "Q":
            print("Goodbye!")
        else:
            print("That is not an option you knucklehead!")


# Main routine
if __name__ == "__main__":
    # declaring the list of dictionary of albums
    albums = []

    # Call the menu
    menu(albums)






