import uuid
from sqlalchemy import Column, Text, BigInteger, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database import Base


class UploadedFile(Base):
    __tablename__ = "uploaded_files"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    agent_id = Column(UUID(as_uuid=True), ForeignKey("agents.id", ondelete="SET NULL"))

    file_name = Column(Text, nullable=False)   # ✅ CORRECT
    file_type = Column(Text)
    file_size = Column(BigInteger)
    storage_path = Column(Text)
    uploaded_by = Column(Text)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
