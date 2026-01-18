from flask_restx import Namespace, Resource, fields
from database import SessionLocal
from models.tool_executions import ToolExecution

api = Namespace("tool_executions", description="Tool Execution Logs API")

payload = api.model("ToolExecutionInput", {
    "tool_id": fields.String(required=True),
    "input": fields.Raw,
    "output": fields.Raw,
    "status": fields.String,
    "error": fields.String,
    "execution_time_ms": fields.Integer
})

@api.route("/create")
class ToolExecutionAPI(Resource):
    @api.expect(payload)
    def post(self):
        data = api.payload
        db = SessionLocal()

        try:
            log = ToolExecution(
                tool_id=data["tool_id"],
                input=data.get("input"),
                output=data.get("output"),
                status=data.get("status", "success"),
                error=data.get("error"),
                execution_time_ms=data.get("execution_time_ms")
            )

            db.add(log)
            db.commit()

            return {"status": "success", "message": "Execution logged"}, 201

        except Exception as e:
            db.rollback()
            return {"status": "error", "message": str(e)}, 500

        finally:
            db.close()
