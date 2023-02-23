import pixela_api_handler as pixela
import json

pixela.set_username("namtest")
pixela.set_token("namtest1")

response = pixela.create_user()

print(response.status_code)
print(json.dumps(response.json(), indent=4, default=str))
