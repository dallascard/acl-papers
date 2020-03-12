# acl-paper

Scripts for downloading pdfs for all ACL papers from a particular conference / year

Note: this has only been tested on EMNLP 2019

Requirements:
- wget
- bs4
- python-wget

Scripts:
- `download_pdfs.py`: find and download the pdfs; these will be placed in data/\<conference>/\<year>/pdfs/
- `convert_pdfs_to_text.py`: use pdftotext to convert all downloaded pdfs to text, placed in data/\<conference>/\<year>/text/
- `search_papers.py`: quick way to search the resulting text files for a string and output a list of links

Usage (assuming an Anaconda environment):
- `conda create -n acl-papers python=3`
- `conda activate acl-papers`
- `conda install -c conda-forge request beautifulsoup4 python-wget`
- `python download_pdfs.py --conf emnlp --year 2019`
- `python convert_pdfs_to_text.py --conf emnlp --year 2019`
- `python search_papers.py --conf emnlp --year 2019 --query variational output_file_with_links.txt`

