import uuid
from sqlalchemy import Column, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database import Base

class Tool(Base):
    __tablename__ = "tools"  # ✅ fix typo

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(Text, unique=True, nullable=False)
    description = Column(Text)
    module = Column(Text, nullable=False)
    status = Column(Text, default="active")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
