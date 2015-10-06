# Initial Cube State (White top, green front)

corners = {'UFR': 'W', 'UFL': 'W', 'UBL': 'W', 'UBR': 'W',
                'LDF': 'O', 'LDB': 'O', 'LUB': 'O', 'LUF': 'O',
                'FRD': 'G', 'FLD': 'G', 'FLU': 'G', 'FRU': 'G',
                'RDB': 'R', 'RDF': 'R', 'RUF': 'R', 'RUB': 'R',
                'BLD': 'B', 'BRD': 'B', 'BRU': 'B', 'BLU': 'B',
                'DBR': 'Y', 'DBL': 'Y', 'DFL': 'Y', 'DFR': 'Y'}

edges = {'UF': 'W', 'UL': 'W', 'UB': 'W', 'UR': 'W',
        'LD': 'O', 'LB': 'O', 'LU': 'O', 'LF': 'O',
        'FD': 'G', 'FL': 'G', 'FU': 'G', 'FR': 'G',
        'RD': 'R', 'RF': 'R', 'RU': 'R', 'RB': 'R',
        'BD': 'B', 'BR': 'B', 'BU': 'B', 'BL': 'B',
        'DB': 'Y', 'DL': 'Y', 'DF': 'Y', 'DR': 'Y'}  


# Take in the scramble and split it up by move

scramble_input = input('Input scramble: ')
scramble = scramble_input.split(' ')

# Turns

def U_turn(x):
    for i in range(x):
        corners['UFR'], corners['UFL'], corners['UBL'], corners['UBR'] = corners['UBR'], corners['UFR'], corners['UFL'], corners['UBL']
        corners['FRU'], corners['LUF'], corners['BLU'], corners['RUB'] = corners['RUB'], corners['FRU'], corners['LUF'], corners['BLU']
        corners['RUF'], corners['FLU'], corners['LUB'], corners['BRU'] = corners['BRU'], corners['RUF'], corners['FLU'], corners['LUB']

        edges['UF'], edges['UL'], edges['UB'], edges['UR'] = edges['UR'], edges['UF'], edges['UL'], edges['UB']
        edges['FU'], edges['LU'], edges['BU'], edges['RU'] = edges['RU'], edges['FU'], edges['LU'], edges['BU']

def D_turn(x):
    for i in range(x):
        corners['DBR'], corners['DBL'], corners['DFL'], corners['DFR'] = corners['DFR'], corners['DBR'], corners['DBL'], corners['DFL']
        corners['BRD'], corners['LDB'], corners['FLD'], corners['FRD'] = corners['FRD'], corners['BRD'], corners['LDB'], corners['FLD']
        corners['RDB'], corners['BLD'], corners['LDF'], corners['RDF'] = corners['RDF'], corners['RDB'], corners['BLD'], corners['LDF']

        edges['DB'], edges['DL'], edges['DF'], edges['DR'] = edges['DR'], edges['DB'], edges['DL'], edges['DF']
        edges['BD'], edges['LD'], edges['FD'], edges['RD'] = edges['RD'], edges['BD'], edges['LD'], edges['FD']

def L_turn(x):
    for i in range(x):
        corners['LDF'], corners['LDB'], corners['LUB'], corners['LUF'] = corners['LUF'], corners['LDF'], corners['LDB'], corners['LUB']
        corners['DFL'], corners['BLD'], corners['UBL'], corners['FLU'] = corners['FLU'], corners['DFL'], corners['BLD'], corners['UBL']
        corners['FLD'], corners['DBL'], corners['BLU'], corners['UFL'] = corners['UFL'], corners['FLD'], corners['DBL'], corners['BLU']

        edges['LD'], edges['LB'], edges['LU'], edges['LF'] = edges['LF'], edges['LD'], edges['LB'], edges['LU']
        edges['DL'], edges['BL'], edges['UL'], edges['FL'] = edges['FL'], edges['DL'], edges['BL'], edges['UL']

