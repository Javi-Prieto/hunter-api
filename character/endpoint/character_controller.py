from typing import List

from fastapi import Depends

from character.model.character import CharacterDto, CharacterEntity
from db import Session, get_session


class CharacterController:
    def getAll(self, session: Session = Depends(get_session)) -> List[CharacterDto]:
        characters = List[CharacterEntity] = session.query(CharacterEntity)

        return [CharacterDto.from_orm(character) for character in characters]

    def create(self, character: CharacterDto, session: Session = Depends(get_session)) -> CharacterDto:
        to_save = CharacterEntity(name=character.name, age=character.age, nen_type=character.nen_type)
        session.add(to_save)
        return CharacterDto.from_orm(to_save)
