from typing import List

from fastapi import APIRouter

from character.endpoint.character_controller import CharacterController
from character.model.character import CharacterDto

router = APIRouter(prefix='/character')
character_controller = CharacterController()


router.add_api_route(path='', endpoint=character_controller.getAll(), methods=['GET'], response_model=List[CharacterDto])