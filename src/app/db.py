import os
from databases import Database
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
from sqlalchemy.sql import func

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://hello_fastapi:hello_fastapi@db/hello_fastapi_dev')

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()

notes = Table(
    'notes',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(50)),
    Column('description', String(50)),
    Column('created_date', DateTime, default=func.now(), nullable=False),
)

# async database
database = Database(DATABASE_URL)
