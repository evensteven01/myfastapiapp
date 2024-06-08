"""TimeService business logic"""

from datetime import datetime
from datetime import timedelta

from fastapi import Depends

from src.settings import get_settings, Settings
from src.time_service.models import DateFromModel


class TimeService:
    """Our TimeService business logic"""
    def __init__(self, settings: Settings = Depends(get_settings)):
        """
        Constructor for our TimeService class.
        We can see another example of Dependency Injection here.
        This works because TimeService is created within the route.

        Depenendencies can be classes or functions.
        """
        self.settings = settings

    def get_current_time(self):
        """
        Get the current time.
        """
        return f"Current time is {datetime.now()}"

    def get_date_offset(self, offset: int):
        """
        Get the date offset by the offset.
        """
        now = datetime.now()
        new_date = now + timedelta(days=offset)

        return f"Date offset by {offset} is {new_date}"

    def get_date_from(self, date_from: DateFromModel):
        """
        Get the date from the date_from.
        """
        date = datetime(year=date_from.year, month=date_from.month, day=date_from.day)

        return f"Date from {date_from} is {date}"
    
    def get_date_part(self, part: str):
        """
        Get the date part.
        """
        now = datetime.now()
        if part == "year":
            return now.year
        elif part == "month":
            return now.month
        elif part == "day":
            return now.day
        else:
            return f"Invalid part: {part}"

