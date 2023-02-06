from models.director import Director as DirectorModel


class DirectorService():
    def __init__(self,db) -> None:
        self.db = db

    def get_director(self) -> DirectorModel:
        result = self.db.query(DirectorModel).all()
        return result

    def create_director(self,director:DirectorModel):
        new_director = DirectorModel(
        director_fname = director.director_fname ,
        director_lname = director.director_lname,    


        )
        self.db.add(new_director)
        self.db.commit()
        return