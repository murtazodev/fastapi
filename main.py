from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from pprint import pprint

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    rating: Optional[int] = None


my_posts = [
    {
        "id": 1,
        "title": "Hello World",
        "content": "This is my first post",
        "rating": 5
    },
    {
        "id": 2,
        "title": "Hello World 2",
        "content": "This is my second post",
        "rating": 4
    }
]


# get operation
# GET /hello-world
@app.get("/hello-world")
async def root():
    return {"message": "Hello Guys!!!"}


# get all posts
# GET /posts
@app.get("/posts")
def get_posts():
    return my_posts


# get an individual post by id 
# GET /posts/{id}
@app.get("/posts/{id}")
def get_post(id: int):
    for i in my_posts:
        if i["id"] == id:
            return {
                "message": "Post found",  
                "post": i
            }
    return {"message": "Post not found"}


# create a new post
# POST /posts
@app.post("/posts")
def create_post(post: Post):
    converted_post = post.model_dump()
    converted_post["id"] = randrange(0, 1000000)
    my_posts.append(converted_post)
    return {
        "message": "Post created successfully",
        "that_post" : converted_post
    }
