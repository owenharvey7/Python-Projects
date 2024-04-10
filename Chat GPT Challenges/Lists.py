# 6
# Lists Challenge:
# Create a program that asks the user for their favorite movies and stores them in a list.

# Explain program to user:
print("This program will ask you for your favorite movies and store them in a list.\n")

# Create an empty list:
movies = []

# Ask the user for their name:
Name = input("What is your name? ")

# Ask the user for their favorite movies in a loop. The user can input as many movies as they want until they say done.
while True:
    movie = input("Enter your favorite movie. Please Enter one at a time and when you are finished input done: ")
    if movie == "done":
        break
    else:
        movies.append(movie)


# Enters the user's name and favorite movies into a text file:
with open("Favorite Movies.txt", "w") as f:
    f.write(f"{Name}'s favorite movies are: {movies}")


# Prints the user name and favorite movies to the console:
print(f"{Name}'s favorite movies are: {movies}. They have been saved to a text file.")
