import networkx as nx
from social_meaning import utils
import pandas as pd


class Society(object):
    def __init__(self, network, agents, methods):
        self.network = network
        nx.set_node_attributes(G=self.network,
                               name='agent',
                               values=agents)
        self.methods = methods

    # todo: make a function to apply functions to all agents, or call
    # methods of all agents.

    def emit(self):
        [data['agent'].emit(self.methods['emit'])
         for name, data in self.network.nodes(data=True)]

    def receive(self):
        [data['agent'].receive(self.methods['receive'])
         for name, data in self.network.nodes(data=True)]

    def update_mind(self):
        [data['agent'].update_mind(self.methods['update mind'])
         for name, data in self.network.nodes(data=True)]

    def step(self):
        self.emit()
        self.receive()
        self.update_mind()

    def mind_similarity(self):
        """
        How similar are the minds in the population to one another?


        """
        df = pd.DataFrame(data=-1,
                          index=self.network.nodes(data=False),
                          columns=self.network.nodes(data=False))
        for index, index_data in self.network.nodes(data=True):
            for column, column_data in self.network.nodes(data=True):
                df.set_value(index, column,
                             utils.edge_similarity(column_data['agent'].mind,
                                                   index_data['agent'].mind))

        return df
