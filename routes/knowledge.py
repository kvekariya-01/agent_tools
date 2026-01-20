from flask_restx import Namespace, Resource, fields
from database import SessionLocal
from models.knowledge_queries import KnowledgeQuery

api = Namespace("knowledge", description="Knowledge API")

model = api.model("KnowledgeQuery", {
    "agent_id": fields.String,
    "query_text": fields.String(required=True),
    "source": fields.String,
    "response": fields.String,
    "confidence_score": fields.Float
})

@api.route("/query")
class Knowledge(Resource):
    @api.expect(model)
    def post(self):
        data = api.payload
        db = SessionLocal()

        q = KnowledgeQuery(
            agent_id=data.get("agent_id"),
            query_text=data["query_text"],
            source=data.get("source"),
            response=data.get("response"),
            confidence_score=data.get("confidence_score")
        )

        db.add(q)
        db.commit()
        db.close()

        return {"message": "Query saved"}, 201
