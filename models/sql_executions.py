import uuid
from sqlalchemy import Column, Text, String, Integer, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database import Base


class SqlExecution(Base):
    __tablename__ = "sql_executions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    agent_id = Column(UUID(as_uuid=True), ForeignKey("agents.id", ondelete="SET NULL"))

    query = Column(Text, nullable=False)

    execution_status = Column(String)     # ✅ MATCHES DB
    rows_affected = Column(Integer)       # ✅ MATCHES DB
    error_message = Column(Text)           # ✅ MATCHES DB

    created_at = Column(DateTime(timezone=True), server_default=func.now())
