from datetime import datetime, timezone
from typing import Dict, Any

from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import User
from ..security import verify_password, create_access_token

router = APIRouter(prefix="/api/Auth", tags=["compat-auth"])


@router.get("/checkVersion/{version}", status_code=status.HTTP_200_OK)
def check_version(version: str):
    # The app expects HTTP 200 to consider server reachable.
    return {"ok": True, "version": version, "ts": datetime.now(tz=timezone.utc).isoformat()}


@router.post("/login")
def login(payload: Dict[str, Any], db: Session = Depends(get_db)):
    # App sends: {"Login": "email", "Password": "password"}
    email = payload.get("Login")
    password = payload.get("Password")
    
    if not email or not password:
        return {"error": "Missing credentials"}
    
    # Find user by email
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return {"error": "User not found"}
    
    # Check if password is null or empty
    if not user.hashed_password:
        return {"error": "Password not set for user"}
    
    if not verify_password(password, user.hashed_password):
        return {"error": "Invalid password"}
    
    # Create token
    token = create_access_token(str(user.id))
    
    # App expects { "AuthToken": "..." }
    return {"AuthToken": token}


@router.post("/checkToken")
def check_token(payload: Dict[str, Any]):
    # App sends: {"AuthToken": "token"}
    token = payload.get("AuthToken")
    
    if not token:
        return {"error": "Missing token"}
    
    # For now, just return success if token exists
    # In real app, you'd verify the JWT token
    return {"valid": True, "token": token}

