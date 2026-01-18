import uuid
from sqlalchemy import Column, Text, String, Integer, BigInteger, ForeignKey, DateTime, Numeric
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from database import Base



class Visualization(Base):
    __tablename__ = "visualizations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    agent_id = Column(UUID(as_uuid=True), ForeignKey("agents.id", ondelete="SET NULL"))

    chart_type = Column(Text, nullable=False)
    input_data = Column(JSONB, nullable=False)
    generated_config = Column(JSONB)
    output_url = Column(Text)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
