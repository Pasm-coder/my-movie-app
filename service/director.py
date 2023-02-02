from models.director import Director as DirectorModel

class DirectorService():
    def __init__(self,db) -> None:
        self.db = db

    def get_director(self) -> DirectorModel:
        result = self.db.query(DirectorModel).all()
        return result

    def create_director(self,director:DirectorModel):
        new_director = DirectorModel(
        director_first_name = director.director_first_name ,
        director_last_name = director.director_last_name,    


        )
        self.db.add(new_director)
        self.db.commit()
        return