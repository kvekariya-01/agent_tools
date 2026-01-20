from database import Base, engine
from models.knowledge_queries import KnowledgeQuery
from models.email import EmailSent
from models.visualizations import Visualization
from models.web_search_results import WebSearchResult
from models.sql_executions import SqlExecution
from models.uploaded_files import UploadedFile

Base.metadata.create_all(bind=engine)
print("Tables created")