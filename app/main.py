from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api.routes import router as api_router
from app.config import settings
from utils.logger import setup_logger

logger = setup_logger(__name__)

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

app.include_router(api_router, prefix="/api")

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred. Please try again later."},
    )

@app.get("/")
async def root():
    return {"message": "RAG Location Recommender"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)