from fastapi import APIRouter


router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)


@router.get("/")
async def get_all_categories():
    """
    Returns a list of all product categories.
    """
    return {"message": "List of all categories (stub)"}


@router.post("/")
async def create_category():
    """
    Creates a new category.
    """
    return {"message": "Category created (stub)"}


@router.put("/{category_id}")
async def update_category(category_id: int):
    """
    Updates a category by its ID.
    """
    return {"message": f"Category with ID {category_id} updated (stub)"}


@router.delete("/{category_id}")
async def delete_category(category_id: int):
    """
    Deletes a category by its ID.
    """
    return {"message": f"Category with ID {category_id} deleted (stub)"}
