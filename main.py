from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine
from router import router
from auth.auth import auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
app.include_router(auth)


