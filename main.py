import re
from string import Template

import requests

TEMPLATE = Template('https://api.github.com/repos/$username/$repo_name/pulls')
URL = "https://github.com/yyx990803/vue-svelte-size-analysis"

# Generate API URL
mypattern = r'https://github.com/(?P<username>[^/]*)/(?P<repo_name>[^/]*)'
match = re.match(mypattern, URL)
template_data = match.groupdict() if match is not None else {}

api_url = TEMPLATE.substitute(**template_data)
print('Built following API URL: ', api_url)

# Make request to GithubAPI
response = requests.get(api_url).json()
print("This is a list of pull requests: ", response)
