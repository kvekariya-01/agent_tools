from database import SessionLocal, engine
from models.knowledge_queries import KnowledgeQuery
from models.email import EmailSent
from models.visualizations import Visualizationisualizations
from models.web_search_results import WebSearchResult
from models.sql_executions import SqlExecution
from models.uploaded_files import UploadedFile

db = SessionLocal()
try:
    try:
        print("Knowledge Queries:", db.query(KnowledgeQuery).count())
    except Exception as e:
        print("Knowledge Queries: Error -", str(e))
    try:
        print("Email Tests:", db.query(EmailSent).count())
    except Exception as e:
        print("Email Tests: Error -", str(e))
    try:
        print("Visualization Tests:", db.query(Visualizationisualizations).count())
    except Exception as e:
        print("Visualization Tests: Error -", str(e))
    try:
        print("Web Search Tests:", db.query(WebSearchResult).count())
    except Exception as e:
        print("Web Search Tests: Error -", str(e))
    try:
        print("SQL Executions:", db.query(SqlExecution).count())
    except Exception as e:
        print("SQL Executions: Error -", str(e))
    try:
        print("File Uploads:", db.query(UploadedFile).count())
    except Exception as e:
        print("File Uploads: Error -", str(e))
finally:
    db.close()