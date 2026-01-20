from flask_restx import Namespace, Resource, fields
from database import SessionLocal
from models.web_search_results import WebSearchResult

api = Namespace("web_search", description="Web Search API")

web_search_model = api.model("WebSearch", {
    "agent_id": fields.String(required=False),
    "query": fields.String(required=True),
    "results": fields.Raw(required=False),
    "source_engine": fields.String(required=False)
})


@api.route("/search")
class WebSearch(Resource):

    @api.expect(web_search_model)
    def post(self):
        db = SessionLocal()
        data = api.payload

        try:
            result = WebSearchResult(
                agent_id=data.get("agent_id"),
                query=data["query"],
                results=data.get("results"),
                source_engine=data.get("source_engine")
            )

            db.add(result)
            db.commit()

            # 🔥 MOST IMPORTANT LINE
            db.refresh(result)

            return {
                "message": "Web search result saved successfully",
                "id": str(result.id)
            }, 201

        except Exception as e:
            db.rollback()
            return {"error": str(e)}, 500

        finally:
            db.close()
