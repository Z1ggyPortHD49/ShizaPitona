import requests
ip_address = '8.8.8.8'

def get_ip_location(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'fail':
            return f"No data"
        else:
            return f'''
            IP: {ip_address}
            City: {data.get('city', 'NaN')}
            Region: {data.get('regionName', 'NaN')}
            Country: {data.get('country', 'NaN')}
            Location: {data.get('lat', 'NaN')},{data.get('lon', 'NaN')}
            '''


location_info = get_ip_location(ip_address)
print(location_info)