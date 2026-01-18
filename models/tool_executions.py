import uuid
from sqlalchemy import Column, Text, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from database import Base

class ToolExecution(Base):
    __tablename__ = "tool_executions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # ❌ REMOVE foreign keys for now
    run_id = Column(UUID(as_uuid=True), nullable=True)
    task_id = Column(UUID(as_uuid=True), nullable=True)
    tool_id = Column(UUID(as_uuid=True), nullable=False)

    input = Column(JSONB)
    output = Column(JSONB)

    status = Column(Text, default="success")
    error = Column(Text)
    execution_time_ms = Column(Integer)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
