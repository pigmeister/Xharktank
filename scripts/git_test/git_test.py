import json
import requests

r = requests.post(url="https://api.github.com/repos/pigmeister/node-weather-website/pulls",
        headers={
            "Authorization": "Bearer {0}".format('ghs_XI8qtJG3Q7QVFRZjnfVB5CjTAMCMFd4XznlD'),
            "Content-Type": "application/json"
        },
        data=json.dumps({
            "title": "Test PR",
            "body": "This is a test PR",
            "head": "test-head",
            "base": "test-base",
        })
    )

print(r)

if not r.ok:
    print("Request Failed: {0}".format(r.text))
else:
    print(r.text)