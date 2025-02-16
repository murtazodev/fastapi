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
        id: 2,
        "title": "Hello World 2",
        "content": "This is my second post",
        "rating": 4
    }
]

@app.get("/hello-world")
async def root():
    return {"message": "Hello Guys!!!"}


@app.get("/posts")
def get_posts():
    return my_posts


@app.post("/posts")
def create_post(post: Post):
    converted_post = post.model_dump()
    converted_post["id"] = randrange(0, 1000000)
    my_posts.append(converted_post)
    return {
        "message": "Post created successfully",
        "that_post" : converted_post
    }

pprint(my_posts)
print(len(my_posts))