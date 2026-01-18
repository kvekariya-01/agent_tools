from flask_restx import Namespace, Resource, fields
from database import SessionLocal
from models.knowledge_queries import KnowledgeQuery

api = Namespace("knowledge", description="Knowledge API")

payload_model = api.model("KnowledgeInput", {
    "query": fields.String(required=True)
})

@api.route("/query")
class KnowledgeAPI(Resource):
    @api.expect(payload_model)
    def post(self):
        data = api.payload
        query = data["query"]

        # MOCK RESPONSE
        answer = f"Mocked answer for query: {query}"

        db = SessionLocal()
        try:
            record = KnowledgeQuery(
                query_text=query,
                response=answer,
                source="api"
            )
            db.add(record)
            db.commit()
        finally:
            db.close()

        return {
            "answer": answer,
            "status": "stored in supabase"
        }, 200