def R_turn(x):
    for i in range(x):
        corners['RDB'], corners['RDF'], corners['RUF'], corners['RUB'] = corners['RUB'], corners['RDB'], corners['RDF'], corners['RUF']
        corners['DBR'], corners['FRD'], corners['UFR'], corners['BRU'] = corners['BRU'], corners['DBR'], corners['FRD'], corners['UFR']
        corners['BRD'], corners['DFR'], corners['FRU'], corners['UBR'] = corners['UBR'], corners['BRD'], corners['DFR'], corners['FRU']

        edges['RD'], edges['RF'], edges['RU'], edges['RB'] = edges['RB'], edges['RD'], edges['RF'], edges['RU']
        edges['DR'], edges['FR'], edges['UR'], edges['BR'] = edges['BR'], edges['DR'], edges['FR'], edges['UR']

def F_turn(x):
    for i in range(x):
        corners['FRD'], corners['FLD'], corners['FLU'], corners['FRU'] = corners['FRU'], corners['FRD'], corners['FLD'], corners['FLU']
        corners['RDF'], corners['DFL'], corners['LUF'], corners['UFR'] = corners['UFR'], corners['RDF'], corners['DFL'], corners['LUF']
        corners['DFR'], corners['LDF'], corners['UFL'], corners['RUF'] = corners['RUF'], corners['DFR'], corners['LDF'], corners['UFL']

        edges['FD'], edges['FL'], edges['FU'], edges['FR'] = edges['FR'], edges['FD'], edges['FL'], edges['FU']
        edges['DF'], edges['LF'], edges['UF'], edges['RF'] = edges['RF'], edges['DF'], edges['LF'], edges['UF']

def B_turn(x):
    for i in range(x):
        corners['BLD'], corners['BRD'], corners['BRU'], corners['BLU'] = corners['BLU'], corners['BLD'], corners['BRD'], corners['BRU']
        corners['LDB'], corners['DBR'], corners['RUB'], corners['UBL'] = corners['UBL'], corners['LDB'], corners['DBR'], corners['RUB']
        corners['DBL'], corners['RDB'], corners['UBR'], corners['LUB'] = corners['LUB'], corners['DBL'], corners['RDB'], corners['UBR']

        edges['BD'], edges['BR'], edges['BU'], edges['BL'] = edges['BL'], edges['BD'], edges['BR'], edges['BU']
        edges['DB'], edges['RB'], edges['UB'], edges['LB'] = edges['LB'], edges['DB'], edges['RB'], edges['UB']

# Applying the scramble

for move in scramble:
    if move == 'U':
        U_turn(1)
    elif move == 'U\'':
        U_turn(3)
    elif move == 'U2':
        U_turn(2)
    elif move == 'D':
        D_turn(1)
    elif move == 'D\'':
        D_turn(3)
    elif move == 'D2':
        D_turn(2)
    elif move == 'L':
        L_turn(1)
    elif move == 'L\'':
        L_turn(3)
    elif move == 'L2':
        L_turn(2)
    elif move == 'R':
        R_turn(1)
    elif move == 'R\'':
        R_turn(3)
    elif move == 'R2':
        R_turn(2)
    elif move == 'F':
        F_turn(1)
    elif move == 'F\'':
        F_turn(3)
    elif move == 'F2':
        F_turn(2)
    elif move == 'B':
        B_turn(1)
    elif move == 'B\'':
        B_turn(3)
    elif move == 'B2':
        B_turn(2)

# The Solver

t_perm = 'R U R\' U\' R\' F R2 U\' R\' U\' R U R\' F\''

# solve_UF = 'R U R\' F\' R U R\' U\' R\' F R2 U\' R\' U\''
# solve_UL = t_perm
# solve_UB = '(l2 D\' L2) ' + t_perm + ' (L2 D l2)'
# solve_LD = '(L d L\') ' + t_perm + ' (L d\' L\')'
# solve_LB = '(d L\') ' + t_perm + ' (L d\')'
# solve_LU = '(L\' d L\') ' + t_perm + ' (L d\' L)'
# solve_LF = '(d\' L) ' + t_perm + ' (L\' d)'
# solve_FD = '(F L\' F\') ' + t_perm + ' (F L F\')'
# solve_FL = '(L\') ' + t_perm + ' (L)'
# solve_FU = '(l D\' L2) ' + t_perm + ' (L2 D l\')'
# solve_FR = '(d2 L) ' + t_perm + ' (L\' d2)'
# solve_RD = '(D\' F L\' F\') ' + t_perm + ' (F L F\' D)'
# solve_RF = '(d\' L\') ' + t_perm + ' (L d)'
# solve_RB = '(d L) ' + t_perm + ' (L\' d\')'
# solve_BD = '(l\' D L2) ' + t_perm + ' (L2 D\' l)'
# solve_BR = '(d2 L\') ' + t_perm + ' (L d2)'
# solve_BU = '(l\' D L2) ' + t_perm + ' (L2 D\' l)'
# solve_BL = '(L) ' + t_perm + ' (L\')'
# solve_DB = '(D L2) ' + t_perm + ' (L2 D\')'
# solve_DL = '(L2) ' + t_perm + ' (L2)'
# solve_DF = '(D\' L2) ' + t_perm + ' (L2 D)'
# solve_DR = '(D2 L2) ' + t_perm + ' (L2 D2)'

