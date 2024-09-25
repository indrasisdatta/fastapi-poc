from fastapi import HTTPException
from ..db import get_collection 

def get_collection_api(collection):
    collection = get_collection(collection)
    if collection is None:
        raise HTTPException(status_code=404, detail="No collection found")
    return collection 

