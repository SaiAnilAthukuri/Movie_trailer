import webbrowser
class trailername():
    def __init__(self,movtitle,movgenre,movieposter,movyoutube):
        self.movtitle=movtitle
        self.movgenre=movgenre
        self.posterimage=movieposter
        self.trailer_youtube_url=movyoutube

    def trailer_see(self):
        webbrowser.open(self.trailer_youtube_url)
