from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, UserRole
from app import auth

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")   #Setting up OAuth2

# Step 1: get the current logged in user from the token
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):                                            #Core function that runs on every protected request
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = auth.verify_access_token(token)   #Is token valid?
    if payload is None:
        raise credentials_exception

    email: str = payload.get("sub")    #Does token have an email?
    if email is None:
        raise credentials_exception

    user = db.query(User).filter(User.email == email).first()   #Does user exist?
    if user is None:
        raise credentials_exception

    return user

# Step 2: role guards built on top of get_current_user
def require_admin(current_user: User = Depends(get_current_user)):    #restricts access to admin users only.
    if current_user.role != UserRole.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return current_user

def require_premium(current_user: User = Depends(get_current_user)):   #restricts access to admin & premium users only.
    if current_user.role not in [UserRole.premium, UserRole.admin]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Premium access required"
        )
    return current_user