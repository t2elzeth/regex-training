import re

URL = 'https://github.com/yyx990803/vue-svelte-size-analysis'


def extract_data(url: str):
    mypattern = r'https://github.com/(?P<username>[^/]*)/(?P<repo_name>[^/]*)'
    match = re.match(mypattern, url)
    return match.groupdict() if match is not None else {}


print(extract_data(URL))
print(extract_data(URL + '/'))
print(extract_data(URL + '/pulls'))
print(extract_data(URL + '/pulls/'))
print(extract_data(URL + '/pulls/ldflsdlflsd/dssfsd'))
