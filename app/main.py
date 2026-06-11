from fastapi import FastAPI
from app.routers import users, admin
from app.database import engine, Base


Base.metadata.create_all(bind=engine)   #Create all database tables


app = FastAPI(
    title="User Management API",
    description="A role-based user management system with Admin, Standard and Premium roles",
    version="1.0.0"
)                            #Create the FastAPI app instance


# Register routers
app.include_router(users.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])

# Root endpoint
@app.get("/")
def root():
    return {"message": "User Management API is running"}