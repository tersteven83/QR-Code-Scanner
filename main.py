import uvicorn

from fastapi import FastAPI

from helpers import models
from helpers.database import engine
from routers import etudiant

models.Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(etudiant.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)