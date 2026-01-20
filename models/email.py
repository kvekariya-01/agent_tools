import uuid
from sqlalchemy import Column, Text, String, DateTime, CheckConstraint, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database import Base


class EmailSent(Base):
    __tablename__ = "emails_sent"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    agent_id = Column(
        UUID(as_uuid=True),
        ForeignKey("agents.id", ondelete="SET NULL"),
        nullable=True
    )

    to_email = Column(Text, nullable=False)
    subject = Column(Text, nullable=True)
    body = Column(Text, nullable=True)

    status = Column(String, nullable=False, default="queued")  # ✅ IMPORTANT
    error_message = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        CheckConstraint(
            "status IN ('queued', 'sent', 'failed')",
            name="emails_sent_status_check"
        ),
    )
