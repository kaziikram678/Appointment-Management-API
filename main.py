from fastapi import FastAPI
from app.routes import router
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Appointment Management API")

# @app.get("/", tags=["Health"])
# async def health_check():
#     return {"message": "Hello World"}


app.include_router(router)
