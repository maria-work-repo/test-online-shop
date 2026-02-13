from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal


class CategoryCreate(BaseModel):
    """
    Model for creating and updating a category.
    Used in POST and PUT requests.
    """
    name: str = Field(
        ..., 
        min_length=3, 
        max_length=50,
        description="Category name (3–50 characters)"
    )
    parent_id: int | None = Field(
        None, 
        description="ID of the parent category, if applicable"
    )


class Category(BaseModel):
    """
    Model for returning category data.
    Used in GET requests.
    """
    id: int = Field(
        ..., 
        description="Unique category identifier"
    )
    name: str = Field(
        ..., 
        description="Category name"
    )
    parent_id: int | None = Field(
        None, 
        description="ID of the parent category, if applicable"
    )
    is_active: bool = Field(
        ..., 
        description="Category active status"
    )

    model_config = ConfigDict(from_attributes=True)


class ProductCreate(BaseModel):
    """
    Model for creating and updating a product.
    Used in POST and PUT requests.
    """
    name: str = Field(
        ..., 
        min_length=3, 
        max_length=100,
        description="Product name (3–100 characters)"
    )
    description: str | None = Field(
        None, 
        max_length=500,
        description="Product description (up to 500 characters)"
    )
    price: Decimal = Field(
        ..., 
        gt=0, 
        description="Product price (greater than 0)", 
        decimal_places=2
    )
    image_url: str | None = Field(
        None, 
        max_length=200, 
        description="Product image URL"
    )
    stock: int = Field(
        ..., 
        ge=0, 
        description="Stock quantity (0 or more)"
    )
    category_id: int = Field(
        ..., 
        description="ID of the category the product belongs to"
    )


class Product(BaseModel):
    """
    Model for returning product data.
    Used in GET requests.
    """
    id: int = Field(
        ..., 
        description="Unique product identifier"
    )
    name: str = Field(
        ..., 
        description="Product name"
    )
    description: str | None = Field(
        None, 
        description="Product description"
    )
    price: Decimal = Field(
        ..., 
        description="Product price", 
        gt=0, 
        decimal_places=2
    )
    image_url: str | None = Field(
        None, 
        description="Product image URL"
    )
    stock: int = Field(
        ..., 
        description="Stock quantity"
    )
    category_id: int = Field(
        ..., 
        description="Category ID"
    )
    is_active: bool = Field(
        ..., 
        description="Product active status"
    )

    model_config = ConfigDict(from_attributes=True)
