"""
We define our routes for our application in here.
We will use FastAPI's router to define our routes.
"""
from typing import Annotated

from fastapi import Depends, Query
from fastapi.routing import APIRouter

from src.time_service.business_logic import TimeService
from src.time_service.models import DateFromModel

# This is used to group routes together.
# You can have more than one APIRouter, for different parts in your code
router = APIRouter(prefix="/myapp")

@router.get("/current_time/")
async def get_current_time(time_service: TimeService = Depends()):
    """
    Get the current time.

    time_service: This is an example of Dependency Injection.
    Dependency injection starts at the routes. You can have dependency injection in constructors that are called from the routes too.
    """
    return {"current_time": time_service.get_current_time()}


# Here were using query parameters, so you'll use data_offset/?offset=5
@router.get("/date_offset/")
async def get_date_offset(offset: int, time_service: TimeService = Depends()):
    """
    Get the date offset by the offset.

    offset: The offset to add to the current date.
    FastAPI makes it easy to read in variables
    """
    return {"date_offset": time_service.get_date_offset(offset)}

# Here youre using path parameters, so you'd use get_part/year
@router.get("/get_part/{part}")
async def get_date_part(part: str, time_service: TimeService = Depends()):
    """
    Get the date part.

    part: The part of the date to get.
    """
    return {"date_part": time_service.get_date_part(part)}

@router.get("/is_future/")
async def is_future(year: Annotated[int, Query(lt=2025)], time_service: TimeService = Depends()):
    """
    Check if the date is in the future.
    """
    return {"is_future": "No"}

@router.post("/date_from/")
async def get_date_from(date_from: DateFromModel, time_service: TimeService = Depends()):
    """
    Get the date from the date_from.

    date_from: The date to calculate from.
    We can see that FastAPI provides automatic creation of the DateFromModel object.
    This is because it is a pydantic BaseModel.
    """
    return {"date_from": time_service.get_date_from(date_from)}
