import webbrowser

class Tollywoodmovies():
    def __init__(self,mov_title,mov_storyline,mov_posterimage,mov_youtubeurl):
        self.title=mov_title
        self.story=mov_storyline
        self.poster=mov_posterimage
        self.youtubeurl=mov_youtubeurl
    def show_movie_trailers(self):
        webbrowser.open(self.trailer_youtube_url)
class Hollywoodmovies():
    def __init__(self,mov_title,mov_storyline,mov_posterimage,mov_youtubeurl):
        self.title=mov_title
        self.story=mov_storyline
        self.poster=mov_posterimage
        self.youtubeurl=mov_youtubeurl
    def show_movie_trailers(self):
        webbrowser.open(self.trailer_youtube_url)
    
