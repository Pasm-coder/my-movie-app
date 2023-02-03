from models.movie_direction import MovieDirection as MovieDirectionModel
from schemas.movie_direction import MovieDirection


class MovieDirectionService():

    def __init__(self,db) -> None:
        self.db = db

    def get_movie_direction(self,dir_id:int):
        result = self.db.query(MovieDirectionModel).filter(MovieDirectionModel.dir_id == dir_id).all()
        return result

    def create_movie_direction(self,movie_direction: MovieDirectionModel):
        new_movie_direction = MovieDirectionModel(
            dir_id = movie_direction.dir_id,
            mov_id = movie_direction.mov_id,
        )
        self.db.add(new_movie_direction)
        self.db.commit()
        return