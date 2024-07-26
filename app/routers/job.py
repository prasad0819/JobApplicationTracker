from fastapi import APIRouter
from typing import List
from app import crud, database, schemas
from fastapi import Depends
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/jobs",
    tags=['Jobs']
)


@router.get("/", response_model=List[schemas.Job])
def read_job(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    jobs = crud.get_jobs(db, skip=skip, limit=limit)
    return jobs


@router.post("/", response_model=schemas.ShowJob)
def create_job(job: schemas.CreateJob, db: Session = Depends(database.get_db)):
    return crud.create_job(db=db, job=job)


@router.put("/{id}", response_model=schemas.ShowJob)
def update_job(job_id: int, job: schemas.CreateJob, db: Session = Depends(database.get_db)):
    job_update = crud.update_job(db=db, job=job, job_id=job_id)
    return job_update


@router.delete("/{id}")
def delete_job(job_id, db: Session = Depends(database.get_db)):
    job_delete = delete_job(db, job_id=job_id)
    return job_delete
