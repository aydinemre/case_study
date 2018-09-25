"""
This code generated for an case study in 25 September 2018

To run this code install dependencies.
Dependencies can be found in requirements.txt
"""

from collections import Counter

# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

print(__doc__)


def show_df_info(df):
    """

    :param df:
    :return:
    """
    print("Total row in excel : %d" % df.shape[0])
    print("*" * 20)
    print("Head of data frame: ")
    print(df.head())
    print("*" * 20)
    print(df.info())
    print("*" * 20)
    print(df.info())
    print("*" * 20)


def df_to_graph(df):
    """

    :param df:
    :return:
    """
    rows = df.values.tolist()
    graph = nx.Graph()
    graph.add_edges_from(rows)
    return graph


def get_neighbours(graph):
    all_neighbours = {}
    for node in graph.nodes:
        neighbors = [n for n in graph.neighbors(node)]
        all_neighbours[node] = neighbors
    return all_neighbours


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--data', type=str, default="./datasets/bristol_adjacency.xlsx")
    parser.add_argument('--draw', dest='draw', action='store_true')

    args = parser.parse_args()
    print("Args : {}".format(args))

    df = pd.read_excel(args.data)
    show_df_info(df)

    graph = df_to_graph(df)
    degree_sequence = Counter(dict(graph.degree))
    most_influential = degree_sequence.most_common(1)

    print("Most Influential Peel : {}".format(most_influential[0][0]))

    all_clusters = get_neighbours(graph)

    neigh_df = pd.DataFrame.from_dict(all_clusters, orient='index')
    neigh_df.to_csv("passenger_clusters.csv", sep=" ", header=None, quoting=3)

    if args.draw:
        plt.figure(figsize=(20, 10))
        nx.draw_networkx(graph, edge_color='.1', with_labels=True)
        plt.show()
