from shutil import copyfile, rmtree
import sys
import os
import zipfile
from lxml import etree

# command format: python3 doc_to_text.py Hello.docx

# let's get the file name
zip_dir = sys.argv[1]
# cut off the .docx, make it a .zip
zip_dir_zip_ext = os.path.splitext(zip_dir)[0] + '.zip'
# make a copy of the .docx and put it in .zip
copyfile(zip_dir, zip_dir_zip_ext)
# unzip the .zip
zip_ref = zipfile.ZipFile(zip_dir_zip_ext, 'r')
zip_ref.extractall('./temp')
# get the xml out of /word/document.xml
data = etree.parse('./temp/word/document.xml')
# we'll want to go over all 'p' elements in the xml node tree.
# note that MS office uses namespaces and that the w must be defined in the namespaces dictionary args
# each :t element is the "text" of the file. that's what we're looking for
# result is a list filled with the text of each t node in the xml document model
result = [node.text.strip() for node in data.xpath("//w:t", namespaces={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'})]
# dump result into a new .txt file
with open(os.path.splitext(zip_dir)[0]+'.txt', 'w') as txt:
    # join the elements of result together since txt.write can't take lists
    joined_result = '\n'.join(result)
    # write it into the new file
    txt.write(joined_result)
# close the zip_ref file
zip_ref.close()
# get rid of our mess of working directories
rmtree('./temp')
os.remove(zip_dir_zip_ext)


def prepare_zipfile(source_file):
    # cut off the .docx, make it a .zip
    dest_zip = os.path.splitext(source_file)[0] + '.zip'
    # make a copy of the .docx and put it in .zip
    copyfile(source_file, dest_zip)

