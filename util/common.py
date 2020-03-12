from requests import get
from requests.exceptions import RequestException
from contextlib import closing


def simple_get(url, as_bytes=True):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        print("Attempting to download", url)
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                if as_bytes:
                    return resp.content
                else:
                    return resp.text
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

    except KeyError as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


def is_int(input_string):
    """
    Check if a string looks like an integer
    :param input_string: str
    :return: True of False
    """
    try:
        int(input_string)
        return True
    except ValueError:
        return False


def get_contents(html):
    # TODO: see if this works in every case
    contents = []
    links = html.find_all('a')
    if len(links) > 0:
        for link in links:
            if len(link.contents) > 0:
                contents.append(str(link.contents[0]))
    else:
        contents = str(html.contents)
    return contents


def remove_url_prefix(url):
    https = False
    www = False
    url = url.lower()
    if url.startswith('https'):
        url = url[5:]
        https = True
    elif url.startswith('http'):
        url = url[4:]
    if url.startswith(':'):
        url = url[1:]
    if url.startswith('/'):
        url = url[1:]
    if url.startswith('/'):
        url = url[1:]
    if url.startswith('www.'):
        url = url[4:]
        www = True
    return url, https, www
