from nanoleaf import setup, Aurora

ips = setup.find_auroras(1)
token = setup.generate_auth_token(ips[0])

print (token)