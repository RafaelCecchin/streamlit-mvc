from routes import oportunidade_controller

def api_routes(page):
    if page == "Dashboard":
        oportunidade_controller()