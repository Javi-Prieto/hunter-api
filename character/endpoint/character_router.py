from typing import List

from fastapi import APIRouter, Depends, HTTPException

from character.model.character import CharacterDto, CharacterEntity
from db import Session, get_session

router = APIRouter(prefix='/character')


@router.get('')
def get_all(session: Session = Depends(get_session)) -> List[CharacterDto]:
    characters: List[CharacterEntity] = session.query(CharacterEntity).all()
    if not characters: raise HTTPException(status_code=404, detail="Item not found")
    return [CharacterDto.from_orm(character) for character in characters]


@router.post('')
def create(character: CharacterDto, session: Session = Depends(get_session)) -> CharacterDto:
    to_save = CharacterEntity(name=character.name, age=character.age, nen_type=character.nen_type)
    session.add(to_save)
    return CharacterDto.from_orm(to_save)


@router.delete('/{character_id}')
def delete_by_id(character_id: int, session: Session = Depends(get_session)):
    print(character_id)
    print('hola mundo')
    session.query(CharacterEntity).filter(CharacterEntity.id == character_id).delete()
    return {'success': True}
