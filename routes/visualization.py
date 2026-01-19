from flask_restx import Namespace, Resource, fields
from database import SessionLocal
from models.visualizations import Visualization

api = Namespace("visualization", description="Visualization API")

# Swagger model
visualization_model = api.model("Visualization", {
    "agent_id": fields.String(required=False, description="Agent UUID"),
    "chart_type": fields.String(required=True, description="Type of chart"),
    "input_data": fields.Raw(required=True, description="Input data for chart"),
    "generated_config": fields.Raw(description="Generated chart config"),
    "output_url": fields.String(description="Output image URL")
})


@api.route("/create")
class CreateVisualization(Resource):
    @api.expect(visualization_model)
    def post(self):
        data = api.payload
        db = SessionLocal()

        viz = Visualization(
            agent_id=data.get("agent_id"),
            chart_type=data["chart_type"],
            input_data=data["input_data"],
            generated_config=data.get("generated_config"),
            output_url=data.get("output_url")
        )

        db.add(viz)
        db.commit()
        db.close()

        return {
            "message": "Visualization created successfully",
            "id": str(viz.id)
        }, 201
