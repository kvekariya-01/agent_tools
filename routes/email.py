from flask_restx import Namespace, Resource, fields
from database import SessionLocal
from models.email import EmailSent

api = Namespace("email", description="Email API")

email_model = api.model("Email", {
    "agent_id": fields.String(required=False),
    "to_email": fields.String(required=True),
    "subject": fields.String,
    "body": fields.String,
    "status": fields.String,
    "error_message": fields.String
})

@api.route("/send")
class SendEmail(Resource):
    @api.expect(email_model)
    def post(self):
        data = api.payload
        db = SessionLocal()

        email = EmailSent(
            agent_id=data.get("agent_id"),
            to_email=data["to_email"],
            subject=data.get("subject"),
            body=data.get("body"),
            status=data.get("status", "sent"),
            error_message=data.get("error_message")
        )

        db.add(email)
        db.commit()
        db.close()

        return {"message": "Email saved"}, 201
