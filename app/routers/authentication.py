from fastapi import APIRouter
from app import crud, database, schemas, models
from fastapi import Depends
from sqlalchemy.orm import Session

router = APIRouter(
    tags=['Authentication']
)


@router.post("/login", response_model=schemas.ShowUser)
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.Users).filter(models.Users.email == request.email).first()
    # if not user:
    #     raise HTTP

    return user
