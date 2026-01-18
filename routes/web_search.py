from flask_restx import Namespace, Resource, fields
from database import SessionLocal
from models.web_search_results import WebSearchResult

api = Namespace("web_search", description="Web Search API")

payload_model = api.model("WebSearchInput", {
    "query": fields.String(required=True),
    "source_engine": fields.String()
})

@api.route("/test")
class WebSearchAPI(Resource):
    @api.expect(payload_model)
    def post(self):
        data = api.payload

        query = data["query"]
        source_engine = data.get("source_engine", "mock")

        results = {
            "items": [
                {"title": "Result 1", "url": "https://example.com"}
            ]
        }

        db = SessionLocal()
        try:
            record = WebSearchResult(
                query=query,
                results=results,
                source_engine=source_engine
            )
            db.add(record)
            db.commit()
        finally:
            db.close()

        return {
            "query": query,
            "source_engine": source_engine,
            "stored": True
        }, 200
