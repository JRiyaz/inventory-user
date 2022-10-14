from sqlalchemy.orm import Session

from user import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


def get_users(db: Session):
    return db.query(models.User).all()


def create_user(db: Session, user: schemas.CreateUser):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def add_roles(db: Session, user_id: int, roles: list[schemas.CreateRoles]):
    for role in roles:
        db_roles = models.Role(role=role, user_id=user_id)
        db.add(db_roles)
    db.commit()
    return roles


def get_user_roles(db: Session, user_id: int):
    return db.query(models.Role).filter(models.Role.user_id == user_id).all()
