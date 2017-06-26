from shutil import copyfile, rmtree
import sys
import os
import zipfile
from lxml import etree

# command format: python3 doc_to_text.py Hello.docx


def prepare_zipfile(source_file):
    """
    copies .docx file into a .zip so the xml parsing can be done
    :param source_file: the .docx file
    :return: dest_zip, a file name
    """
    # cut off the .docx, make it a .zip
    dest_zip = os.path.splitext(source_file)[0] + '.zip'
    # make a copy of the .docx and put it in .zip
    copyfile(source_file, dest_zip)
    return dest_zip


def extract_zipfile(source_zip):
    """
    unzips your new zip file into a temporary directory to work in
    :param source_zip: a .zip file
    :return: None. should create a temp dir in the PWD then put the .zip contents in it
    """
    # unzip the .zip
    zip_ref = zipfile.ZipFile(source_zip, 'r')
    zip_ref.extractall('./temp')
    return zip_ref # the zip ref object will need to be closed later.


def parse_xml_t_elements_to_list(source_xml_file):
    """
    where the xml is parsed.
    :param source_xml_file:
    :return: result list. contains each :t element as an individual item in the list
    """
    data = etree.parse(source_xml_file)
    # we'll want to go over all 't' elements in the xml node tree.
    # note that MS office uses namespaces and that the w must be defined in the namespaces dictionary args
    # each :t element is the "text" of the file. that's what we're looking for
    # result is a list filled with the text of each t node in the xml document model
    result = [node.text.strip() for node in
              data.xpath("//w:t", namespaces={'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'})]

    return result


def write_node_list_to_txt_file(node_list, source_zip_dir, zip_manipulator):
    """
    Takes a list of strings (the t elements from the xml tree), joins them with line breaks, then writes them to a .txt file
    :param node_list: a list of t nodes parsed out of xml
    :param source_zip_dir: the name of the .zip file that will have .txt appended to it,
    then have the node_list contents written to it.
    :param zip_manipulator: the zip file manipulator object
    :return: None.
    """
    # dump node_list into a new .txt file
    with open(os.path.splitext(source_zip_dir)[0] + '.txt', 'w') as txt:
        # join the elements of node_list together since txt.write can't take lists
        joined_node_str = '\n'.join(node_list)
        # write it into the new file
        txt.write(joined_node_str)
    # close the zip_manipulator file
    zip_manipulator.close()
    return None


def cleanup(zip_file):
    """
    gets rid of the temp directory and the .zip file
    :param zip_file:
    :return: None
    """
    rmtree('./temp')
    os.remove(zip_file)
    return None

zip_dir = sys.argv[1]
zip_file_location = prepare_zipfile(zip_dir)
zip_ref_obj = extract_zipfile(zip_file_location)
t_elem_node_list = parse_xml_t_elements_to_list(source_xml_file='./temp/word/document.xml')
write_node_list_to_txt_file(t_elem_node_list, zip_file_location,zip_ref_obj)
cleanup(zip_file_location)

