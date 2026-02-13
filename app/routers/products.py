from fastapi import APIRouter


# Create router for products
router = APIRouter(
    prefix="/products",
    tags=["products"],
)


@router.get("/")
async def get_all_products():
    """
    Returns a list of all products.
    """
    return {"message": "List of all products (stub)"}


@router.post("/")
async def create_product():
    """
    Creates a new product.
    """
    return {"message": "Product created (stub)"}


@router.get("/category/{category_id}")
async def get_products_by_category(category_id: int):
    """
    Returns a list of products in the specified category by its ID.
    """
    return {"message": f"Products in category {category_id} (stub)"}


@router.get("/{product_id}")
async def get_product(product_id: int):
    """
    Returns detailed information about a product by its ID.
    """
    return {"message": f"Product details {product_id} (stub)"}


@router.put("/{product_id}")
async def update_product(product_id: int):
    """
    Updates a product by its ID.
    """
    return {"message": f"Product {product_id} updated (stub)"}


@router.delete("/{product_id}")
async def delete_product(product_id: int):
    """
    Deletes a product by its ID.
    """
    return {"message": f"Product {product_id} deleted (stub)"}
