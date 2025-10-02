from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import Alert, Crew, AlertAssignment, AlertOpenRequest
from ..schemas import AssignAlertIn, AssignAlertOut, OpenRequestIn, OpenRequestOut, DecisionIn


router = APIRouter(prefix="/admin", tags=["admin"])


def _require_admin_user_id() -> int:
    # Placeholder: in a real app, extract from auth. For now, raise if not provided.
    # For testing we allow passing X-User-Id header via dependency or use a fixed UUID.
    # Here we use a fixed UUID-like string for seed admin. Replace with real auth later.
    return 1


@router.post("/assign", response_model=AssignAlertOut, status_code=status.HTTP_201_CREATED)
def assign_alert(payload: AssignAlertIn, db: Session = Depends(get_db)):
    admin_user_id = _require_admin_user_id()

    alert = db.get(Alert, payload.alert_id)
    crew = db.get(Crew, payload.crew_id)
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    if not crew:
        raise HTTPException(status_code=404, detail="Crew not found")

    alert.assigned_crew_id = crew.id

    assignment = AlertAssignment(
        alert_id=alert.id,
        crew_id=crew.id,
        assigned_by_user_id=admin_user_id,
        assigned_at=datetime.now(timezone.utc),
    )
    db.add(assignment)
    db.add(alert)
    db.commit()
    db.refresh(assignment)

    return AssignAlertOut(
        id=str(assignment.id),
        alert_id=str(alert.id),
        crew_id=str(crew.id),
        assigned_by_user_id=admin_user_id,
    )


@router.post("/open-request", response_model=OpenRequestOut, status_code=status.HTTP_201_CREATED)
def create_open_request(payload: OpenRequestIn, db: Session = Depends(get_db)):
    admin_user_id = _require_admin_user_id()
    alert = db.get(Alert, payload.alert_id)
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")

    # request_statuses: Pending=code
    status_row = db.execute(
        "SELECT id FROM request_statuses WHERE code = 'Pending'"
    ).first()
    if not status_row:
        raise HTTPException(status_code=500, detail="Missing request status 'Pending'")

    req = AlertOpenRequest(
        alert_id=alert.id,
        requested_by_user_id=admin_user_id,
        requested_at=datetime.now(timezone.utc),
        status_id=status_row[0],
    )
    db.add(req)
    db.commit()
    db.refresh(req)
    return OpenRequestOut(id=str(req.id), alert_id=str(alert.id), status="Pending")


@router.post("/decision")
def decide_open_request(payload: DecisionIn, db: Session = Depends(get_db)):
    admin_user_id = _require_admin_user_id()
    req = db.get(AlertOpenRequest, payload.request_id)
    if not req:
        raise HTTPException(status_code=404, detail="Request not found")

    code = "Approved" if payload.approve else "Rejected"
    status_row = db.execute(
        "SELECT id FROM request_statuses WHERE code = :code", {"code": code}
    ).first()
    if not status_row:
        raise HTTPException(status_code=500, detail=f"Missing request status {code}")

    req.status_id = status_row[0]
    req.approved_by_user_id = admin_user_id
    req.approved_at = datetime.now(timezone.utc)
    db.add(req)
    db.commit()
    return {"ok": True, "status": code}

