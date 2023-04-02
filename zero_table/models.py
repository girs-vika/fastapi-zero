from core.db import Base
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, sql
from sqlalchemy.orm import relationship


class Table(Base):
    __tablename__ = "zero_table"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    value = Column(String)
    date_update = Column(DateTime)
    user = Column(Integer, ForeignKey("user.id"))
    user_id = relationship("User")
