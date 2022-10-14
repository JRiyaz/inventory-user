from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from user import crud, schemas
from user.database import db_session

from fastapi import APIRouter

router = APIRouter()


@router.post("/users/", status_code=201, response_model=schemas.CreateUser)
def create_user(user: schemas.CreateUser, db: Session = Depends(db_session)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@router.get("/users/", status_code=200, response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(db_session)):
    # users = crud.get_users(db, skip=skip, limit=limit)
    users = crud.get_users(db)
    return users


@router.get("/users/{user_id}", status_code=200, response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(db_session)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/roles/{user_id}", status_code=200, response_model=list[schemas.CreateRoles] | schemas.CreateRoles)
def read_user(user_id: int, roles: list[schemas.CreateRoles], db: Session = Depends(db_session)):
    db_user = crud.add_roles(db, user_id, roles)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/roles/{user_id}", status_code=200, response_model=schemas.UserWithRoles)
def read_user(user_id: int, db: Session = Depends(db_session)):
    db_user = crud.get_user(db, user_id=user_id)
    db_roles = crud.get_user_roles(db, user_id)
    user = schemas.UserWithRoles(
        email=db_user.email, gender=db_user.gender, is_active=db_user.is_active, roles=db_roles
    )
    return user
