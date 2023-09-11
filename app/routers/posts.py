from .. import models, schemas, oauth2
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import get_db
from typing import List, Optional
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter

router = APIRouter(
    prefix="/posts", #use only if all router use the same path in this file !
    tags=['Posts']
)


@router.get("/", response_model=List[schemas.PostOut]) #we should return a list of posts
def get_posts(db : Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
            limit : int=10, skip : int=0, search : Optional[str]=""):

    posts = db.query(models.Post).all() #return all posts of all users
    #posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all() #return all posts of a specific user

    # we add a query parameter to limit the number of posts we retrieve (define limit in the def with default value)
    # we can also add another param to skip some posts (first 2 for ex) using offset function
    # also filter on a search keyword using .filter(models.Post.title.contains(search))
    # in postman, add posts?limit=xxx&skip=2
    #posts = db.query(models.Post).limit(limit).offset(skip).all() 


    #JOIN posts and votes
    results = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(
            models.Post.id).all()
    return results
    
    #serialized_results = []

    #for post, vote_count in results:
    #    serialized_results.append({
    #        'post_id': post.id,
    #        'post_title': post.title,
    #        'votes': vote_count
    #    })

    #return serialized_results
    #specify left outer / groupby post id / use count from func library and rename it as "votes" with label
    # tips : user print(results) to see the SQL query in the terminal
    # don't forget the .all() to actually run the SQL query 


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ResponsePost)
def create_posts(post : schemas.CreatePost, db : Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    new_post = models.Post(owner_id = current_user.id, **post.model_dump())
    # We need to add owner_id now 

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
    #return{"data" : new_post}

@router.get("/{id}", response_model=schemas.ResponsePost)
def get_post(id : int, db : Session = Depends(get_db)):

    post = db.query(models.Post).filter(models.Post.id == id).first() #.first because we know there is only 1 to get
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id:{id} was not found")
    
    #return {"Post detailed" : post}
    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int, db : Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    deleted_post_query = db.query(models.Post).filter(models.Post.id == id)
    deleted_post = deleted_post_query.first()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post {id} not found")
    
    #We add the logic to make sure the logged in User is deleting his post
    if deleted_post.owner_id != current_user.id:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail=f"Not authorized")
    
    deleted_post_query.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/posts/{id}", response_model=schemas.Post)
def update_post(id:int, updated_post : schemas.CreatePost, db : Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post {id} not found")
    
    post_query.update(updated_post.model_dump(), synchronize_session=False)
    db.commit()

    #return {"post updated, check it out !" : post_query.first( )}
    return post_query.first()