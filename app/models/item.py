from typing import Any, Optional
from bson import ObjectId
from fastapi.encoders import ENCODERS_BY_TYPE, jsonable_encoder
from pydantic import BaseModel, Field, model_validator, root_validator
import pydantic

class Item(BaseModel):
    id: Optional[str] = Field(None, alias="_id", description="Unique identifier")
    name: str = Field(..., min_length=3, max_length=20, description="Item name should be between 3 to 50 characters")
    description: str = Field(None, max_length=200, description="Description should be within 200 characters")
    price: float = Field(..., gt=0, description="Price should be greater than 0")

    @model_validator(mode="before")
    def convert_object_id(cls, values: Any):
        if '_id' in values and isinstance(values['_id'], ObjectId):
            values['_id'] = str(values['_id'])
        return values

    class Config:
        jsonable_encoders = {
            ObjectId: str
        }

# ENCODERS_BY_TYPE[ObjectId] = str