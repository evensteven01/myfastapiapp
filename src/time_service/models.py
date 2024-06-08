"""
This module contains the pydantic model for the DateFromModel.

We can consider these models the contract for the API.
It can define what we receive and what we write.
"""
from pydantic import BaseModel

class DateFromModel(BaseModel):
    year: int
    month: int
    day: int
