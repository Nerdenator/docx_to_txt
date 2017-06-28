import unittest


class TestDocxToTxt(unittest.TestCase):
    """
    Test suite for docx_to_txt functionality
    """
    def setUp(self):
        """
        Define the test client and other test variables
        :return:
        """
        self.singleLineFileName = "Hello.docx"
        self.multiLineFileName = "HelloMultiLine.docx"

    def test_single_line(self):
        """
        translate .docx to .txt with single line of text.
        :return:
        """
        pass

    def test_single_line_on_multiple_lines(self):
        """
        translate .docx to .txt with single sentence of text on multiple lines.
        :return:
        """
        pass

    def test_multi_line(self):
        """
        translate .docx to .txt with multiple lines, all of them text
        :return:
        """
        pass

    def test_multi_line_with_blank_lines(self):
        """
        translate .docx to .txt with multiple lines, one of them a blank line
        :return:
        """

    def test_single_line_with_formatting(self):
        """
        translate .docx to .txt with single line when the <t> element is formatted
        :return:
        """
        pass

    def test_multi_line_with_formatting(self):
        """
        translate .docx to .txt with multiple lines when the <t> element is formatted
        :return:
        """
        pass

    def test_table_only_one_row_one_column(self):
        """
        make a table out of | and - characters, for 1x1 table
        :return:
        """
        pass

    def test_table_only_one_row_three_column(self):
        """
        make a table out of | and - characters, for 3x1 table
        :return:
        """
        pass

    def test_table_three_row_three_column(self):
        """
        make a table out of | and - characters, for 3x3 table
        :return:
        """
        pass

    def test_one_picture_only(self):
        """
        let's just put the filename in square brackets
        :return:
        """
        pass

    def test_try_to_open_excel_workbook(self):
        """
        ew excel. say no to opening it
        :return:
        """
        pass

if __name__ == '__main__':
    unittest.main()