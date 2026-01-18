from flask_restx import Namespace, Resource, fields
from database import SessionLocal
from models.uploaded_files import UploadedFile

api = Namespace("files", description="File Upload API")

payload_model = api.model("FileUploadInput", {
    "filename": fields.String(required=True),
    "file_type": fields.String()
})

@api.route("/upload")
class FileUploadAPI(Resource):
    @api.expect(payload_model)
    def post(self):
        data = api.payload

        file_name = data["filename"]
        file_type = data.get("file_type", "unknown")

        # Mock values (since no real file is uploaded)
        file_size = 0
        storage_path = f"/mock/path/{file_name}"
        uploaded_by = "test_user"

        db = SessionLocal()
        try:
            record = UploadedFile(
                file_name=file_name,        # ✅ MATCHES DB
                file_type=file_type,
                file_size=file_size,
                storage_path=storage_path,
                uploaded_by=uploaded_by
            )

            db.add(record)
            db.commit()

            return {
                "status": "success",
                "file_name": file_name,
                "stored": "in supabase"
            }, 200

        except Exception as e:
            db.rollback()
            return {
                "status": "error",
                "message": str(e)
            }, 500

        finally:
            db.close()
