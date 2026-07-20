#Hey there! , this is my First OOP project.
class Movie:
    def __init__(self, title ,director , year, rating):
        self.title = title
        self.director = director
        self.year = year
        self.rating = rating

    def show(self):
        print("Tilte: " , self.title)
        print("Director: ", self.director)
        print("Year: ", self.year)
        print(f"Rating [{self.rating}]")
        print("-" * 30)

class MovieCollection:
    def __init__(self):
        self.movie = []

    def add_movies(self , movie):
        self.movie.append(movie)
    
    def show_all(self):
        print("====Movie Collection====")
        for Movie in self.movie:
            Movie.show()

def movie_addition():
    title = input("Enter movie title: ")
    director = input("Enter director: ")
    year = int(input("Year: "))
    rating = float(input("Rating: "))
    print("-"* 30)
    movie5 = Movie(title , director , year , rating)
    return movie5
    
collection = MovieCollection()



movie1 = Movie("Intestaller", "Christopher Nolan", "2014", 9.5)
movie2 = Movie("The Matrix", "Wachawski Sisters", "1999", 9.2)
movie3 = Movie("Inception", "Christopher Nolan", "2010", 9.0)
movie4 = Movie("The Godfather", "Francis Ford Coppola", "1972", 9.8)

movie_add = int(input("How many movies you want to add? (Max = 3)"))
for movie in range(movie_add):      
            movie = movie_addition()
            collection.add_movies(movie)

collection.add_movies(movie1)
collection.add_movies(movie2)
collection.add_movies(movie3)
collection.add_movies(movie4)
collection.show_all()