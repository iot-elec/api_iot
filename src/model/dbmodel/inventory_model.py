from typing import List

from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.types import Date, Boolean
from sqlalchemy.orm import Mapped, relationship, mapped_column
from src.controller.database.database import Base
from src.model.mixin import DictMixIn
import datetime
from sqlalchemy.dialects.mysql import VARCHAR


from .item_model import ItemModel

# class InventoryModel {
#   List<int> inventoryId;
#   ItemModel itemModel;
#   DateTime? exp;
#   DateTime? mfg;
#   double price;
#   String priceUnit;


class InventoryModel(Base, DictMixIn):
  __tablename__ = 'Inventory'

  id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)

  itemModelId: Mapped[int] = mapped_column(ForeignKey("Item.id"))

  inventoryId: Mapped[str] = mapped_column(String.with_variant(VARCHAR(63, charset="utf8"), "mysql", "mariadb")) 
  expire: Mapped[datetime.date] = mapped_column(Date)
  manufacturing: Mapped[datetime.date] = mapped_column(Date)
  price: Mapped[float] = mapped_column(Float)
  priceUnit: Mapped[str] = mapped_column(String.with_variant(VARCHAR(5, charset="utf8"), "mysql", "mariadb"))
  isBuy: Mapped[bool] = mapped_column(Boolean)

  itemModel: Mapped["ItemModel"] = relationship(back_populates="child")

