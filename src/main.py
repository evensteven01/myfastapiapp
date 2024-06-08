import uvicorn

from src.app import MyApp, lifespan

app = MyApp(lifespan=lifespan) # When we create the app, we pass in the lifespan method, which Starlette will call

# For running locally
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=11200)
