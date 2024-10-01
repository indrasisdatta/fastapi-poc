from doctest import debug_script
from fastapi import APIRouter, HTTPException
from ..models.item import Item 
from typing import List
import logging
from bson import ObjectId
from ..helpers.collection_helper import get_collection_api
from bson.errors import InvalidId

router = APIRouter()
COLLECTION_NAME = 'items'

@router.get('/{id}', response_model=Item, summary="Get all items", description="Fetches all items from the database.", tags=["Items"])
async def get_item(id: str):
    try:
        # Check if id is valid object id
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid item object id")
        collection = get_collection_api(COLLECTION_NAME)
        item = collection.find_one({ "_id": ObjectId(id)})
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return item
    except InvalidId as e:
        logging.error(f"Invalid ObjectId: {e}")
        raise HTTPException(status_code=400, detail="Invalid item")
    except Exception as e:
        logging.info(f"API exception caught: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))

@router.get('/', response_model=List[Item])
async def get_items():
    try:
        collection = get_collection_api(COLLECTION_NAME)
        logging.info(f"Collection: {collection}")
        items = list(collection.find())        
        logging.info(f"Items: {items}")
        if not items:
            raise HTTPException(status_code=404, detail="No item found")
        return items    
    except Exception as e:
        logging.info(f"API exception caught: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))
    
@router.post("/", response_model=Item)
async def create_item(item: Item):    
    try:
        collection = get_collection_api(COLLECTION_NAME)
        result = collection.insert_one(item.model_dump())
        inserted_item = collection.find_one({ "_id": ObjectId(result.inserted_id)})
        if inserted_item is not None:
            return inserted_item 
        raise HTTPException(status_code=404, detail="Item save failed")
    except Exception as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
    
@router.put("/{id}", response_model=Item)
async def update_item(id: str, item: Item):
    try:
        # Check if id is valid object id
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid item object id")
        collection = get_collection_api(COLLECTION_NAME)
        result = collection.update_one(
                    { "_id": ObjectId(id)}, 
                    {"$set": item.model_dump()
                })
        logging.info(f"Update status: {result}")
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="No record found to update")
        if result.modified_count == 0:
            raise HTTPException(status_code=400, detail="Update failed")        

        updated_item = collection.find_one({ "_id": ObjectId(id)})
        if updated_item is not None:
            return updated_item 
        raise HTTPException(status_code=404, detail="Item save failed")
    except Exception as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
    
@router.delete('/{id}')
def delete_item(id: str):
    try:
        collection = get_collection_api(COLLECTION_NAME)
        # Check if id is valid
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid item") 
        result = collection.delete_one({ "_id": ObjectId(id) })
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Item not found") 
        
        return {"detail": f"Item with id {id} deleted successfully"}

    except Exception as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))