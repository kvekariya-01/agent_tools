from flask_restx import Namespace, Resource, fields
from database import SessionLocal
from models.email import EmailSent

api = Namespace("email", description="Email API")

payload_model = api.model("EmailInput", {
    "to_email": fields.String(required=True),
    "subject": fields.String(),
    "body": fields.String()
})

@api.route("/test")
class EmailAPI(Resource):
    @api.expect(payload_model)
    def post(self):
        data = api.payload
        to_email = data["to_email"]
        subject = data.get("subject", "Test Subject")
        body = data.get("body", "Test Body")

        # MOCK RESPONSE
        status = f"Mocked email sent to {to_email}"

        db = SessionLocal()
        try:
            record = EmailSent(
            to_email=to_email,
            subject=subject,
            body=body,
            status="sent"
            )
            db.add(record)
            db.commit()
        finally:
            db.close()

        return {
            "status": status,
            "stored": "in supabase"
        }, 200
