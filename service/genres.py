from models.genres import Genres as GenresModel

class GenresService():
    def __init__(self,db) -> None:
        self.db = db

    def get_genres(self) -> GenresModel:
        result = self.db.query(GenresModel).all()
        return result

    def create_genres(self,genres:GenresModel):
        new_genres = GenresModel(
        genres_title = genres.genres_title ,   

        )
        self.db.add(new_genres)
        self.db.commit()
        return