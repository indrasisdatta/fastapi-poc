from fastapi import FastAPI, UploadFile
from fastapi.exceptions import RequestValidationError

from app.helpers.exception import custom_validation_excetion_handler
from .routes import items
from .db import startup_db_client, shutdown_db_client

app = FastAPI()

app.add_event_handler('startup', startup_db_client)
app.add_event_handler('shutdown', shutdown_db_client)

# Include the custom exception handler globally
app.add_exception_handler(RequestValidationError, custom_validation_excetion_handler)

# Include routes
app.include_router(items.router, prefix="/items", tags=["Items"])

@app.get('/')
def home():
    return { 'data': 'Welcome to Fast API home' }

# @app.get('/contact')
# def contact():
#     return { 'data': 'Welcome to Fast API contact' }

# @app.post('/upload')
# def uploadFile(files: list[UploadFile]):
#     print('Uploaded files: ', files)

# import uvicorn
# uvicorn.run(app)