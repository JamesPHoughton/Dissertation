import networkx as nx
import itertools


class Agent(object):

    def __init__(self, mental_graph, social_network, node_name):
        """

        Parameters
        ----------
        mental_graph: networkx graph
        node: networkx node name for name of node in society
        social_network: reference to social network
        """
        self.mind = mental_graph
        self.name = node_name
        self.social_network = social_network
        self.neighbors = self.social_network.neighbors(self.name)
        self.emissions = {n: [] for n in self.neighbors}
        self.receipts = None

    def emit(self, method):
        if method == 'all to neighbors':
            self.emit_all_to_neighbors()
        else:
            raise NotImplementedError("Method '%s' not implemented" % method)


    def emit_all_to_neighbors(self):
        """
        every neighbor is addressed a signal of every edge in the
        network

        """
        self.emissions = {n: self.mind.edges() for n in self.neighbors}

    def receive(self, method):
        if method == 'all equally':
            self.receive_all_equally()
        else:
            raise NotImplementedError("Method '%s' not implemented" % method)

    def receive_all_equally(self):
        """
        Go to neighbors and see what signals they have for you

        """
        self.receipts = {n: self.social_network.node[n]['agent'].emissions[self.name]
                         for n in self.neighbors}

    def update_mind(self, method):
        if method == 'union':
            self.update_mind_equally()
        else:
            raise NotImplementedError("Method '%s' not implemented" % method)

    def update_mind_equally(self):
        """
        Add all neighbors signals to the mind network, as the union of
        all neighbors' edge suggestions
        """
        self.mind.add_edges_from(itertools.chain(*self.receipts.values()))
