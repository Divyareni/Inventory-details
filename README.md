# 🛠️ Inventory Details

A FastAPI-based application demonstrating CRUD operations for managing product inventory, with a PostgreSQL database backend. Ideal for learning FastAPI, database integration, and building RESTful APIs.


---

## ✅ Features

- **CRUD Operations**: Create, Read, Update, Delete products
- **Database Integration**: PostgreSQL backend
- **FastAPI**: High-performance API with automatic docs
- **SQLAlchemy**: ORM for database interaction
- **Pydantic**: Data validation and serialization

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.7+
- PostgreSQL
- pip (Python package installer)

---

### 🔧 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Divyareni/Inventory-details.git
   cd Inventory-details
   
2. Set up a virtual environment:

   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install dependencies:

   pip install -r requirements.txt

4. Configure PostgreSQL:

   ## Create a new database: ##

   CREATE DATABASE inventory;

   Update your database connection settings in database.py:

   SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/inventory"

### Running the Application ###

Start the FastAPI application:

uvicorn main:app --reload


Access the interactive API documentation at: http://127.0.0.1:8000/docs

### API Endpoints ###
Method	Endpoint	Description
POST	/products/	Create a new product
GET	/products/	Get all products
GET	/products/{id}	Get a specific product
PUT	/products/{id}	Update a product
DELETE	/products/{id}	Delete a product

