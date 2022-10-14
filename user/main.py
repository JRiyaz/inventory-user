from fastapi import FastAPI

from user import models, apis
from user.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(apis.router)
