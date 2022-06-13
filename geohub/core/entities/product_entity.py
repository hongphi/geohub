from dataclasses import dataclass


@dataclass
class ProductEntity:
    name: str
    price: float
    os: str
