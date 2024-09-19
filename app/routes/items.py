from fastapi import APIRouter, HTTPException
from ..models.item import Item 
from ..db import get_collection 
from typing import List
import logging
from bson import ObjectId

router = APIRouter()

COLLECTION_NAME = 'items'

@router.get('/{id}', response_model=Item)
async def get_item(id: str):
    try:
        collection = get_collection(COLLECTION_NAME)
        if collection is None:
            raise HTTPException(status_code=404, detail="No collection found")
        item = collection.find_one({ "_id": ObjectId(id)})
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return item
    except Exception as e:
        logging.info(f"API exception caught: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/', response_model=List[Item])
async def get_items():
    try:
        collection = get_collection(COLLECTION_NAME)
        if collection is None:
            raise HTTPException(status_code=404, detail="No collection found")
        logging.info(f"Collection: {collection}")
        items = list(collection.find())        
        logging.info(f"Items: {items}")
        if not items:
            raise HTTPException(status_code=404, detail="No item found")
        return items    
    except Exception as e:
        logging.info(f"API exception caught: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/", response_model=Item)
async def create_item(item: Item):    
    try:
        collection = get_collection(COLLECTION_NAME)
        if collection is None:
            raise HTTPException(status_code=404, detail="No collection found")
        result = collection.insert_one(item.model_dump())
        inserted_item = collection.find_one({ "_id": ObjectId(result.inserted_id)})
        if inserted_item is not None:
            return inserted_item 
        raise HTTPException(status_code=404, detail="Item save failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.put("/{id}", response_model=Item)
async def update_item(id: str, item: Item):
    try:
        collection = get_collection(COLLECTION_NAME)
        if collection is None:
            raise HTTPException(status_code=404, detail="No collection found")
        result = collection.update_one(
                    { "_id": ObjectId(id)}, 
                    {"$set": item.model_dump()
                })
        logging.info(f"Update status: {result}")
        if result["modified_count"] == 0:
            raise HTTPException(status_code=400, detail="Failed to update")
        updated_item = collection.find_one({ "_id": ObjectId(id)})
        if updated_item is not None:
            return updated_item 
        raise HTTPException(status_code=404, detail="Item save failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))