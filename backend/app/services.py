import os
import requests
from dotenv import load_dotenv

load_dotenv()

PERENUAL_API_KEY = os.getenv('PERENUAL_API_KEY')

PERENUAL_BASE_URL = 'https://api.perenual.com'

def get_plant_data(plant_id):
    """ Fetch plant data from Perenual API. """
    headers = {'Authorization': f'Bearer {PERENUAL_API_KEY}'}
    response = requests.get(f'{PERENUAL_BASE_URL}/plants/{plant_id}', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_all_plants():
    """ Fetch data for all plants from Perenual API. """
    headers = {'Authorization': f'Bearer {PERENUAL_API_KEY}'}
    response = requests.get(f'{PERENUAL_BASE_URL}/plants', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
