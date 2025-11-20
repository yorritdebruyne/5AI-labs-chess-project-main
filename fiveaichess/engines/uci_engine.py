import chess

from fiveaichess.agents.agent import Agent


class UCIEngine():

    option_definitions: dict[str, dict[str, any]] = {}
    
    def __init__(self, agent: Agent) -> None:
        self.agent = agent
        self.options = {}
        
    def run(self):
        board = chess.Board()

        # continuously receive commands and process them
        while True:
            input_val = input().split(' ')

            match input_val:

                case ['uci']:
                    print(f'id name {self.agent.name}')
                    print(f'id author {self.agent.author}')
                    self.declare_options()
                    print('uciok')

                case ['setoption', 'name', name]:
                    if name in self.option_definitions:
                        definition = self.option_definitions[name]
                        match definition['type']:
                            case 'button':
                                self.options[name] = True
                            case _:
                                self.options[name] = definition['default']

                case ['setoption', 'name', name, 'value', value]:
                    if name in self.option_definitions:
                        definition = self.option_definitions[name]
                        match definition['type']:
                            case 'spin':
                                value = int(value)
                            case 'check':
                                value = bool(value == 'true')
                            case 'string':
                                pass
                            case 'combo':
                                pass
                    self.options[name] = value

                case ['isready']:
                    print('readyok')

                case ['ucinewgame']:
                    board = chess.Board()

                case ['position', 'startpos']:
                    board = chess.Board()
                
                case ['position', 'startpos', 'moves', *moves]:
                    board = chess.Board()
                    for move in moves:
                        board.push_uci(move)

                case ['go', *args]:
                    it = iter(args)
                    known_keys = {'wtime', 'btime', 'winc', 'binc', 'movestogo', 'depth', 'nodes', 'mate', 'movetime'}
                    constraints = {key: int(next(it)) for key in it if key in known_keys}
                    print(f'bestmove {self.agent.calculate_move(board, constraints)}')

                case ['quit']:
                    break

    def declare_options(self):
        for o_name, definition in self.option_definitions.items():
            o_type = definition['type']
            declaration = f"option name {o_name} type {o_type}"
            if 'default' in definition:
                o_default = definition['default']
                declaration += f" default {o_default}"
            match o_type:
                case 'spin':
                    o_min = definition['min']
                    o_max = definition['max']
                    declaration += f" min {o_min} max {o_max}"
                case 'check':
                    pass
                case 'string':
                    pass
                case 'combo':
                    o_vars = definition['vars']
                    for o_var in o_vars.spit(' '):
                        declaration += f" var {o_var}"
                case 'button':
                    pass
            print(declaration)