y_perm = 'F R U\' R\' U\' R U R\' F\' R U R\' U\' R\' F R F\''

def get_edge(location):
    """Returns the colors of the edge at a location"""
    return edges[location] + edges[location[::-1]]

def print_solve(location):

    edges['UR'], edges[location] = edges[location], edges['UR']
    edges['RU'], edges[location[::-1]] = edges[location[::-1]], edges['RU']

    if location == 'UF':
        return 'R U R\' F\' R U R\' U\' R\' F R2 U\' R\' U\''
    elif location == 'UL':
        return t_perm
    elif location == 'UB':
        return '(l2 D\' L2) ' + t_perm + ' (L2 D l2)'
    elif location == 'LD':
        return '(L d L\') ' + t_perm + ' (L d\' L\')'
    elif location == 'LB':
        return '(d L\') ' + t_perm + ' (L d\')'
    elif location == 'LU':
        return '(L\' d L\') ' + t_perm + ' (L d\' L)'
    elif location == 'LF':
        return '(d\' L) ' + t_perm + ' (L\' d)'
    elif location == 'FD':
        return '(F L\' F\') ' + t_perm + ' (F L F\')'
    elif location == 'FL':
        return '(L\') ' + t_perm + ' (L)'
    elif location == 'FU':
        return '(l D\' L2) ' + t_perm + ' (L2 D l\')'
    elif location == 'FR':
        return '(d2 L) ' + t_perm + ' (L\' d2)'
    elif location == 'RD':
        return '(D\' F L\' F\') ' + t_perm + ' (F L F\' D)'
    elif location == 'RF':
        return '(d\' L\') ' + t_perm + ' (L d)'
    elif location == 'RB':
        return '(d L) ' + t_perm + ' (L\' d\')'
    elif location == 'BD':
        return '(l\' D L2) ' + t_perm + ' (L2 D\' l)'
    elif location == 'BR':
        return '(d2 L\') ' + t_perm + ' (L d2)'
    elif location == 'BU':
        return '(l\' D L2) ' + t_perm + ' (L2 D\' l)'
    elif location == 'BL':
        return '(L) ' + t_perm + ' (L\')'
    elif location == 'DB':
        return '(D L2) ' + t_perm + ' (L2 D\')'
    elif location == 'DL':
        return '(L2) ' + t_perm + ' (L2)'
    elif location == 'DF':
        return '(D\' L2) ' + t_perm + ' (L2 D)'
    elif location == 'DR':
        return '(D2 L2) ' + t_perm + ' (L2 D2)'

_zip = zip

def zip(*sequences):
    """Returns a list of lists, where the i-th list contains the i-th
    element from each of the argument sequences.

    >>> zip(range(0, 3), range(3, 6))
    [[0, 3], [1, 4], [2, 5]]
    >>> for a, b in zip([1, 2, 3], [4, 5, 6]):
    ...     print(a, b)
    1 4
    2 5
    3 6
    >>> for triple in zip(['a', 'b', 'c'], [1, 2, 3], ['do', 're', 'mi']):
    ...     print(triple)
    ['a', 1, 'do']
    ['b', 2, 're']
    ['c', 3, 'mi']
    """
    return list(map(list, _zip(*sequences)))

def flipped_edges():
    check_edges = ['UF', 'UL', 'UB', 'FL', 'LB', 'BR', 'RF', 'DB', 'DL', 'DF', 'DR']
    flipped_positions = ['GW', 'OW', 'BW', 'OG', 'BO', 'RB', 'GR', 'BY', 'OY', 'GY', 'RY']
    for edge, flipped_position in zip(check_edges, flipped_positions):
        if get_edge(edge) == flipped_position:
            return edge
    return False

