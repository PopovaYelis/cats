from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from typing import Dict, Any
from database import Base


class Breed(Base):
    __tablename__ = 'breed'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    def __repr__(self):
        return f"Breed {self.name}"

    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in
                self.__table__.columns}


class Cats(Base):
    __tablename__ = 'cats'
    id = Column(Integer, primary_key=True, index=True)
    cat_name = Column(String, index=True)
    color = Column(String, index=True)
    age = Column(Integer, index=True)
    description = Column(String, index=True)
    breed_id = Column(Integer, ForeignKey('breed.id'))
    breed = relationship("Breed", backref="cats")

    def __repr__(self):
        return f"Cat {self.cat_name}"

    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in
                self.__table__.columns}

