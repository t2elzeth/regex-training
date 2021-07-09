from urllib.parse import urlparse
from string import Template
import requests

API_URL_TEMPLATE = "https://api.github.com/repos/{username}/{repo_name}/pulls"

TEMPLATE = Template('https://api.github.com/repos/$username/$repo_name/pulls')
URL = "https://github.com/yyx990803/vue-svelte-size-analysis"

# Generate API URL
url_path = urlparse(URL).path
splitted_url = url_path.split("/")
username = splitted_url[1]
repo_name = splitted_url[2]

api_url = API_URL_TEMPLATE.format(username=username, repo_name=repo_name)
print("Built following API URL: ", api_url)
print('Built following API URL2: ', TEMPLATE.substitute(username=username, repo_name=repo_name))

# Make request to GithubAPI
# response = requests.get(api_url).json()
# print("This is a list of pull requests: ", response)
