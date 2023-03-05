class tvShows:
    category="thriller"
    
class prisonbreak(tvShows):
    
    category="drama + thriller"
    seasons=5
    episodes=22

    def __init__(self,h,a):
        self.hero=h
        self.actress=a

    def __str__(self):
        return f"The actor playing hero - {self.hero} is wentsworth miller and the actress playing heroine- {self.actress} is sarah" 

tbag=prisonbreak("michael","sara")
print(tbag)
print(tbag.seasons)
print(tbag.category)



