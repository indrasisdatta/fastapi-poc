from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(..., min_length=3, max_length=20, description="Item name should be between 3 to 50 characters")
    description: str = Field(None, max_length=200, description="Description should be within 200 characters")
    price: float = Field(..., gt=0, description="Price should be greater than 0")