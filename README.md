# acl-paper

Download pdfs for the ACL papers from a particular conference / year

Note: this has only been tested on EMNLP 2019

Requirements:
- wget
- bs4
- 

`download_pdfs.py`: find and download the pdfs; these will be placed in data/\<conference>/\<year>/pdfs/

`convert_pdfs_to_text.py`: use pdftotext to convert all downloaded pdfs to text, placed in data/\<conference>/\<year>/text/

`search_papers.py`: quick way to search the resulting text files for a string and output a list of links