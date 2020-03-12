import os
import glob
import subprocess
from optparse import OptionParser


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

    base_dir = os.path.join('data', conf, year)
    pdf_dir = os.path.join(base_dir, 'pdfs')
    text_dir = os.path.join(base_dir, 'text')
    if not os.path.exists(text_dir):
        os.makedirs(text_dir)

    files = glob.glob(os.path.join(pdf_dir, '*.pdf'))
    files.sort()
    for infile in files:
        basename = os.path.basename(infile)
        name = os.path.splitext(basename)[0]
        parts = name.split('-')
        num = parts[1]
        # skip the Proceedings file
        if num == '1000':
            print("Skipping", infile)
        else:
            cmd = ['pdftotext', infile, os.path.join(text_dir, name + '.txt')]
            print(' '.join(cmd))
            subprocess.call(cmd)


if __name__ == '__main__':
    main()
