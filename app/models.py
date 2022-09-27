""" Scraper model."""

from sqlalchemy import Column, Integer, String
from config.database import engine, Base


class Posts(Base):
    """ Create scraper model."""
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(500))
    link = Column(String(500))
    nb_likes = Column(Integer)
    nb_comments = Column(Integer)
    date = Column(String(50))
    time = Column(String(50))


Base.metadata.create_all(engine)
