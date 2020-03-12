import os
import re
import glob
import string
from optparse import OptionParser


def main():
    usage = "%prog outfile"
    parser = OptionParser(usage=usage)
    parser.add_option('--conf', type=str, default='emnlp',
                      help='Conference: default=%default')
    parser.add_option('--year', type=str, default='2019',
                      help='Year: default=%default')
    parser.add_option('--query', type=str, default='variational',
                      help='Query string (after removing spaces and punctuation): default=%default')

    (options, args) = parser.parse_args()
    outfile = args[0]

    conf = options.conf
    year = options.year
    query = options.query

    files = glob.glob(os.path.join('data', 'acl', conf, year, 'text', '*.txt'))
    files.sort()
    print(len(files))

    regex = re.compile('[%s]' % re.escape(string.punctuation))

    links = []
    for file_i, infile in enumerate(files):
        if file_i % 100 == 0:
            print('.', end='')
        paper_id = os.path.basename(infile).split('.')[0]
        with open(infile) as f:
            text = f.read()
        text = text.lower()
        text = regex.sub('', text)
        text = re.sub(r'\s', '', text)

        if query in text:
            links.append('https://www.aclweb.org/anthology/' + str(paper_id) + '.pdf')

    print()
    print(len(links))
    with open(outfile, 'w') as f:
        for link in links:
            f.write(link + '\n')


if __name__ == '__main__':
    main()
