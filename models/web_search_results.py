import uuid
from sqlalchemy import Column, Text, String, Integer, BigInteger, ForeignKey, DateTime, Numeric
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from database import Base



class WebSearchResult(Base):
    __tablename__ = "web_search_results"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    agent_id = Column(UUID(as_uuid=True), ForeignKey("agents.id", ondelete="SET NULL"))

    query = Column(Text, nullable=False)
    results = Column(JSONB)
    source_engine = Column(Text)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
