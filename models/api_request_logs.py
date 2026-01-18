import uuid
from sqlalchemy import Column, Text, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from database import Base

class ApiRequestLog(Base):
    __tablename__ = "api_request_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    api_name = Column(Text, nullable=False)
    endpoint = Column(Text, nullable=False)

    request_payload = Column(JSONB)
    response_payload = Column(JSONB)

    status_code = Column(Integer)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
