from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from passlib.apps import custom_app_context as pwd_context

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""


class Category(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    user_id = Column(Integer)

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


# class User(Model):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True)
#     username = Column(String(32), index=True)
#     password_hash = Column(String(64))
#
#     def hash_password(self, password):
#         self.password_hash = pwd_context.encrypt(password)
#
#     def verify_password(self, password):
#         return pwd_context.verify(password, self.password_hash)
#
#     def __repr__(self):
#         return f'{self.id} - {self.username}'
