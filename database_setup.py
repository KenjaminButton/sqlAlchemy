import sys

from sqlalchemy import
Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()
# insert at the end of file

engine =create_engine(
'sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)





# creating a class and table. 
# Note that this should be placed between the configuration code

class Restaurant(Base): 

__tablename__ = 'restaurant'


class MenuItem(Base):

__tablename__ = 'menu_item'

# mapper code used to create columns in the database
# inside Restaurant Class

name = Column(
String(80), nullable = False)

id = Column (
Integer, primary_key = True)

# Inside Menu Item Class. Still MAPPER. 

name = Column(String(80), nullable = False)
id = Column(Integer, primary_key = True)
course = Column(String(250))
description = Column(String(250))
price = Column(String(8))
restaurant_id = Column (
Integer, ForeignKey('restaurant.id'))
restaurant = relationship(Restaurant)
