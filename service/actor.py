from models.actor import Actor as ActorMoldel


class ActorService():
    def __init__(self,db) -> None:
        self.db = db

    def get_actors(self) -> ActorMoldel:
        result = self.db.query(ActorMoldel).all()
        return result

    def create_actor(self,actor:ActorMoldel):
        new_actor = ActorMoldel(
        act_fname = actor.act_fname ,
        act_lname = actor.act_lname,
        act_gender = actor.act_gender,    
        )
        self.db.add(new_actor)
        self.db.commit()
        return