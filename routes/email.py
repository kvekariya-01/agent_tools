from flask_restx import Namespace, Resource, fields
from database import SessionLocal
from models.email import EmailSent

api = Namespace("email", description="Email APIs")

email_model = api.model("EmailSend", {
    "agent_id": fields.String(required=True),
    "to_email": fields.String(required=True),
    "subject": fields.String(required=True),
    "body": fields.String(required=True),
})


@api.route("/send")
class SendEmail(Resource):

    @api.expect(email_model)
    def post(self):
        db = SessionLocal()
        data = api.payload

        try:
            email = EmailSent(
                agent_id=data["agent_id"],
                to_email=data["to_email"],
                subject=data["subject"],
                body=data["body"],
                status="queued",   # ✅ DB ke hisab se
                error_message=None
            )

            db.add(email)
            db.commit()
            db.refresh(email)

            return {
                "message": "Email queued successfully",
                "email_id": str(email.id),
                "status": email.status
            }, 201

        except Exception as e:
            db.rollback()
            return {"error": str(e)}, 500

        finally:
            db.close()
