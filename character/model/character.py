from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String

from db import Base


class CharacterEntity(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    nen_type = Column(String)
    age = Column(Integer)


class CharacterDto(BaseModel):
    name: str = Field(...)
    age: int = Field(..., gt=0)
    nen_type: str = Field(...)

    class Config:
        from_attributes = True
        orm_mode = True
