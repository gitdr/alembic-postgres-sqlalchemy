from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import os

from models.user import Address

def get_url():
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "")
    server = os.getenv("POSTGRES_SERVER", "db")
    db = os.getenv("POSTGRES_DB", "app")
    return f"postgresql://{user}:{password}@{server}/{db}"


engine = create_engine(get_url(), echo=True)

with Session(engine) as session:
    patrick = Address(
        postcode = "fdsafad",  
        key = "fdsasfda", 
        value = 10
    )

    session.add_all([patrick])
    session.commit()