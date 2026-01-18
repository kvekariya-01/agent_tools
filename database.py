import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError

load_dotenv()

# -----------------------------
# DATABASE URL
# -----------------------------
DATABASE_URL = os.getenv("DATABASE_URL")

engine = None

if DATABASE_URL:
    try:
        engine = create_engine(
            DATABASE_URL,
            pool_pre_ping=True
        )
        # Test connection
        with engine.connect() as conn:
            print("✅ Supabase DB connected successfully")

    except OperationalError as e:
        print("❌ Supabase connection failed:")
        print(e)
        print("⚠️ Falling back to SQLite")

        engine = create_engine(
            "sqlite:///database.db",
            connect_args={"check_same_thread": False},
            pool_pre_ping=True
        )
else:
    print("⚠️ DATABASE_URL not found, using SQLite")
    engine = create_engine(
        "sqlite:///database.db",
        connect_args={"check_same_thread": False},
        pool_pre_ping=True
    )

# -----------------------------
# SESSION & BASE
# -----------------------------
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

Base = declarative_base()

# -----------------------------
# IMPORTANT: IMPORT ALL MODELS
# -----------------------------
# This registers tables in SQLAlchemy metadata
import models.agents
import models.knowledge_queries
import models.email
import models.visualizations
import models.web_search_results
import models.sql_executions
import models.uploaded_files
import models.tools  # ✅ add Tool model here
import models.tool_executions
import models.api_request_logs
