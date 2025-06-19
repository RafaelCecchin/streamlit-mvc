import pandas as pd

def load_data():
    #Loads sample data for the app.
    data = {
        'Name': ['Welinton', 'Rafael', 'Thiago'],
        'Age': [35, 23, 22],
        'City': ['New York', 'Toronto', 'London']
    }
    return pd.DataFrame(data)