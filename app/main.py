from fastapi import FastAPI

from app.db import database, User

app = FastAPI(title="FastAPI, Docker and Traefik")

@app.get("/")
async def read_root():
    return await User.objects.all()

@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    await User.objects.get_or_create(email="test@test.com")

@app.on_event("shutdown")
async def startup():
    if database.is_connected:
        await database.disconnect()


