""" this program uses a while loop to repeatedly ask the user for their favourite movies """

# set list to store movies
movies = []

keep_asking = True

while keep_asking == True:
    movie_name = input("Enter a favourite movie")
    if movie_name == "stop":
        keep_asking = False 
        
    else:
        movies.append(movie_name)
        
print(movies)

#loop through list and display the movies
for movie in movies:
    print(movie)
    
# loop through list and produce a numbered list of items
for i in range(len(movies)):
    print(i+1, movies[i])
    

