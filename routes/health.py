from flask_restx import Namespace, Resource
from logger import logger

api = Namespace("health", description="Health Check")

@api.route("/check")
class Health(Resource):
    def get(self):
        logger.info("HEALTH CHECK HIT")
        return {
            "service": "Agent Tools",
            "status": "UP"
        }, 200
