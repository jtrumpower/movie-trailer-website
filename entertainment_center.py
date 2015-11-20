import media
import fresh_tomatoes
import datetime

# Create 3 movie instances

# These arguements are already inside parenthsis and thus
# I do not believe I should place them in another parenthesis
# I also do not think a backslash is required because this is
# not a expression being evaluated but rather method arguements
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        ["Tom Hanks",
                         "Tim Allen",
                         "Don Rickles"
                        ],
                        "John Lasseter",
                        datetime.date(1995, 11, 22))

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://resizing.flixster.com/W1BtrV4MS0HZwzJQSBe4mBQfwQs=/800x1200/dkpu1ddg7pbsk.cloudfront.net/movie/11/17/67/11176792_ori.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     ["Sam Worthington",
                      "Zoe Saldana",
                      "Sigourney Weaver"
                     ],
                     "James Cameron", \
                     datetime.date(2009, 12, 18))


avengers = media.Movie("Avengers",
                       "Superheros fight aliens and stuff",
                       "http://ia.media-imdb.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZTcwODg0OTY0Nw@@._V1_SX640_SY720_.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8",
                       ["Robert Downey Jr.",
                        "Chris Evans",
                        "Mark Ruffalo"
                       ],
                       "Joss Whedon",
                       datetime.date(2012, 5, 4))

# Create array to store movies
movies = [toy_story, avatar, avengers]

# Cenerate and open HTML page
fresh_tomatoes.open_movies_page(movies)
