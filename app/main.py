import uvicorn
from fastapi import FastAPI
from app.routes import router
from config.config import initiate_database

app = FastAPI()

app.include_router(router)


@app.on_event("startup")
async def start_db():
    await initiate_database()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
