from fastapi import APIRouter, HTTPException
from ..models.item import Item 
from ..db import collection 
from typing import List
import logging

router = APIRouter()

@router.get('/', response_model=List[Item])
async def get_items():
    try:
        if not collection:
            raise HTTPException(status_code=404, detail="No collection found")
        items = list(collection.find())
        if not items:
            raise HTTPException(status_code=404, detail="No item found")
        return items    
    except Exception as e:
        logging.info(f"API exception caught: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/", response_model=Item)
async def create_item(item: Item):
    try:
        result = collection.insert_one(item.model_dump())
        if result:
            return result 
        raise HTTPException(status_code=404, detail="Item save failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))