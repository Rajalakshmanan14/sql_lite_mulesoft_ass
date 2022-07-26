class Movie:

    def __init__(self,moviename, actor, actress, year):
        self.moviename=moviename
        self.actor = actor
        self.actress = actress
        self.year = year



    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.moviename,self.actor, self.actress, self.year)