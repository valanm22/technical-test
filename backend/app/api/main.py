from fastapi import APIRouter

from app.api.routes import appointments, users

api_router = APIRouter()

api_router.include_router(appointments.router)
api_router.include_router(users.router)
