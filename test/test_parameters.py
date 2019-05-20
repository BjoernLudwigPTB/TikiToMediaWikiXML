import sys
from subprocess import check_output


class TestMath:

    def test_minimal_call(self):
        check_output(
            [sys.executable, "tikiToMwiki.py",
             "https://fb1-7.bs.ptb.de/tiki/",
             "./test/math/math.tar"])

    def test_stdout_call(self):
        expected_win = '<mediawiki ' \
                       'xml:lang="en">\r\n<siteinfo>\r\n<base>https://fb1-7.' \
                       'bs.ptb.de/tiki/</base>\r\n</siteinfo>\r\n<page>\r\n' \
                       '<title>Math testpage</title>\r\n<revision>\r\n<id>1' \
                       '</id>\r\n<timestamp>2018-03-12T12:38:31Z</timestamp>' \
                       '\r\n<contributor><username>mustermann</username>' \
                       '</contributor>\r\n<text xml:space="preserve">\r\n' \
                       '__TOC__\r\n\r\n{{mathjax}}\r\n\r\na(t) = \\frac{1}{2}' \
                       '\\left[\r\n\r\na_1 sin(\\omega t) + a_2 sin(\\omega ' \
                       't - \\varphi_0)\r\n\r\n\\right]\r\n\r\n{{/mathjax}}' \
                       '\r\n\r\n</text>\r\n</revision>\r\n</page>\r\n' \
                       '</mediawiki>\r\n\r\nnumber of pages = 1 number of ' \
                       'versions = 1\r\nwith contributions by [\'mustermann' \
                       '\']\r\nand file uploads on these pages: dict_keys([])' \
                       '\r\n'.encode()
        expected_lin = '<mediawiki xml:lang="en">\n<siteinfo>\n<base>' \
                       'https://fb1-7.bs.ptb.de/tiki/</base>\n</siteinfo>\n' \
                       '<page>\n<title>Math testpage</title>\n<revision>\n' \
                       '<id>1</id>\n<timestamp>2018-03-12T12:38:31Z' \
                       '</timestamp>\n<contributor><username>mustermann' \
                       '</username></contributor>\n<text xml:space=' \
                       '"preserve">\n__TOC__\n\n{{mathjax}}\n\na(t) = ' \
                       '\\frac{1}{2}\\left[\n\na_1 sin(\\omega t) + a_2 sin(' \
                       '\\omega t - \\varphi_0)\n\n\\right]\n\n{{/mathjax}}' \
                       '\n\n</text>\n</revision>\n</page>\n</mediawiki>\n\n' \
                       'number of pages = 1 number of versions = 1\nwith ' \
                       'contributions by [\'mustermann\']\nand file uploads ' \
                       'on these pages: dict_keys([])\n'.encode()
        result = check_output(
            [sys.executable, "tikiToMwiki.py", "-o", "-",
             "https://fb1-7.bs.ptb.de/tiki/", "./test/math/math.tar"])
        assert (result == expected_lin or result == expected_win)
