from flask_restx import Namespace, Resource, fields
from database import SessionLocal
from models.web_search_results import WebSearchResult

api = Namespace("web_search", description="Web Search API")

# Swagger model
web_search_model = api.model("WebSearch", {
    "agent_id": fields.String(required=False, description="Agent UUID"),
    "query": fields.String(required=True, description="Search query"),
    "results": fields.Raw(description="Search results JSON"),
    "source_engine": fields.String(description="Search engine name")
})


@api.route("/search")
class WebSearch(Resource):
    @api.expect(web_search_model)
    def post(self):
        data = api.payload
        db = SessionLocal()

        result = WebSearchResult(
            agent_id=data.get("agent_id"),
            query=data["query"],
            results=data.get("results"),
            source_engine=data.get("source_engine")
        )

        db.add(result)
        db.commit()
        db.close()

        return {
            "message": "Web search result saved successfully",
            "id": str(result.id)
        }, 201
