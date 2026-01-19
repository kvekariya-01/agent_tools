from flask_restx import Namespace, Resource, fields
from database import SessionLocal
from models.tool_executions import ToolExecution

api = Namespace("tool_executions", description="Tool Execution API")

model = api.model("ToolExecution", {
    "run_id": fields.String,
    "task_id": fields.String,
    "tool_id": fields.String(required=True),
    "input": fields.Raw,
    "output": fields.Raw,
    "status": fields.String,
    "error": fields.String,
    "execution_time_ms": fields.Integer
})

@api.route("/")
class ToolExec(Resource):
    @api.expect(model)
    def post(self):
        data = api.payload
        db = SessionLocal()

        exec = ToolExecution(
            run_id=data.get("run_id"),
            task_id=data.get("task_id"),
            tool_id=data["tool_id"],
            input=data.get("input"),
            output=data.get("output"),
            status=data.get("status", "success"),
            error=data.get("error"),
            execution_time_ms=data.get("execution_time_ms")
        )

        db.add(exec)
        db.commit()
        db.close()

        return {"message": "Tool execution saved"}, 201
