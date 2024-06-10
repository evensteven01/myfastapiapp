import json
import logging
from typing import Any

from fastapi.responses import JSONResponse
from fastapi import Request

logger = logging.getLogger(__name__)

async def catch_exceptions_middleware(request: Request, call_next) -> Any:
    """
    Middleware to catch exceptions.
    """
    try:
        return await call_next(request)
    except Exception as exc:
        logger.error("Caught exception: %s", exc)
        return JSONResponse(status_code=500, content={"message": "Server error"})

async def log_incoming_message_middleware(request: Request, call_next) -> Any:
    """
    Middleware to log incoming messages.
    """
    logger.debug("Received request: %s", request.url)
    return await call_next(request)

async def filter_requests_middleware(request: Request, call_next) -> Any:
    """
    Middleware to filter requests.
    """
    logger.debug("Filtering request: %s", request.url)
    if request.method == "POST" and request.url.path == "/myapp/date_from/":
        payload_str = await request.body()
        payload = json.loads(payload_str)
        if payload.get("year") > 2024:
            return JSONResponse(
                status_code=403, content={"message": "Year cannot be greater than 2024"}
            )
        
    return await call_next(request)
    
