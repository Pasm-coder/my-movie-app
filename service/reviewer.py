from models.reviewer import Reviewer as ReviewerModel
from schemas.reviewer import Reviewer

class ReviewerService():
    def __init__(self,db) -> None:
        self.db = db

    def get_reviewer(self) -> ReviewerModel:
        result = self.db.query(ReviewerModel).all()
        return result

    def create_reviewer(self,reviewer:ReviewerModel):
        new_reviewer = ReviewerModel(
            rev_id=reviewer.rev_id,
            rev_name=reviewer.rev_name,   

        )
        self.db.add(new_reviewer)
        self.db.commit()
        return
    
