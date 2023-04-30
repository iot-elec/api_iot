import typing

from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.types import Date, Boolean
from sqlalchemy.orm import Mapped, relationship, mapped_column
from src.controller.database.database import Base
from src.model.mixin import DictMixIn
import datetime
from sqlalchemy.dialects.mysql import VARCHAR

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

  inventoryId: Mapped[str] = mapped_column(VARCHAR(63, charset="utf8")) 
  expire: Mapped[datetime.date] = mapped_column(Date)
  manufacturing: Mapped[datetime.date] = mapped_column(Date)
  price: Mapped[float] = mapped_column(Float)
  priceUnit: Mapped[str] = mapped_column(VARCHAR(5, charset="utf8"))
  isBuy: Mapped[bool] = mapped_column(Boolean)

  itemModel: Mapped["ItemModel"] = relationship(back_populates="inventoryModel")

  # def __init__(self, itemModelId: str, inventoryId: str, expire: datetime.date, manufacturing: datetime.date, price: float, )


# "itemModel": 
# 	"itemID": 0,
# 	"itemName": "Extra Mature Cheddar Cheese 400G",
# 	"productDescription": {
# 		"details": "Extra mature Cheddar cheese.100% British milk.\\n Hand selected cheese for a strong and full flavour",
# 		"size": 400,
# 		"unitSize": "G"
# 	},
# 	"allergyInformation": "Contains milk"


class ItemModel(Base, DictMixIn):
    __tablename__ = 'Item'
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True) 
    itemName: Mapped[str] = mapped_column(VARCHAR(127, charset="utf8"))
    details: Mapped[bool] = mapped_column(VARCHAR(1023, charset="utf8"))
    allergyInformation: Mapped[str] = mapped_column(VARCHAR(63, charset="utf8"))

    size: Mapped[int] = mapped_column(Integer)
    unitSize: Mapped[str] = mapped_column(VARCHAR(3, charset="utf8"))
    isActive: Mapped[bool] = mapped_column(Boolean)

    inventoryModel: Mapped["InventoryModel"] = relationship(back_populates="itemModel")

