##
# imports
import sys
import os
import urllib2
import networkx as nx

## constants.
FILE_URL = "https://raw.githubusercontent.com/cBioPortal/oncotree/master/tumor_tree.txt"

## functions

def build_oncotree():

    # load the file.
    req = urllib2.Request(FILE_URL)
    response = urllib2.urlopen(req)
    the_page = response.read()

    # create a graph.
    g = nx.Graph()

    # add root node.
    root = g.add_node("root", {"text":"root"})

    # parse the file.
    line_cnt = 0
    for line in the_page.strip().split("\n"):

        # skip header.
        if line_cnt == 0:
            line_cnt += 1
            continue

        # tokenize.
        tokens = line.strip().split("\t")
        try:
            metamaintype = tokens[5]
        except IndexError:
            metamaintype = None
        try:
            metacolor = tokens[6]
        except IndexError:
            metacolor = None
        try:
            metanci = tokens[7]
        except IndexError:
            metanci = None
        try:
            metaumls = tokens[8]
        except IndexError:
            metaumls = None

        # set root node.
        prev_n = root

        # build nodes all the way down.
        nodes = list()
        for i in range(4):

            # check if empty.
            if tokens[i] == "":
                continue

            # split into two.
            tmp = tokens[i].split("(")
            val = tmp[0].strip()
            key = tmp[1].strip().replace("(","").replace(")","")

            # build node.
            n = g.add_node(key, {
                'text': val,
                'metamaintype': metamaintype,
                'metacolor': metacolor,
                'metanci': metanci,
                'metaumls': metaumls
            })

            # add edge.
            g.add_edge(prev_n, n)

        # increment line count.
        line_cnt += 1

    # return the graph.
    return g