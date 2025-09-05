
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class user(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)