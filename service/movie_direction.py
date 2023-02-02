from models.movie_direction import MovieDirection as MovieDirectionModel

class MovieDirectionService():
    def __init__(self,db) -> None:
        self.db = db

    def get_movie_direction(self) -> MovieDirectionModel:
        result = self.db.query(MovieDirectionModel).all()
        return result

    def create_movie_direction(self,movie_direction:MovieDirectionModel):
        new_movie_direction = MovieDirectionModel(
        dir_id = movie_direction.dir_id ,   

        )
        self.db.add(movie_direction)
        self.db.commit()
        return