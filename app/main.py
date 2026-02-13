from fastapi import FastAPI

from app.routers import categories, products


# Create FastAPI application
app = FastAPI(
    title="FastAPI Online Store",
    version="0.1.0",
)

# Include category routes
app.include_router(categories.router)
app.include_router(products.router)


# Root endpoint for health check
@app.get("/")
async def root():
    """
    Root route confirming that the API is running.
    """
    return {"message": "Welcome to the Online Store API!"}
