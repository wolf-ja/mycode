#!/usr/bin/env python3




movies= [{"scifi":{"best":"matrix","worst":"matrix reloaded"}},{"comedy":{"best":"spaceballs","worst":"click"}},{"horror":{"best":"conjuring","worst":"glass house"}},]

print("Please select a genre")
genre = input(">")

if genre == "scifi":
    genreNum = 0

elif genre == "comedy":
    genreNum = 1

elif genre == "horror":
    genreNum = 2

else:
    print("We currently don't have that genre on file.")
    quit()

print("Please select best or worst")
choice = input(">")

if choice != "best" and choice != "worst":
    print("That is not a valid option.")
    quit()

else:
    print(f"The {choice} {genre} film is: {movies[genreNum][genre][choice].capitalize()}")



