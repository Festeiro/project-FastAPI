import datetime

class Product:
    def __init__(self, id: int, product_name: str, description: str, price: float, image_url: str, category: str, date_added: datetime, date_updated: datetime):
        self.id = id
        self.product_name = product_name
        self.description = description
        self.price = price
        self.image_url = image_url
        self.category = category
        self.date_added = date_added
        self.date_updated - date_updated

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, description={self.description}, price={self.price}, image_url={self.image_url}, category={self.category})"
