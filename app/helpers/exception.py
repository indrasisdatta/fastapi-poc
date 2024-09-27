
import logging
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

async def custom_validation_excetion_handler(request: Request, exc: RequestValidationError):
    errors = {}
    logging.info(f"Custom validation error: {exc.errors()}")
    for error in exc.errors():
        errors[error["loc"][-1]] = error["msg"]
    return JSONResponse(status_code=422, content={"errors": errors})