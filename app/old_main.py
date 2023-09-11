#my_posts = [{"title" : "title of post 1", "content" : "content of post 1", "id" : 1},
#            {"title" : "favorite food", "content" : "I love Pizza", "id" : 2 }
#             ]

#def find_post(id):
#    for p in my_posts:
#        if p['id'] == id:
#            return p
        
#def find_index_post(id):
#    for i, p in enumerate(my_posts):
#        if p['id'] == id:
#            return i



#@app.get("/posts")
#def get_posts():

    #cursor.execute("""SELECT * FROM posts """)
    #posts = cursor.fetchall()
    #return {"data" : posts}

#@app.post("/posts", status_code=status.HTTP_201_CREATED)
#def create_posts(post : Post):
    #new_post = models.Post(title = post.title, content = post.content, published = post.published)
    #cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
    # (post.title, post.content, post.published))
    #new_post = cursor.fetchone()
    #conn.commit()

#handle it wihtout proper database   
#post_dict = post.model_dump()
#post_dict['id'] = randrange(0,100000)
#my_posts.append(post_dict)
#raise HTTPException(status_code=status.HTTP_201_CREATED, detail=f"post created {post_dict['id']}")
 #   return{"data" : new_post}

#@app.get("/posts/{id}")
#def get_post(id : int):
    #cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (str(id))) #convert into str needed because id is int initially
    #post = cursor.fetchone()

#    if not post:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                            detail=f"post with id:{id} was not found")
#    return {"Post detailed" : post}

#def delete_post(id:int):

    #cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING *""", (str(id)))
    #deleted_post = cursor.fetchone()
    #conn.commit() #anytime there is a change in the db !

 #   if deleted_post.first() == None:
 #       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post {id} not found")
    
    
#old code w/o SQL : index = find_index_post(id)
#cmd: my_posts.pop(deleted_post)
#    return Response(status_code=status.HTTP_204_NO_CONTENT)

#@app.put("/posts/{id}")
#def update_post(id:int, post : Post):
    #cursor.execute(""" UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """, 
    #               (post.title, post.content, post.published, str(id)))
    #updated_post = cursor.fetchone()
    #conn.commit()

    #if post == None:
   #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post {id} not found")
    
    #old code w/o SQL:
    #index = find_index_post(id)
    #post_dict = post.model_dump()
    #post_dict['id'] = id
    #my_posts[index] = post_dict

    #return {"post updated !" : post_query.first()}