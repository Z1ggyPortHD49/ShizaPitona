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
            Status: {data.get('status', 'False')}
            IP: {ip_address}
            City: {data.get('city', 'NaN')}
            Region: {data.get('regionName', 'NaN')}
            Country: {data.get('country', 'NaN')}
            Location: {data.get('lat', 'NaN')},{data.get('lon', 'NaN')}
            Timezone {data.get('timezone', 'NaN')}
            isp: {data.get('isp', 'NaN')}
            org: {data.get('org', 'NaN')}
            as: {data.get('as', 'NaN')}
            Mobile: {data.get('mobile', 'NaN')}
            Proxy: {data.get('proxy', 'NaN')}
            Hosting: {data.get('hosting', 'NaN')}
            '''


location_info = get_ip_location(ip_address)
print(location_info)