from fastapi import APIRouter


router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)


@router.get("/")
async def get_all_categories():
    return {"message": "List of all categories (stub)"}


@router.post("/")
async def create_category():
    return {"message": "Category created (stub)"}


@router.put("/{category_id}")
async def update_category(category_id: int):
    return {"message": f"Category with ID {category_id} updated (stub)"}


@router.delete("/{category_id}")
async def delete_category(category_id: int):
    return {"message": f"Category with ID {category_id} deleted (stub)"}
