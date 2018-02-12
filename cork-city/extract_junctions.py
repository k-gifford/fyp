#!/usr/bin/env python

# script to extract all junctions from the osm.net file and insert
# them into a seperate xml file.
import xml.etree.ElementTree as ET

# creates an element tree from the xml document passed in
def create_tree(document):
    tree = ET.ElementTree()
    tree.parse(document)
    return tree

# create a tree iterator, starting at the root of the element tree
# using the tag
def get_tree_iterator(tree, tag):
    root = tree.getroot()
    if(tag):
        return root.getiterator(tag)
    else:
        return root.getiterator()

# recursively remove all children of the element
def remove_all_children(element):
    children = element.getchildren()
    for child in children:
        remove_all_children(child)
        print("removed child: ", element.tag, element.attrib['id'])
        element.remove(child)

# remove all tags from the tree except the tag name you supply
def remove_all_but(tree, tag):
    keep = tag
    root = tree.getroot()
    iterator = root.getiterator()

    for element in iterator:
        tag = element.tag
        if tag != keep and tag != 'request' and tag != 'net' and tag != 'location':
            print("removed: ", element.tag)
            remove_all_children(element)
            root.remove(element)



def main():
    # take in the osm net and parse into tree
    tree = create_tree("osm.net.xml")
    junction_iterator = get_tree_iterator(tree, "junction")
    new_tree = ET.ElementTree()  # new tree to hold junctions
    new_root = ET.Element('net')  # new tree's root element
    new_tree._setroot(new_root)

    # append all the junctions in the network to the new tree
    for j in junction_iterator:
        # print(j.attrib)
        new_root.append(j)

    new_tree.write("junctions.xml")

if __name__ == '__main__':
    main()
