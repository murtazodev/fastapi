from typing import Optional
from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from random import randrange

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
    return {
        "message": "List of Posts",
        "posts": my_posts
    }


# get an individual post by id 
# GET /posts/{id}
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    for i in my_posts:
        if i["id"] == id:
            return {
                "status_code": status.HTTP_200_OK,  
                "post": i
            }
    return {
            "message": "Post not found",
            "status_code": status.HTTP_404_NOT_FOUND
        }


# create a new post
# POST /posts
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    converted_post = post.model_dump()
    converted_post["id"] = randrange(0, 1000000)
    my_posts.append(converted_post)
    return {
        "message": "Post created successfully",
        "that_post" : converted_post
    }


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    for i in my_posts:
        if i["id"] == id:
            my_posts.remove(i)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

print(len(my_posts))

class Demo:
    def __init__(self, x):
        self.x = x
    def __call__(self, x):
        return x + 1
    
add_one = Demo(9)
print(add_one(9))

    