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
        cls.s = Society(network, agents)

    def test_setup(self):

        self.assertEqual(self.s.network.node[0]['agent'].mind.nodes(),
                         list(range(5)))

        self.assertEqual(self.s.network.node[1]['agent'].mind.nodes(),
                         list())

    def test_emit(self):
        self.s.emit('all to neighbors')
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
        self.s.receive('all equally')
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
        self.s.update_mind('union')
        self.assertEqual(self.s.network.node[1]['agent'].mind.nodes(),
                         list(range(5)))

        # the 'sender' still has their original
        self.assertEqual(self.s.network.node[0]['agent'].mind.nodes(),
                         list(range(5)))
