from datetime import datetime, timezone
from typing import Dict, Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import Crew, Board, Employee, Alert

router = APIRouter(prefix="/api/Data", tags=["compat-data"])


@router.post("/getcrews")
def get_crews(db: Session = Depends(get_db)):
    """Get all crews"""
    crews = db.query(Crew).all()
    return [
        {
            "Guid": str(crew.id),
            "DisplayName": crew.name
        }
        for crew in crews
    ]


@router.post("/getboarts")
def get_boards(db: Session = Depends(get_db)):
    """Get all boards"""
    boards = db.query(Board).all()
    return [
        {
            "Guid": str(board.id),
            "DisplayName": board.number_plate or board.model or f"Board {board.id[:8]}"
        }
        for board in boards
    ]


@router.post("/getemployees")
def get_employees(db: Session = Depends(get_db)):
    """Get all employees"""
    employees = db.query(Employee).all()
    return [
        {
            "Guid": str(emp.id),
            "DisplayName": emp.full_name,
            "PersonNum": emp.person_num or ""
        }
        for emp in employees
    ]


@router.post("/startsession")
def start_session(payload: Dict[str, Any], db: Session = Depends(get_db)):
    """Start a session with crew, board, and employees"""
    # App sends device info, crew, board, employees
    device_id = payload.get("DeviceId")
    crew_guid = payload.get("Crew", {}).get("Guid")
    board_guid = payload.get("Board", {}).get("Guid")
    
    print(f"Starting session for device: {device_id}")
    print(f"Crew: {crew_guid}, Board: {board_guid}")
    
    # For now, just return a session token
    return {"SessionToken": "session-token-123"}


@router.post("/getAlertInfo")
def get_alert_info(payload: Dict[str, Any], db: Session = Depends(get_db)):
    """Get alert information"""
    # Return empty alert info for now
    return {
        "alert": None,
        "gbrInfo": {
            "alert": None,
            "alertMesgs": []
        }
    }


@router.post("/updateAlertInfo")
def update_alert_info(payload: Dict[str, Any], db: Session = Depends(get_db)):
    """Update alert information"""
    return {"success": True}


@router.post("/debug")
def debug(payload: Dict[str, Any], db: Session = Depends(get_db)):
    """Debug endpoint"""
    return {"debug": "ok"}


@router.post("/confirmLogout")
def confirm_logout(payload: Dict[str, Any], db: Session = Depends(get_db)):
    """Confirm logout"""
    return {"success": True}


@router.post("/logout")
def logout(payload: Dict[str, Any], db: Session = Depends(get_db)):
    """Logout"""
    return {"success": True}


@router.get("/readImage/{alert_id}/{image_num}")
def read_image(alert_id: str, image_num: int, db: Session = Depends(get_db)):
    """Read alert image"""
    # Return placeholder for now
    return {"image": "placeholder"}
