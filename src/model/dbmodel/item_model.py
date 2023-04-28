from typing import List

from sqlalchemy import Integer, String
from sqlalchemy.types import  Boolean
from sqlalchemy.orm import Mapped, relationship, mapped_column
from src.controller.database.database import Base
from sqlalchemy.dialects.mysql import VARCHAR
from src.model.mixin import DictMixIn


from src.model.dbmodel.inventory_model import InventoryModel

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
    id = Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True) 
    itemName: Mapped[str] = mapped_column(String.with_variant(VARCHAR(127, charset="utf8"), "mysql", "mariadb"))
    details: Mapped[bool] = mapped_column(String.with_variant(VARCHAR(1023, charset="utf8"), "mysql", "mariadb"))
    allergyInformation: Mapped[str] = mapped_column(String.with_variant(VARCHAR(63, charset="utf8"), "mysql", "mariadb"))

    size: Mapped[int] = mapped_column(Integer)
    unitSize: Mapped[str] = mapped_column(String.with_variant(VARCHAR(3, charset="utf8"), "mysql", "mariadb"))
    isActive: Mapped[bool] = mapped_column(Boolean)

    inventoryModel: Mapped["InventoryModel"] = relationship(back_populates="parent")


# id: Mapped[int] = mapped_column(primary_key=True)
# children: Mapped[List["Child"]] = relationship()



