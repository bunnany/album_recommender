##
# album_recommender.py
# Asks the user to enter an album
# An album a title, artist, genre and rating
# The user can add, edit, delete and rate an album
# If the user rates an album, recommend them another album (from the same genre)


# Add function
def add(albums, album_id):
    """
    Adds an album to the albums collection
    Asks user for title, artist, genre and rating
    Increments the album_id
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
        except ValueError:
            print("Rating must be between {}-{}: ".format(MIN_RATING, MAX_RATING))

    # Add the values to the album dictionary
    album = {"title":title, "artist":artist, "genre":genre, "rating":rating}

    # Add our album to our albums collection
    albums[album_id] = album

    # Increment the album id
    album_id += 1

    return albums, album_id
        
                  


# Edit function


# Delete function


# Display all


# Rate function


# Recommend function


def menu(albums, album_id):
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
            albums, album_id = add(albums, album_id)
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

    # track the current album ID
    album_id = 0
    
    menu(albums, album_id)






