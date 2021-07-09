import re

URL = 'https://github.com/yyx990803/vue-svelte-size-analysis'


# template = 'https://github.com/$username/$repo_name'

# pattern = re.escape(template)
# pattern = re.sub(r'\\\$(\w+)', r'(?P<\1>.*)', pattern)


def extract_data(url: str):
    mypattern = r'^https://github.com/(?P<username>.*)/(?P<repo_name>.*)(?:/(.*)+)?$'
    match = re.match(mypattern, url)
    return match.groupdict() if match is not None else {}


print(extract_data(URL))
