import uvicorn
from fastapi import FastAPI

from character.endpoint import character_router
from db import Base, engine

app = FastAPI()

app.include_router(router=character_router)
@app.on_event('startup')
def create_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)
