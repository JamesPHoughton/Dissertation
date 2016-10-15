import networkx as nx
from matplotlib import animation, rc
import matplotlib.pylab as plt
rc('animation', html='html5')

class ThresholdModel(object):

    def __init__(self, g, fractional_threshold=None, numerical_threshold=None):
        """
        Parameters
        ----------
        g: networkx graph
        fractional_threshold: list of numbers
            these are values between 0 and 1 representing the fraction of the neighbors who need
            to be activated before the focal node will become activated.
            For these thresholds, adopters are
        numerical_threshold: list of integers
            these are
            This innovation from Centola and Macy 2007


        """
        self.g = g
        if fractional_threshold:
            fractional_threshold_dict = dict(zip(g.nodes(), fractional_threshold))
            nx.set_node_attributes(self.g, 'fractional threshold', fractional_threshold_dict)
        else:
            nx.set_node_attributes(self.g, 'fractional threshold', 0)

        if numerical_threshold:
            numerical_threshold_dict = dict(zip(g.nodes(), numerical_threshold))
            nx.set_node_attributes(self.g, 'numerical threshold', numerical_threshold_dict)
        else:
            nx.set_node_attributes(self.g, 'numerical threshold', 0)

        nx.set_node_attributes(self.g, 'adopting', False)

    def seed(self, nodes=None):
        for n in nodes:
            self.g.node[n]['numerical threshold'] = 0
            self.g.node[n]['fractional threshold'] = 0
            self.g.node[n]['adopting'] = True

    def draw(self):
        key = {False: 'b', True: 'r'}
        colors = [key[self.g.node[n]['adopting']] for n in self.g.nodes()]
        nx.draw_circular(self.g, alpha=.6, node_color=colors)

    def step(self):
        def decide(g, n):
            neighbors = g.neighbors(n)
            num_neighbors = len(neighbors)
            numerical_threshold = g.node[n]['numerical threshold']
            fractional_threshold = g.node[n]['fractional threshold']
            adopting = sum([g.node[neighbor]['adopting'] for neighbor in neighbors])
            return (adopting >= (fractional_threshold * num_neighbors) and
                    adopting >= numerical_threshold )

        new_state = dict(zip(self.g.nodes(), [decide(self.g, n) for n in self.g.nodes()]))
        nx.set_node_attributes(self.g, 'adopting', new_state)

    def num_rioting(self):
        return sum([self.g.node[n]['rioting'] for n in self.g.nodes()])

    def _frame(self):
        self.step()
        self.draw()

    def run(self, steps=20, animate=True):
        if animate:
            fig, ax = plt.subplots()
            anim = animation.FuncAnimation(fig, self._frame(),
                                           frames=steps, interval=2000, blit=False)
            return anim
        else:
            for i in range(steps):
                self.step()
