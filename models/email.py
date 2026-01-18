import uuid
from sqlalchemy import Column, Text, String, Integer, BigInteger, ForeignKey, DateTime, Numeric
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from database import Base


class EmailSent(Base):
    __tablename__ = "emails_sent"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    agent_id = Column(UUID(as_uuid=True), ForeignKey("agents.id", ondelete="SET NULL"))

    to_email = Column(Text, nullable=False)
    subject = Column(Text)
    body = Column(Text)

    status = Column(String)
    error_message = Column(Text)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
