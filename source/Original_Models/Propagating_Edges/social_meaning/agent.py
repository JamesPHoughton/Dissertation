import networkx as nx
import itertools


class Agent(object):

    def __init__(self, mental_graph=None, g=None, node_name=None):
        """

        Parameters
        ----------
        mental_graph: networkx graph
        node: networkx node name for name of node in society
        g: reference to social network
        """
        self.mind = mental_graph
        self.name = node_name
        self.g = g
        self.neighbors = self.g.neighbors(self.name)
        self.emissions = {n: [] for n in self.neighbors}
        self.receipts = None

    def emit(self, method):
        pass

    def emit_all_to_neighbors(self):
        """
        every neighbor is addressed a signal of every edge in the
        network

        """
        self.emissions = {n: self.mind.edges() for n in self.neighbors}

    def receive(self, method):
        pass

    def receive_all_equally(self):
        """
        Go to neighbors and see what signals they have for you

        """
        self.receipts = {n: self.g.node[n]['emissions'][self.name] for n in self.neighbors}

    def update_mind(self):
        pass

    def update_mind_equally(self):
        """
        Add all neighbors signals to the mind network
        """
        self.mind.add_edges_from(itertools.chain(*self.receipts.values()))


class Society(object):

    def __init__(self):
        self.social = nx.connected_watts_strogatz_graph(n=100, k=8, p=.1)
        mentals = dict(zip(self.social.nodes(),
                           [nx.fast_gnp_random_graph(n=40, p=.03) for _ in
                            range(self.social.number_of_nodes())]))
        nx.set_node_attributes(self.social, 'mental', mentals)
