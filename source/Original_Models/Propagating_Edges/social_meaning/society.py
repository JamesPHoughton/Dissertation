import networkx as nx


class Society(object):
    def __init__(self, network, agents):
        self.network = network
        nx.set_node_attributes(G=self.network,
                               name='agent',
                               values=agents)

    def emit(self, method):
        """
        Parameters
        ----------
        method: basestring
            options:
            - all to neighbors: shares all edges of the mind network with all edges

        """
        [data['agent'].emit(method)
         for name, data in self.network.nodes(data=True)]

    def receive(self, method):
        """
        Parameters
        ----------
        method: basestring
            options:
            - 'all equally': samples all neighbors for their edges, weighting them equally

        Returns
        -------

        """
        [data['agent'].receive(method)
         for name, data in self.network.nodes(data=True)]

    def update_mind(self, method):
        [data['agent'].update_mind(method)
         for name, data in self.network.nodes(data=True)]