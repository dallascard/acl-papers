import os
import time
from optparse import OptionParser

import wget
from bs4 import BeautifulSoup

from util.common import simple_get


def main():
    usage = "%prog"
    parser = OptionParser(usage=usage)
    parser.add_option('--conf', type=str, default='emnlp',
                      help='Conference: default=%default')
    parser.add_option('--year', type=str, default='2019',
                  help='Year: default=%default')
    (options, args) = parser.parse_args()

    conf = options.conf
    year = str(options.year)
    emnlp_dir = os.path.join('data', conf, year)
    output_dir = os.path.join(emnlp_dir, 'pdfs')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    url = 'https://www.aclweb.org/anthology/events/' + conf + '-' + year + '/index.html'

    raw_html = simple_get(url)
    with open(os.path.join(emnlp_dir, 'index.html'), 'wb') as f:
        f.write(raw_html)
    html = BeautifulSoup(raw_html, 'html.parser')

    pdf_urls = set()
    hrefs = html.findAll('a', {'title': "Open PDF"})
    for href in hrefs:
        url = href.get('href')
        parts = url.split('/')
        name = parts[-1]
        parts = name.split('.')
        if len(parts) == 2:
            if len(parts[0]) == 8 and parts[1] == 'pdf':
                pdf_urls.add(url)

    pdf_urls = list(pdf_urls)
    pdf_urls.sort()

    max_tries = 3

    n_urls = len(pdf_urls)
    print(n_urls, 'pdfs found')
    for url_i, url in enumerate(pdf_urls):
        tries = 0
        success = False
        parts = url.split('/')
        name = parts[-1]
        outfile = os.path.join(output_dir, name)
        if os.path.exists(outfile):
            print("({:d}/{:d}) Skipping {:s}".format(url_i, n_urls, url))
        else:
            while tries < max_tries and not success:
                try:
                    print("({:d}/{:d}) Downloading {:s}".format(url_i, n_urls, url))
                    wget.download(url, out=output_dir)
                    success = True
                    print()
                except Exception as e:
                    print("Download failed on", url)
                    if os.path.exists(outfile):
                        os.remove(outfile)
                    if tries < max_tries:
                        print("Pausing for 3 seconds...")
                        time.sleep(3)
                        tries += 1
                    else:
                        print("Maximum number of tries exceeded on", url)
                        raise e


if __name__ == '__main__':
    main()
