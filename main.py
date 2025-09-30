from fastapi import FastAPI, Depends
from models import Product
from database import session, engine
import database_models
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
database_models.Base.metadata.create_all(engine)

product_details = [
    Product(id=3, name="phone", description="iphone 11"),
    Product(id=4, name="laptop", description="macbook air")
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()

    count = db.query(database_models.Product).count()
    if count == 0:
        initial_products = [
            Product(id=3, name="phone", description="iphone 11"),
            Product(id=4, name="laptop", description="macbook air")
        ]
        for product in initial_products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()
    db.close()

init_db()

@app.get("/products/")
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(database_models.Product).all()
    return products


@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_products:
        return db_products
    return "not found"

@app.post("/products/")
def add_product(product:Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first() 
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db.commit()
        return "product updated"
    else:
        return "product not found"
    
@app.delete("/products/{id}")
def delete_product(id: int, db : Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first() 
    if db_product:
        db.delete(db_product)
        db.commit()
        return "product deleted"
    else:
        return "not deleted"