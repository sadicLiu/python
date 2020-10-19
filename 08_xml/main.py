import os

from xml.dom.minidom import parse
import xml.dom.minidom


def parse_xml():
    path_xml = './info.xml'

    DOMTree = xml.dom.minidom.parse(path_xml)
    annotation = DOMTree.documentElement

    filename = annotation.getElementsByTagName("filename")[0]
    print(filename.childNodes[0].nodeValue)

    size = annotation.getElementsByTagName("size")[0]
    width = size.getElementsByTagName("width")[0].childNodes[0].nodeValue
    height = size.getElementsByTagName("height")[0].childNodes[0].nodeValue
    depth = size.getElementsByTagName("depth")[0].childNodes[0].nodeValue
    print('width: {}, height: {}, depth: {}'.format(width, height, depth))

    nodes = annotation.getElementsByTagName("object")
    for node in nodes:
        name = node.getElementsByTagName("name")[0].childNodes[0].nodeValue
        box = node.getElementsByTagName("bndbox")[0]
        x1 = box.getElementsByTagName("xmin")[0].childNodes[0].nodeValue
        y1 = box.getElementsByTagName("ymin")[0].childNodes[0].nodeValue
        x2 = box.getElementsByTagName("xmax")[0].childNodes[0].nodeValue
        y2 = box.getElementsByTagName("ymax")[0].childNodes[0].nodeValue
        print('box: {}, {}, {}, {}'.format(x1, y1, x2, y2))


if __name__ == '__main__':
    parse_xml()
