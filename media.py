import webbrowser

class Movie():
    #create constructor
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, actors, director, release_date):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.actors = actors
        self.director = director
        self.release_date = release_date
