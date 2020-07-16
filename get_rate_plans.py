import requests
import json
import app

api_token = ''
api_url_base = 'https://api.apaleo.com/rateplan/v1/rate-plans/'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {0}'.format(api_token)
}

def get_rate_plans():
    api_url = '{0}'.format(api_url_base)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content)
    else:
        return None

rate_plans = get_rate_plans()

if rate_plans is not None:
    print('Here are the rateplans: ')
    print(rate_plans)
else:
    print('[!] Request failed')