def api_routes(app):
    @app.get("/api")
    async def api_home():
        return {"message": "API Home"}
