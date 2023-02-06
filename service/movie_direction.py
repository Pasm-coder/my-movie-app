from models.movie_direction import MovieDirection as MovieDirectionModel
from schemas.movie_direction import MovieDirection



class MovieDirectionService():

    def __init__(self,db) -> None:
        self.db = db

    def get_movie_direction(self,direction_id:int):
        result = self.db.query(MovieDirectionModel).filter(MovieDirectionModel.direction_id == direction_id).all()
        return result

    def create_movie_direction(self,movie_direction: MovieDirectionModel):
        new_movie_direction = MovieDirectionModel(
            direction_id = movie_direction.direction_id,
            movie_id = movie_direction.movie_id,
        )
        self.db.add(new_movie_direction)
        self.db.commit()
        return