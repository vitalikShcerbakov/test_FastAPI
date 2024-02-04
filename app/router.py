from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import app.crud as crud
import app.models as models
import app.schemas as schemas
from auth.auth import get_current_active_user
from app.database import get_db

router = APIRouter(
    prefix='/v1',
    tags=['FastApi app']
)


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user=user)


@router.get("/users/", response_model=list[schemas.User])
def read_users_all(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.post("/users/items/", response_model=schemas.Item)
def create_item(
    current_user: Annotated[models.User, Depends(get_current_active_user)],
    item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=current_user.id)


@router.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@router.get("/users/items/")
def get_item_for_user_all(
        current_user: Annotated[models.User, Depends(get_current_active_user)],
        db: Session = Depends(get_db),
):
    return crud.get_item(db, user_id=current_user.id)


@router.get("/users/me/")
def get_user_me(
        current_user: Annotated[models.User, Depends(get_current_active_user)],
        db: Session = Depends(get_db),
):
    return crud.get_user(user_id=current_user.id, db=db)
