import unittest
import networkx as nx
import itertools


def all_same(iterable):
    it_copy = itertools.tee(iterable, 1)
    return len(set(it_copy)) == 1


class TestAgent(unittest.TestCase):
    def test__init__(self):
        from social_meaning.agent import Agent
        society = nx.watts_strogatz_graph(10, 2, 0)
        a = Agent(mental_graph=nx.fast_gnp_random_graph(10, .1),
                  g=society,
                  node_name=society.nodes()[0])
        repr(a)

    def test_emit_all_to_neighbors(self):
        from social_meaning.agent import Agent
        society = nx.watts_strogatz_graph(10, 2, 0)
        a = Agent(mental_graph=nx.fast_gnp_random_graph(10, .1),
                  g=society,
                  node_name=society.nodes()[0])

        a.emit_all_to_neighbors()
        # check that emissions are going to all neighbors
        self.assertSetEqual(set(a.emissions.keys()),
                            set(society.neighbors(0)))
        # check that all neighbors get the same thing
        self.assertTrue(all_same(a.emissions.values()))
        # check that the emission is the full set of edges
        self.assertSetEqual(set(a.emissions[society.neighbors(0)[0]]),
                            set(a.mind.edges()))

    def test_receive_all_equally(self):
        from social_meaning.agent import Agent
        society = nx.watts_strogatz_graph(10, 2, 0)
        emission_set = {m: {n: [(m, n)] for n in society.nodes()} for m in society.nodes()}

        nx.set_node_attributes(society, 'emissions', emission_set)
        a = Agent(mental_graph=nx.fast_gnp_random_graph(10, .1),
                  g=society,
                  node_name=society.nodes()[0])
        a.receive_all_equally()

        expected = {n: [(n, 0)] for n in society.neighbors(0)}
        actual = a.receipts
        self.assertDictEqual(actual, expected)

    def test_update_mind_equally(self):
        from social_meaning.agent import Agent
        mind = nx.Graph()
        mind.add_nodes_from(range(4))
        society = nx.complete_graph(3)
        a = Agent(mental_graph=mind,
                  g=society,
                  node_name=society.nodes()[0])

        self.assertSequenceEqual(a.mind.edges(), [])
        a.receipts = {1: [(0, 1)], 2: [(0, 1), (0, 2)]}
        a.update_mind_equally()
        self.assertSetEqual(set(a.mind.edges()), set([(0, 1), (0, 2)]))
