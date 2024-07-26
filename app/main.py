from fastapi import FastAPI
from app import models
from app import database
from app.routers import job, user, authentication

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(authentication.router)
app.include_router(job.router)
app.include_router(user.router)


@app.get("/", tags=['Home'])
def home():
    return {"Hello World!"}


# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
#     db_user = crud.create_user(db=db, user=user)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)


# @app.post("/users/", response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED, tags=['Users'])
# def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
#     # db_user = crud.get_user_by_email(email=email, db=db)
#     # if db_user:
#     #     raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(user=user, db=db)
#

# @app.post("/users/")
# def create_user(request: schemas.CreateUser, db: Session = Depends(get_db())):
#     new_user = models.Users(first_name=request.first_name, last_name=request.last_name, email=request.email, password=request.password)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


# @app.get("/users/", response_model=list[schemas.ShowUser], tags=['Users'])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users
#
#
# @app.get("/users/{user_id}", response_model=schemas.ShowUser, tags=['Users'])
# def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_id(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
#     return db_user


#
# @app.post("/users/{user_id}/jobs/", response_model=schemas.ShowJob, tags=['Jobs'])
# def create_user_job(user_id: int, job: schemas.CreateJob, db: Session = Depends(get_db)):
#     return crud.create_user_job(db=db, job=job, user_id=user_id)
#
#
# @app.get("/jobs/", response_model=list[schemas.Job], tags=['Jobs'])
# def read_job(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     jobs = crud.get_jobs(db, skip=skip, limit=limit)
#     return jobs
#
#
# @app.put("/jobs/{id}", response_model=schemas.ShowJob, tags=['Jobs'])
# def update_job(job_id: int, job: schemas.CreateJob, db: Session = Depends(get_db)):
#     job_update = crud.update_job(db=db, job=job, job_id=job_id)
#     return job_update
#
#
# @app.delete("/jobs/{id}", tags=['Jobs'])
# def delete_job(id, db: Session = Depends(get_db)):
#     job_delete = delete_job(db, job_id=id)
#     return job_delete

#
# @app.delete("/users/{id}", tags=['Users'])
# def delete_user(user_id: int, db: Session = Depends(get_db)):
#     user_delete = delete_user(db, user_id=user_id)
#     return user_delete
