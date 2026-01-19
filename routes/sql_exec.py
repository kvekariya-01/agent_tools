from flask_restx import Namespace, Resource, fields
from database import SessionLocal
from models.sql_executions import SqlExecution

api = Namespace("sql_exec", description="SQL Execution API")

model = api.model("SqlExecution", {
    "agent_id": fields.String,
    "query": fields.String(required=True),
    "execution_status": fields.String,
    "rows_affected": fields.Integer,
    "error_message": fields.String
})

@api.route("/run")
class RunSQL(Resource):
    @api.expect(model)
    def post(self):
        data = api.payload
        db = SessionLocal()

        execution = SqlExecution(
            agent_id=data.get("agent_id"),
            query=data["query"],
            execution_status=data.get("execution_status"),
            rows_affected=data.get("rows_affected"),
            error_message=data.get("error_message")
        )

        db.add(execution)
        db.commit()
        db.close()

        return {"message": "SQL execution logged"}, 201
