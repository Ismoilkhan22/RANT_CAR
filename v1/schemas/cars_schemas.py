from core.models.car import Brand, Category, Car, Arenda
from ninja import Schema


class BrandSchemaIn(Schema):
    name: str


class CategorySchemaIn(Schema):
    name: str


class CarSchemaIn(Schema):
    name: str
    brand: str
    ctg: str
    raqam: str
    xk: str
    price: int
    status: bool
    yili: int





