from flask_restx import Namespace, Resource, fields
from database import SessionLocal
from models.sql_executions import SqlExecution

api = Namespace("sql_exec", description="SQL Execution API")

payload_model = api.model("SqlExecInput", {
    "query": fields.String(required=True)
})

@api.route("/test")
class SqlExecAPI(Resource):
    @api.expect(payload_model)
    def post(self):
        data = api.payload
        query = data["query"]

        db = SessionLocal()
        try:
            record = SqlExecution(
                query=query,
                execution_status="success",
                rows_affected=1,
                error_message=None
            )
            db.add(record)
            db.commit()
        finally:
            db.close()

        return {
            "query": query,
            "stored": True
        }, 200
