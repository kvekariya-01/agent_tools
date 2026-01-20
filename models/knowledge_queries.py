import uuid
from sqlalchemy import Column, Text, String, Integer, BigInteger, ForeignKey, DateTime, Numeric
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from database import Base


class KnowledgeQuery(Base):
    __tablename__ = "knowledge_queries"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    agent_id = Column(UUID(as_uuid=True), ForeignKey("agents.id", ondelete="SET NULL"))

    query_text = Column(Text, nullable=False)
    source = Column(Text)
    response = Column(Text)
    confidence_score = Column(Numeric(5, 2))

    created_at = Column(DateTime(timezone=True), server_default=func.now())
