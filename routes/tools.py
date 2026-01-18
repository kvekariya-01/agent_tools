from flask_restx import Namespace, Resource, fields
from database import SessionLocal
from models.tools import Tool

api = Namespace("tools", description="Tools API")

payload_model = api.model("ToolInput", {
    "name": fields.String(required=True),
    "description": fields.String(required=True),
    "module": fields.String(required=True),
    "status": fields.String(default="active")
})

@api.route("/create")
class ToolsAPI(Resource):
    @api.expect(payload_model)
    def post(self):
        data = api.payload
        db = SessionLocal()
        try:
            # Check if tool already exists
            existing = db.query(Tool).filter(Tool.name == data["name"]).first()
            if existing:
                return {"status": "exists", "message": "Tool already exists"}, 200

            tool = Tool(
                name=data["name"],
                description=data["description"],
                module=data["module"],
                status=data.get("status", "active")
            )

            db.add(tool)
            db.commit()

            return {"status": "success", "tool": data["name"], "stored": "in supabase"}, 201

        except Exception as e:
            db.rollback()
            return {"status": "error", "message": str(e)}, 500

        finally:
            db.close()
