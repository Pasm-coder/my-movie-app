from models.rating import Rating as RatingModel
from schemas.rating import Rating


class Ratingervice():

    def __init__(self,db) -> None:
        self.db = db

    def get_rating(self):
        result = self.db.query(RatingModel).all()
        return result

    def get_rating(self,id:int):
        result = self.db.query(RatingModel).filter(RatingModel.id == id).first()
        return result

    def get_rating_by_release_contry(self,release_contry:str):
        result = self.db.query(RatingModel).filter(RatingModel.release_contry == release_contry).all()
        return result        

    def create_rating(self, rating:Rating):
        new_rating = RatingModel(
        mov_id=rating.mov_id,
        rev_id = rating.rev_id,
        rev_stars = rating.rev_stars,
        num_o_ratings = rating.num_o_ratings,
        )
        self.db.add(new_rating)
        self.db.commit()
        return 

    def update_movie(self,id:int, data:Rating):
        movie = self.db.query(RatingModel).filter(RatingModel.id == id).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.time = data.time
        movie.date_release = data.date_release
        movie.release_contry = data.release_contry
        self.db.commit()
        return

    def delete_movie(self,id:int,data:Rating):
        self.db.delete(data)
        self.db.commit



