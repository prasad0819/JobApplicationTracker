from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app import models, schemas


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.Users).filter(models.Users.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.Users).filter(models.Users.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Users).offset(skip).limit(limit).all()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(user: schemas.CreateUser, db: Session):
    hashed_password = pwd_context.hash(user.password)
    new_user = models.Users(id=user.id, first_name=user.first_name, last_name=user.last_name, email=user.email,
                            password=hashed_password)
    # if new_user:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Jobs).offset(skip).limit(limit).all()


def create_job(db: Session, job: schemas.CreateJob):
    db_job = models.Jobs(id=job.id, title=job.title, company=job.company, status=job.status, location=job.location,
                         applied_on=job.applied_on, source=job.source)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


def update_job(db: Session, job: schemas.CreateJob, job_id: int):
    job_update = db.query(models.Jobs).filter(models.Jobs.id == job_id)

    # if not job_update.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} not found")
    job_update.update(**job.dict())
    db.commit()
    db.refresh(job_update)
    return job_update


def delete_job(db: Session, job_id: int):
    job_delete = db.query(models.Jobs).filter(models.Jobs.id == job_id).delete(synchronize_session=False)
    db.add(job_delete)
    db.commit()
    db.refresh(job_delete)
    return job_delete


def delete_user(db: Session, user_id: int):
    user_delete = db.query(models.Users).filter(models.Users.id == user_id).delete(synchronize_session=False)
    db.add(user_delete)
    db.commit()
    db.refresh(user_delete)
    return user_delete
