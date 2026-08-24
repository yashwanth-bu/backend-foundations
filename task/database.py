from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# database url : database name, database driver to use
#"postgresql+psycopg://username:password@localhost:5432/mydatabase"
DATABASE_URL = "sqlite:///./tasks.db"

# helps to make connections with sqlite3 database
# uses sqlite3 driver by default
# install psycopg as python env as sqlalchemy, for postgresql it uses by itself
engine = create_engine(
    DATABASE_URL,
    # helps to use multiple threads, by default sqlalchemy use single thread
    connect_args={"check_same_thread": False}
)

# sessionmaker creates a object called SessionLocal (factory), which helps to create multiple other sessions (rooms)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# declarative_base: blueprint helps to config tables through python classed
# acts like registry base that SQLAlchemy uses to know about ORM models.
Base = declarative_base()
# Base is created to track on instance of complete sqlalchemy operations

# helps to create sessions
def get_db():
    db = SessionLocal()
    try:
        # pause the process until is called again
        yield db
    finally:
        db.close()
