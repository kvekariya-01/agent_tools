from flask_restx import Namespace, Resource, fields
from database import SessionLocal
from models.visualizations import Visualization

api = Namespace("visualization", description="Visualization API")

payload_model = api.model("VisualizationInput", {
    "chart_type": fields.String(required=True),
    "input_data": fields.Raw(required=True),
})

@api.route("/test")
class VisualizationAPI(Resource):
    @api.expect(payload_model)
    def post(self):
        data = api.payload

        chart_type = data["chart_type"]
        input_data = data["input_data"]

        generated_config = {
            "mock": True,
            "chart": chart_type
        }

        output_url = "https://example.com/chart.png"

        db = SessionLocal()
        try:
            record = Visualization(
                chart_type=chart_type,
                input_data=input_data,
                generated_config=generated_config,
                output_url=output_url
            )
            db.add(record)
            db.commit()
        finally:
            db.close()

        return {
            "status": "Visualization generated",
            "chart_type": chart_type
        }, 200
