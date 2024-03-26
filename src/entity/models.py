from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), index=True)
    last_name = Column(String(50), index=True)
    email = Column(String(50), index=True)
    phone_number = Column(String(50), index=True)
    birthday = Column(Date, index=True)
    additional_data = Column(Boolean, default=False)





    # id: Mapped[int] = mapped_column(primary_key=True)
    # first_name: Mapped[str] = mapped_column(String(50), index=True)
    # last_name: Mapped[str] = mapped_column(String(50), index=True)
    # email: Mapped[str] = mapped_column(String(50), index=True)
    # phone_number: Mapped[str] = mapped_column(String(50), index=True)
    # birthday: Mapped[int] = mapped_column(String(8), index=True)
    # additional_data: Mapped[bool] = mapped_column(default=False)