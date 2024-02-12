from typing import List

import uvicorn
from fastapi import FastAPI, Depends

from character.endpoint import character_router
from character.model.character import CharacterEntity, CharacterDto
from db import Base, engine, Session, get_session

app = FastAPI()


app.include_router(router=character_router.router)


@app.on_event('startup')
def create_db():
    Base.metadata.create_all(bind=engine)


# @app.get('/character')
# def getAll(session: Session = Depends(get_session)) -> List[CharacterDto]:
#     characters: List[CharacterEntity] = session.query(CharacterEntity).all()
#
#     return [CharacterDto.from_orm(character) for character in characters]


if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)
