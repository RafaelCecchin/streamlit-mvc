from models.data_loader import load_data
from views.dashboard import view

class OportunidadeController:
    
    def index(self):
        data = load_data()
        view(data)
