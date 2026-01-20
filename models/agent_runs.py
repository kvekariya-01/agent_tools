import uuid
from sqlalchemy import Column, Text, String, Integer, DateTime, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database import Base

class Agent(Base):
    __tablename__ = "agent_runs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    name = Column(Text, nullable=False)
    description = Column(Text)
    module = Column(Text)
    sub_module = Column(Text)
    role = Column(Text, nullable=False)

    status = Column(String, default="draft")
    temperature = Column(Numeric)
    max_tokens = Column(Integer)
    system_prompt = Column(Text)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
