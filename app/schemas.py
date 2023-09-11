from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    email : EmailStr
    password :str


class UserOut(BaseModel): #Response the user will receive (he does not want to see his password sent back)
    email : EmailStr
    id : int
    created_at : datetime

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email : EmailStr
    password : str

class PostBase(BaseModel):
    title : str
    content : str
    published : bool = True


class CreatePost(PostBase):
    pass

# Pydantic model for the response
class ResponsePost(BaseModel):
    id : int
    owner_id : int
    title : str
    content : str
    owner : UserOut #make sure to put User classes before to retrieve User info from UserOut class
    class Config:
        from_attributes = True

class Post(PostBase):
    id : int
    #created_at : datetime
    #owner_id : int

    #to make sure it converts to dict() - see doc
    class Config:
        from_attributes = True

class PostOut(BaseModel):
    Post: ResponsePost
    votes: int




class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[str] = None


class Vote(BaseModel):
    post_id : int
    dir : int

