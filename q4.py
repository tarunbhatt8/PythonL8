''' Q.4- Create a class MovieDetails and initialize it with movie name, artistname,Year of release and ratings .
Make methods to
1. Display-Display the details.
2. Add- Add the movie details. '''

class MovieDetails:
    '''class for displaying and adding movie details'''

    def __init__(self):
        self.moviename='unnamed movie'
        self.artist='unnamed artist'
        self.year=0
        self.ratings=0.0

    def Display(self):
        '''method to display the movie details'''
        print("Movie: {}\nFeaturing Artist: {}\nRelease Year:{}\nRatings: {}\n\n".format(self.moviename,self.artist,self.year,self.ratings))

    def Add(self,moviename,artist,year,ratings):
        '''method to add movie details'''
        self.moviename=moviename
        self.artist=artist
        self.year=year
        self.ratings=ratings

m1=MovieDetails()
m1.Display()
m2=MovieDetails()
m2.Add('Mission Impossible Fallout','Tom Cruise',2018,4.5)
m2.Display()
