from flask_restx import Namespace, Resource, fields
from database import SessionLocal
from models.visualizations import Visualization

api = Namespace("visualization", description="Visualization API")

visualization_model = api.model("Visualization", {
    "agent_id": fields.String(required=False, description="Agent UUID"),
    "chart_type": fields.String(required=True),
    "input_data": fields.Raw(required=True),
    "generated_config": fields.Raw(required=False),
    "output_url": fields.String(required=False)
})


@api.route("/create")
class CreateVisualization(Resource):

    @api.expect(visualization_model)
    def post(self):
        db = SessionLocal()
        data = api.payload

        try:
            viz = Visualization(
                agent_id=data.get("agent_id"),
                chart_type=data["chart_type"],
                input_data=data["input_data"],
                generated_config=data.get("generated_config"),
                output_url=data.get("output_url")
            )

            db.add(viz)
            db.commit()

            # 🔥 MOST IMPORTANT LINE
            db.refresh(viz)

            return {
                "message": "Visualization created successfully",
                "id": str(viz.id)
            }, 201

        except Exception as e:
            db.rollback()
            return {"error": str(e)}, 500

        finally:
            db.close()
