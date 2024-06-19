import uvicorn

from fastapi import FastAPI

from app.helpers import models
from app.helpers.database import engine
from app.routers import etudiant

models.Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(etudiant.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)