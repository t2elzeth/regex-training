from regex_version import extract_data

EXPECTED_RESULT = {
    'username': 'yyx990803',
    'repo_name': 'vue-svelte-size-analysis'
}


def test_url_without_trailing_slash():
    url = 'https://github.com/yyx990803/vue-svelte-size-analysis'
    assert extract_data(url) == EXPECTED_RESULT


def test_url_with_trailing_slash():
    url = 'https://github.com/yyx990803/vue-svelte-size-analysis/pulls'
    assert extract_data(url) == EXPECTED_RESULT


# def test_url_with_trailing_slash_and_url_after_slash():
#     url = 'https://github.com/yyx990803/vue-svelte-size-analysis/pulls/'
#     assert extract_data(url) == EXPECTED_RESULT
