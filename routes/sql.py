from flask_restx import Namespace, Resource, fields
from tools.sql_tools import SQLTool

api = Namespace("SQL", description="Safe SQL execution")
tool = SQLTool()

model = api.model("SQLQuery", {
    "query": fields.String(required=True)
})

@api.route("/execute")
class ExecuteSQL(Resource):
    @api.expect(model)
    def post(self):
        return tool.execute(api.payload)
