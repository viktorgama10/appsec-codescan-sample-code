from fastapi import FastAPI
from .routers import sample, application
from starlette.middleware.cors import CORSMiddleware
from .database import SessionLocal, engine
from starlette.requests import Request
from starlette.responses import Response
from . import models


models.Base.metadata.create_all(bind=engine)


# -----------------------------------------------------------------------------
# APPLICATION OBJECT
# -----------------------------------------------------------------------------
app = FastAPI(
    title="Heimdall Identity Server API",
    description="An identity management microservice written in Python and Cloud Native",
    version="1.0.0",
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url=None
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Cannot establish connection with persistence provider", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# -----------------------------------------------------------------------------
# CORS RULES
# -----------------------------------------------------------------------------
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------------------------------------------------
# ADD ROUTERS
# -----------------------------------------------------------------------------
app.include_router(sample.router, prefix="/api/v1")
app.include_router(application.router, prefix="/api/v1")


