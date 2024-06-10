"""
Main application module.


"""
from contextlib import asynccontextmanager
import logging
from typing import Any

from fastapi.applications import FastAPI

from src.fe.fe import configure_frontend
from src.fe.routes import router as static_router
from src.time_service.routes import router as time_router
from src.settings import get_settings, Settings
from src.middleware import catch_exceptions_middleware, filter_requests_middleware, log_incoming_message_middleware


logger = logging.getLogger(__name__) # This will give us a logger named after the module name.

class MyApp(FastAPI):
    """Main application class."""
    def __init__(self, *args, **kwargs):
        print("Creating application.")
        self._settings = get_settings()
        super().__init__(*args, **kwargs)

    def setup(self):
        """
        Set up the application.
        Things to set up here include logging, middleware.
        # This gets called during creation of the app itself.
        Its called before lifespan.

        Middleware should be configured here because in lifespan its too late, as the app is already starting up.
        Middleware must be loaded before the app is starting up.
        """
        print("Setting up application.")
        setup_logging(self._settings)
        configure_middleware(self)
        configure_frontend(self)
        logger.debug("Logging set up.")

@asynccontextmanager
async def lifespan(my_app: MyApp):  # type: ignore
    """
    Application lifespan context manager.
    This will start to run during startup, before the app is ready to serve requests.

    After the app is shutting down, it can also spin down the app's resources.
    """
    print(f"Lifespan starting up for app: {my_app}")
    configure_routes(my_app)
    yield
    print("Lifespan shutting down")

def configure_routes(app: MyApp) -> None:
    """Configure the routes for the application."""
    logger.debug("Configuring routes.")
    app.include_router(time_router)
    app.include_router(static_router)


def setup_logging(settings: Settings):
    """Sets up logging"""

    logging.basicConfig(level=logging.DEBUG)

def configure_middleware(app: MyApp):
    """
    Configure middleware for the application.
    Middleware is code that runs before and after a request is processed.
    Middleware is reversed in reverse order, so anything you want to run first should be added last.
    """
    app.middleware("http")(catch_exceptions_middleware)
    app.middleware("http")(log_incoming_message_middleware)
    app.middleware("http")(filter_requests_middleware)
    logger.debug("Configuring middleware.")
