from flask_restx import Namespace, Resource, fields
from database import SessionLocal
from models.api_request_logs import ApiRequestLog

api = Namespace("api_request_logs", description="API Request Logs")

payload = api.model("ApiRequestLogInput", {
    "api_name": fields.String(required=True),
    "endpoint": fields.String(required=True),
    "request_payload": fields.Raw,
    "response_payload": fields.Raw,
    "status_code": fields.Integer
})

@api.route("/create")
class ApiRequestLogAPI(Resource):
    @api.expect(payload)
    def post(self):
        data = api.payload
        db = SessionLocal()

        try:
            log = ApiRequestLog(
                api_name=data["api_name"],
                endpoint=data["endpoint"],
                request_payload=data.get("request_payload"),
                response_payload=data.get("response_payload"),
                status_code=data.get("status_code")
            )

            db.add(log)
            db.commit()

            return {"status": "success", "message": "API log saved"}, 201

        except Exception as e:
            db.rollback()
            return {"status": "error", "message": str(e)}, 500

        finally:
            db.close()
