from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str | None = None


class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str | None

    class Config:
        from_attributes = True


class AssignAlertIn(BaseModel):
    alert_id: str
    crew_id: str


class AssignAlertOut(BaseModel):
    id: str
    alert_id: str
    crew_id: str
    assigned_by_user_id: int


class OpenRequestIn(BaseModel):
    alert_id: str


class OpenRequestOut(BaseModel):
    id: str
    alert_id: str
    status: str


class DecisionIn(BaseModel):
    request_id: str
    approve: bool

