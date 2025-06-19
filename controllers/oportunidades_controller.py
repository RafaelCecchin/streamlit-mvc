from models.data_loader import load_data
from views.dashboard import view

def oportunidade_controller():
    data = load_data()
    view(data)