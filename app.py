from flask import Flask
from flask_restx import Api
from asgiref.wsgi import WsgiToAsgi

from database import Base, engine  # ✅ import Base and engine
from routes.knowledge import api as knowledge_ns
from routes.health import api as health_ns
from routes.email import api as email_ns
from routes.visualization import api as visualization_ns
from routes.web_search import api as web_search_ns
from routes.sql_exec import api as sql_exec_ns
from routes.files import api as files_ns
from routes.tools import api as tools_ns
from routes.tool_executions import api as tool_exec_ns
from routes.api_request_logs import api as api_logs_ns

# -----------------------------
# CREATE TABLES
# -----------------------------
Base.metadata.create_all(bind=engine)  # ✅ create all tables at startup

def create_app():
    app = Flask(__name__)

    api = Api(
        app,
        title="AGENT TOOLS POST API",
        version="1.0",
        description="Centralized Agent Tools API",
        doc="/docs"   # Swagger UI
    )

    api.add_namespace(health_ns, path="/api/health")
    api.add_namespace(knowledge_ns, path="/api/knowledge")
    api.add_namespace(email_ns, path="/api/email")
    api.add_namespace(visualization_ns, path="/api/visualization")
    api.add_namespace(web_search_ns, path="/api/web_search")
    api.add_namespace(sql_exec_ns, path="/api/sql_exec")
    api.add_namespace(files_ns, path="/api/files")
    api.add_namespace(tools_ns, path="/api/tools")
    api.add_namespace(tool_exec_ns, path="/api/tool_executions")
    api.add_namespace(api_logs_ns, path="/api/api_request_logs")

    return app

app = create_app()
asgi_app = WsgiToAsgi(app)
