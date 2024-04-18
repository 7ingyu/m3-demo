from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from ..connection import db

class Artwork(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    price: Mapped[float] = mapped_column(nullable=True)
    medium: Mapped[str] = mapped_column(nullable=True)
    artist: Mapped[int] = mapped_column(ForeignKey("user.id"))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}