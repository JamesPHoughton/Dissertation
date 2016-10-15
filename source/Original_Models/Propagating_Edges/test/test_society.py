import unittest
import networkx as nx
from social_meaning.agent import Agent


class TestSocietyBasicOperation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from social_meaning.society import Society
        network = nx.star_graph(2)
        agents = {0: Agent(mental_graph=nx.house_graph(),
                           social_network=network,
                           node_name=0),
                  1: Agent(mental_graph=nx.Graph(),
                           social_network=network,
                           node_name=1),
                  2: Agent(mental_graph=nx.Graph(),
                           social_network=network,
                           node_name=2)
                  }
        methods = {'emit': 'all to neighbors',
                   'receive': 'all equally',
                   'update mind': 'union'}

        cls.s = Society(network, agents, methods)

    def test_setup(self):

        self.assertEqual(self.s.network.node[0]['agent'].mind.nodes(),
                         list(range(5)))

        self.assertEqual(self.s.network.node[1]['agent'].mind.nodes(),
                         list())

    def test_emit(self):
        self.s.emit()
        # check emitting to both neighbors
        self.assertSetEqual(set(self.s.network.node[0]['agent'].emissions),
                            set([1, 2]))

        self.assertSetEqual(set(self.s.network.node[0]['agent'].emissions[1]),
                            set(nx.house_graph().edges()))

        # emissions of empty graphs should be empty,
        # but should still have an emissions dictionary
        self.assertSetEqual(set(self.s.network.node[1]['agent'].emissions[0]),
                            set())

    def test_receive(self):
        self.s.receive()
        # check emitting to both neighbors
        self.assertSetEqual(set(self.s.network.node[0]['agent'].receipts),
                            set([1, 2]))

        self.assertSetEqual(set(self.s.network.node[0]['agent'].receipts[1]),
                            set())

        # emissions of empty graphs should be empty,
        # but should still have an emissions dictionary
        self.assertSetEqual(set(self.s.network.node[1]['agent'].receipts[0]),
                            set(nx.house_graph().edges()))

    def test_update_mind(self):
        self.s.update_mind()
        self.assertEqual(self.s.network.node[1]['agent'].mind.nodes(),
                         list(range(5)))

        # the 'sender' still has their original
        self.assertEqual(self.s.network.node[0]['agent'].mind.nodes(),
                         list(range(5)))

    def test_mind_similarity(self):
        # todo: test this with an actually interesting set of networks
        similarity_matrix = self.s.mind_similarity()
        repr(similarity_matrix)
