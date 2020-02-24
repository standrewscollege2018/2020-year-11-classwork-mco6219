""" this program will ask a user for their favourite movies and make a list from their input """

# set up empty list to store the movies
movies = []

# asking user for input, starting loop to ask for three movies
for i in range (0,3,1):
    movie_name = input("Enter name of your favourite movie:")
    movies.append(movie_name)
    
# printing list
print(movies)