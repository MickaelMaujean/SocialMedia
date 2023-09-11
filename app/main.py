from fastapi import FastAPI
from . import models
from app.database import engine
from .routers import posts, users, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

#this command is useless with alembic 
models.Base.metadata.create_all(bind=engine) 

app = FastAPI()

#origins = ["https://www.google.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message":"Hello World"}






