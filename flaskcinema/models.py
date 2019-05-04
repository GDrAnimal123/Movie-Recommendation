class Rating():

    def __init__(self, movie_id, user_id, score):
        self.movie_id = movie_id
        self.user_id = user_id
        self.score = score

    def __repr__(self):
        return '<movie_id-{}, user_id-{}, score-{}>'.format(self.movie_id, self.user_id, self.score)
