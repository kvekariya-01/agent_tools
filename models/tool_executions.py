import uuid
from sqlalchemy import Column, Text, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from database import Base


class ToolExecution(Base):
    __tablename__ = "tool_executions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    run_id = Column(
        UUID(as_uuid=True),
        ForeignKey("agent_runs.id", ondelete="SET NULL"),
        nullable=True
    )

    #run_id = Column(UUID(as_uuid=True), nullable=True)

    # 🔥 FIX: remove FK to agent_tasks
    task_id = Column(UUID(as_uuid=True), nullable=True)

    tool_id = Column(String, nullable=False)
    input = Column(JSONB, nullable=True)
    output = Column(JSONB, nullable=True)
    status = Column(String, nullable=True)
    error = Column(Text, nullable=True)
    execution_time_ms = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
