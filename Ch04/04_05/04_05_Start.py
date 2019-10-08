# HTML Parser Module
from html.parser import HTMLParser


class HTMLparser(HTMLParser):
    def handler_starttag(self, tag, attrs):
        print('start tag:', tag)
        for attr in attrs:
            print('attr:', attr)

    def handle_endtab(self, tag):
        print('end tab:', tag)

    def handle_comment(self, data):
        print('comment', data)

    def handle_data(self, data):
        print('Data', data)


parser = HTMLparser()
html = open('sampleHTML.html', 'r')

s = ''
for line in html:
    s += line

parser.feed(s)