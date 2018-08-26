from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Category(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    user_id = Column(Integer)
    items = relationship('Item', cascade="all, delete-orphan")

    def __repr__(self):
        return self.name


class Item(Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False)
    description = Column(String(564), default='Default description')
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship("Category")
    user_id = Column(Integer)

    def __repr__(self):
        return f'{self.title} ({self.id}) - {self.category.name}'
