from flask_restx import Namespace, Resource, fields
from database import SessionLocal
from models.uploaded_files import UploadedFile

api = Namespace("files", description="Files API")

model = api.model("UploadedFile", {
    "agent_id": fields.String,
    "file_name": fields.String(required=True),
    "file_type": fields.String,
    "file_size": fields.Integer,
    "storage_path": fields.String,
    "uploaded_by": fields.String
})

@api.route("/upload")
class UploadFile(Resource):
    @api.expect(model)
    def post(self):
        data = api.payload
        db = SessionLocal()

        file = UploadedFile(
            agent_id=data.get("agent_id"),
            file_name=data["file_name"],
            file_type=data.get("file_type"),
            file_size=data.get("file_size"),
            storage_path=data.get("storage_path"),
            uploaded_by=data.get("uploaded_by")
        )

        db.add(file)
        db.commit()
        db.close()

        return {"message": "File uploaded"}, 201