def solve_flipped_edges(location):
    print(print_solve(location))
    print(print_solve(location[::-1]))    

    # elif get_edge('UR') == 'WR' or get_edge('UR') == 'RW':
    #     #cycle_break = find_unsolved_edge()
    #     #print
    #     t_perm_swap(cycle_break)
    #     solves_edges()

def solve_edges():
    if (edges['UF'] == 'W') and (edges['UL'] == 'W') and (edges['UB'] == 'W') and (edges['UR'] == 'W') and (edges['LD'] == 'O') and (edges['LB'] == 'O') and (edges['LU'] == 'O') and (edges['LF'] == 'O') and (edges['FD'] == 'G') and (edges['FL'] == 'G') and (edges['FU'] == 'G') and (edges['FR'] == 'G') and (edges['RD'] == 'R') and (edges['RF'] == 'R') and (edges['RU'] == 'R') and (edges['RB'] == 'R') and (edges['BD'] == 'B') and (edges['BR'] == 'B') and (edges['BU'] == 'B') and (edges['BL'] == 'B') and (edges['DB'] == 'Y') and (edges['DL'] == 'Y') and (edges['DF'] == 'Y') and (edges['DR'] == 'Y'):
        print('Solved')
        return False

    elif get_edge('UR') == 'WG':
        print(print_solve('UF'))
        solve_edges()

    elif get_edge('UR') == 'WO':
        print(print_solve('UL'))
        solve_edges()

    elif get_edge('UR') == 'WB':
        print(print_solve('UB'))
        solve_edges()

    elif get_edge('UR') == 'OY':
        print(print_solve('LD'))
        solve_edges()

    elif get_edge('UR') == 'OB':
        print(print_solve('LB'))
        solve_edges()

    elif get_edge('UR') == 'OW':
        print(print_solve('LU'))
        solve_edges()

    elif get_edge('UR') == 'OG':
        print(print_solve('LF'))
        solve_edges()

    elif get_edge('UR') == 'GY':
        print(print_solve('FD'))
        solve_edges()

    elif get_edge('UR') == 'GO':
        print(print_solve('FL'))
        solve_edges()

    elif get_edge('UR') == 'GW':
        print(print_solve('FU'))
        solve_edges()

    elif get_edge('UR') == 'GR':
        print(print_solve('FR'))
        solve_edges()

    elif get_edge('UR') == 'RY':
        print(print_solve('RD'))
        solve_edges()

    elif get_edge('UR') == 'RG':
        print(print_solve('RF'))
        solve_edges()

    elif get_edge('UR') == 'RB':
        print(print_solve('RB'))
        solve_edges()

    elif get_edge('UR') == 'BY':
        print(print_solve('BD'))
        solve_edges()

    elif get_edge('UR') == 'BR':
        print(print_solve('BR'))
        solve_edges()

    elif get_edge('UR') == 'BW':
        print(print_solve('BU'))
        solve_edges()

    elif get_edge('UR') == 'BO':
        print(print_solve('BL'))
        solve_edges()

    elif get_edge('UR') == 'YB':
        print(print_solve('DB'))
        solve_edges()

    elif get_edge('UR') == 'YO':
        print(print_solve('DL'))
        solve_edges()

    elif get_edge('UR') == 'YG':
        print(print_solve('DF'))
        solve_edges()

    elif get_edge('UR') == 'YR':
        print(print_solve('DR'))
        solve_edges()

    # here we check if the buffer is solved/flipped

    elif flipped_edges():
        solve_flipped_edges(flipped_edges())
# Example scrambles it can do
# R U' R U R U R U' R' U' R2
# R2 U R U R' U' R' U' R' U R'

# L' F L F L F L' F' L' F' R2 U R U R' U' R' U' R' U R'
# U2 L2 D L2 R2 U' R2 D L2 R2 B L F2 D L D' L' B F R' # no cycle breaks
# R2 B D R2 F R' L U B2 R U2 R2 L2 B2 D2 B' U2 D2 R2 U2 D2 # no cycle breaks, but has a flipped edge
