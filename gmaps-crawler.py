from outscraper import ApiClient


api_cliet = ApiClient(api_key='KEY_FROM_OUTSCRAPER')
response = api_cliet.google_maps_search(
    'Motor Repair Shop near Bantul Regency, ID',
    language='en',
    region='id',
    limit=100
)
