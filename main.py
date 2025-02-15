from fastapi import FastAPI

app = FastAPI()


@app.get("/hello-world")
async def root():
    return {"message": "Hello Guys!!!"}

@app.get("/posts")
def get_posts():
    return [
        {
            "title": "Hello World",
            "content": "This is my first post"
        },
        {
            "title": "Hello World 2",
            "content": "This is my second post"
        }
    ]