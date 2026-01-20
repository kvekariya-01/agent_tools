import uuid
from sqlalchemy import Column, Text, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from database import Base


class WebSearchResult(Base):
    __tablename__ = "web_search_results"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    agent_id = Column(
        UUID(as_uuid=True),
        ForeignKey("agents.id", ondelete="SET NULL"),
        nullable=True
    )

    query = Column(Text, nullable=False)
    results = Column(JSONB, nullable=True)
    source_engine = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
