import webbrowser

class Movie(object):
    """docstring for Movie...
    Takes the arguments title, poster_image, trailer_youtube, genre,
    and developer to inititalize and create new movies"""
    def __init__(self, title, poster_image, trailer_youtube, genre,
                developer):

        super(Movie, self).__init__()
        self.title = title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.genre = genre
        self.developer = developer
    
    # Opens a window to play trailer    
    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)