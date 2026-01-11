from fiveaichess.agents.minimax_agent import MinimaxAgent
from fiveaichess.utilities.combined_utility import CombinedUtility
from fiveaichess.engines.uci_engine import UCIEngine

if __name__ == "__main__":
    # create your utility
    utility = CombinedUtility()
    # create your agent
    agent = MinimaxAgent(utility, 15.0, depth=5)
    # create the engine

    engine = UCIEngine(agent)

    # run the engine (will loop until the game is done or exited)
    engine.run()
