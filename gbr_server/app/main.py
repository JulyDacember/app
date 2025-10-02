from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers.health import router as health_router
from .routers.users import router as users_router
from .routers.admin import router as admin_router
from .routers.compat_auth import router as compat_auth_router
from .routers.compat_data import router as compat_data_router


def create_app() -> FastAPI:
    application = FastAPI(title="GBR Server")
    
    # CORS middleware
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # In production, specify exact origins
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    application.include_router(health_router)
    application.include_router(users_router, prefix="/users", tags=["users"])
    application.include_router(admin_router)
    application.include_router(compat_auth_router)
    application.include_router(compat_data_router)
    return application


app = create_app()

