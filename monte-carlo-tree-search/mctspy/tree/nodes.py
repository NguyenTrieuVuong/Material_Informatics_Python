import numpy as np
from collections import defaultdict
from abc import ABC, abstractmethod

class MonteCarloTreeSearchNode(ABC):

    def __init__(self, state, parent=None):
        """
        Parameters
        ----------
        state : mctspy.games.common.TwoPlayersAbstractGameState
        parent : MonteCarloTreeSearchNode
        """
        self.state = state
        self.parent = parent
        self.children = []

    @property
    @abstractmethod
    def untried_actions(self):
        """
        Returns a list of untried actions for the current node.
        """
        pass

    @property
    @abstractmethod
    def q(self):
        """
        Returns the Q value of the current node.
        """
        pass

    @property
    @abstractmethod
    def n(self):
        """
        Returns the number of visits to the current node.
        """
        pass

    @abstractmethod
    def expand(self):
        """
        Expands the current node by selecting an untried action and creating a new child node.
        """
        pass

    @abstractmethod
    def is_terminal_node(self):
        """
        Checks if the current node is a terminal node (end of the game).
        """
        pass

    @abstractmethod
    def rollout(self):
        """
        Simulates a random rollout from the current node until the end of the game and returns the result.
        """
        pass

    @abstractmethod
    def backpropagate(self, reward):
        """
        Backpropagates the result of a rollout to update the node's statistics.
        """
        pass

    def is_fully_expanded(self):
        """
        Checks if all possible actions from the current node have been tried.
        """
        return len(self.untried_actions) == 0

    def best_child(self, c_param=1.4):
        """
        Selects the child node with the highest UCB1 value.
        """
        choices_weights = [
            (c.q / c.n) + c_param * np.sqrt((2 * np.log(self.n) / c.n))
            for c in self.children
        ]
        return self.children[np.argmax(choices_weights)]

    def rollout_policy(self, possible_moves):        
        """
        Randomly selects a move from the list of possible moves during the rollout.
        """
        return possible_moves[np.random.randint(len(possible_moves))]


class TwoPlayersGameMonteCarloTreeSearchNode(MonteCarloTreeSearchNode):

    def __init__(self, state, parent=None):
        super().__init__(state, parent)
        self._number_of_visits = 0.
        self._results = defaultdict(int)
        self._untried_actions = None

    @property
    def untried_actions(self):
        """
        Overrides the base class method to get untried actions from the game state.
        """
        if self._untried_actions is None:
            self._untried_actions = self.state.get_legal_actions()
        return self._untried_actions

    @property
    def q(self):
        """
        Calculates and returns the Q value of the current node.
        """
        wins = self._results[self.parent.state.next_to_move]
        loses = self._results[-1 * self.parent.state.next_to_move]
        return wins - loses

    @property
    def n(self):
        """
        Returns the number of visits to the current node.
        """
        return self._number_of_visits

    def expand(self):
        """
        Expands the current node by selecting an untried action, creating a new child node, and adding it to the children list.
        """
        action = self.untried_actions.pop()
        next_state = self.state.move(action)
        child_node = TwoPlayersGameMonteCarloTreeSearchNode(
            next_state, parent=self
        )
        self.children.append(child_node)
        return child_node

    def is_terminal_node(self):
        """
        Checks if the current node is a terminal node (end of the game).
        """
        return self.state.is_game_over()

    def rollout(self):
        """
        Simulates a random rollout from the current node until the end of the game and returns the result.
        """
        current_rollout_state = self.state
        while not current_rollout_state.is_game_over():
            possible_moves = current_rollout_state.get_legal_actions()
            action = self.rollout_policy(possible_moves)
            current_rollout_state = current_rollout_state.move(action)
        return current_rollout_state.game_result

    def backpropagate(self, result):
        """
        Backpropagates the result of a rollout to update the node's statistics.
        """
        self._number_of_visits += 1.
        self._results[result] += 1.
        if self.parent:
            self.parent.backpropagate(result)
