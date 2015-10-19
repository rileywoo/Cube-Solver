# Initial Cube State (White top, green front)

# corners = {'URF': 'W', 'UFL': 'W', 'ULB': 'W', 'UBR': 'W',
#                 'LFD': 'O', 'LDB': 'O', 'LBU': 'O', 'LUF': 'O',
#                 'FRD': 'G', 'FDL': 'G', 'FLU': 'G', 'FUR': 'G',
#                 'RBD': 'R', 'RDF': 'R', 'RFU': 'R', 'RUB': 'R',
#                 'BLD': 'B', 'BDR': 'B', 'BRU': 'B', 'BUL': 'B',
#                 'DRB': 'Y', 'DBL': 'Y', 'DLF': 'Y', 'DFR': 'Y'}

corners = {'URF': 'WRG', 'UFL': 'WGO', 'ULB': 'WOB', 'UBR': 'WBR',
                'LFD': 'OGY', 'LDB': 'OYB', 'LBU': 'OBW', 'LUF': 'OWG',
                'FRD': 'GRY', 'FDL': 'GYO', 'FLU': 'GOW', 'FUR': 'GWR',
                'RBD': 'RBY', 'RDF': 'RYG', 'RFU': 'RGW', 'RUB': 'RWB',
                'BLD': 'BOY', 'BDR': 'BYR', 'BRU': 'BRW', 'BUL': 'BWO',
                'DRB': 'YRB', 'DBL': 'YBO', 'DLF': 'YOG', 'DFR': 'YGR'}

solved_corners = dict(corners)

edges = {'UF': 'W', 'UL': 'W', 'UB': 'W', 'UR': 'W',
        'LD': 'O', 'LB': 'O', 'LU': 'O', 'LF': 'O',
        'FD': 'G', 'FL': 'G', 'FU': 'G', 'FR': 'G',
        'RD': 'R', 'RF': 'R', 'RU': 'R', 'RB': 'R',
        'BD': 'B', 'BR': 'B', 'BU': 'B', 'BL': 'B',
        'DB': 'Y', 'DL': 'Y', 'DF': 'Y', 'DR': 'Y'}

solved_edges = dict(edges)


# Take in the scramble and split it up by move

scramble_input = input('Input scramble: ')
scramble = scramble_input.split(' ')

# Turns

def U_turn(x):
    for _ in range(x):
        corners['URF'], corners['UFL'], corners['ULB'], corners['UBR'] = corners['UBR'], corners['URF'], corners['UFL'], corners['ULB']
        corners['FUR'], corners['LUF'], corners['BUL'], corners['RUB'] = corners['RUB'], corners['FUR'], corners['LUF'], corners['BUL']
        corners['RFU'], corners['FLU'], corners['LBU'], corners['BRU'] = corners['BRU'], corners['RFU'], corners['FLU'], corners['LBU']
        edges['UF'], edges['UL'], edges['UB'], edges['UR'] = edges['UR'], edges['UF'], edges['UL'], edges['UB']
        edges['FU'], edges['LU'], edges['BU'], edges['RU'] = edges['RU'], edges['FU'], edges['LU'], edges['BU']

def D_turn(x):
    for _ in range(x):
        corners['DRB'], corners['DBL'], corners['DLF'], corners['DFR'] = corners['DFR'], corners['DRB'], corners['DBL'], corners['DLF']
        corners['BDR'], corners['LDB'], corners['FDL'], corners['RDF'] = corners['RDF'], corners['BDR'], corners['LDB'], corners['FDL']
        corners['RBD'], corners['BLD'], corners['LFD'], corners['FRD'] = corners['FRD'], corners['RBD'], corners['BLD'], corners['LFD']

        edges['DB'], edges['DL'], edges['DF'], edges['DR'] = edges['DR'], edges['DB'], edges['DL'], edges['DF']
        edges['BD'], edges['LD'], edges['FD'], edges['RD'] = edges['RD'], edges['BD'], edges['LD'], edges['FD']

def L_turn(x):
    for _ in range(x):
        corners['LFD'], corners['LDB'], corners['LBU'], corners['LUF'] = corners['LUF'], corners['LFD'], corners['LDB'], corners['LBU']
        corners['DLF'], corners['BLD'], corners['ULB'], corners['FLU'] = corners['FLU'], corners['DLF'], corners['BLD'], corners['ULB']
        corners['FDL'], corners['DBL'], corners['BUL'], corners['UFL'] = corners['UFL'], corners['FDL'], corners['DBL'], corners['BUL']

        edges['LD'], edges['LB'], edges['LU'], edges['LF'] = edges['LF'], edges['LD'], edges['LB'], edges['LU']
        edges['DL'], edges['BL'], edges['UL'], edges['FL'] = edges['FL'], edges['DL'], edges['BL'], edges['UL']

def R_turn(x):
    for _ in range(x):
        corners['RBD'], corners['RDF'], corners['RFU'], corners['RUB'] = corners['RUB'], corners['RBD'], corners['RDF'], corners['RFU']
        corners['DRB'], corners['FRD'], corners['URF'], corners['BRU'] = corners['BRU'], corners['DRB'], corners['FRD'], corners['URF']
        corners['BDR'], corners['DFR'], corners['FUR'], corners['UBR'] = corners['UBR'], corners['BDR'], corners['DFR'], corners['FUR']

        edges['RD'], edges['RF'], edges['RU'], edges['RB'] = edges['RB'], edges['RD'], edges['RF'], edges['RU']
        edges['DR'], edges['FR'], edges['UR'], edges['BR'] = edges['BR'], edges['DR'], edges['FR'], edges['UR']

def F_turn(x):
    for _ in range(x):
        corners['FRD'], corners['FDL'], corners['FLU'], corners['FUR'] = corners['FUR'], corners['FRD'], corners['FDL'], corners['FLU']
        corners['RDF'], corners['DLF'], corners['LUF'], corners['URF'] = corners['URF'], corners['RDF'], corners['DLF'], corners['LUF']
        corners['DFR'], corners['LFD'], corners['UFL'], corners['RFU'] = corners['RFU'], corners['DFR'], corners['LFD'], corners['UFL']

        edges['FD'], edges['FL'], edges['FU'], edges['FR'] = edges['FR'], edges['FD'], edges['FL'], edges['FU']
        edges['DF'], edges['LF'], edges['UF'], edges['RF'] = edges['RF'], edges['DF'], edges['LF'], edges['UF']

def B_turn(x):
    for _ in range(x):
        corners['BLD'], corners['BDR'], corners['BRU'], corners['BUL'] = corners['BUL'], corners['BLD'], corners['BDR'], corners['BRU']
        corners['LDB'], corners['DRB'], corners['RUB'], corners['ULB'] = corners['ULB'], corners['LDB'], corners['DRB'], corners['RUB']
        corners['DBL'], corners['RBD'], corners['UBR'], corners['LBU'] = corners['LBU'], corners['DBL'], corners['RBD'], corners['UBR']

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
y_perm = 'F R U\' R\' U\' R U R\' F\' R U R\' U\' R\' F R F\''

def get_edge(location):
    """Returns the colors of the edge at a location"""
    return edges[location] + edges[location[::-1]]

def get_corner(location):
    """Returns the colors of the corner at a location"""
    return corners[location] + (corners[location[1:] + location[:1]]) + (corners[location[2:] + location[:2]])

def print_edge_solve(location):

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
        return '(l\' D\' L2) ' + t_perm + ' (L2 D l)'
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

def print_corner_solve(location):
    corners['ULB'], corners[location] = corners[location], corners['ULB']
    corners['LBU'], corners[location[1:] + location[:1]] = corners[location[1:] + location[:1]], corners['LBU']
    corners['BUL'], corners[location[2:] + location[:2]] = corners[location[2:] + location[:2]], corners['BUL']
    
    if location == 'URF':
        return y_perm
    elif location == 'UFL':
        return '(F2 D R2) ' + y_perm + ' (R2 D\' F2)'
    elif location == 'UBR':
        return '(R2 D R2) ' + y_perm + ' (R2 D\' R2)'
    elif location == 'LFD':
        return '(D R) ' + y_perm + ' (R\' D\')'
    elif location == 'LDB':
        return '(D2 F\') ' + y_perm + ' (F D2)'
    elif location == 'LUF':
        return '(F) ' + y_perm + ' (F\')'
    elif location == 'FRD':
        return '(R) ' + y_perm + ' (R\')'
    elif location == 'FDL':
        return '(D F\') ' + y_perm + ' (F D\')'
    elif location == 'FLU':
        return '(F2 R) ' + y_perm + ' (R\' F2)'
    elif location == 'FUR':
        return '(F R) ' + y_perm + ' (R\' F\')'
    elif location == 'RBD':
        return '(D\' R) ' + y_perm + ' (R\' D)'
    elif location == 'RDF':
        return '(F\') ' + y_perm + ' (F)'
    elif location == 'RFU':
        return '(R\' F\') ' + y_perm + '(F R)'
    elif location == 'RUB':
        return '(R D\' R) ' + y_perm + ' (R\' D R\')'
    elif location == 'BLD':
        return '(D2 R) ' + y_perm + ' (R\' D2)'
    elif location == 'BDR':
        return '(D\' F\') ' + y_perm + ' (F D)'
    elif location == 'BRU':
        return '(R\') ' + y_perm + ' (R)'
    elif location == 'DRB':
        return '(R2) ' + y_perm + ' (R2)'
    elif location == 'DBL':
        return '(D\' R2) ' + y_perm + ' (R2 D)'
    elif location == 'DLF':
        return '(F2) ' + y_perm + ' (F2)'
    elif location == 'DFR':
        return '(D R2) ' + y_perm + ' (R2 D\')'

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
    print(print_edge_solve(location))
    print(print_edge_solve(location[::-1]))

def twisted_corners():
    check_corners = ['URF', 'UFL', 'UBR', 'DRB', 'DBL', 'DLF', 'DFR']
    twisted_corners1 = ['RGW', 'GOW', 'BRW', 'RBY', 'BOY', 'OGY', 'GRY']
    twisted_corners2 = ['GWR', 'OWG', 'RWB', 'BYR', 'OYB', 'GYO', 'RYG']
    for corner, pos1, pos2 in zip(check_corners, twisted_corners1, twisted_corners2):
        if corners[corner] == pos1:
            return corner, 'CCW'
        elif corners[corner] == pos2:
            return corner, 'CW'
    return False

def solve_twisted_corners(location): # Need to figure out how to break up the tuple better
    if location[1] == 'CCW':
        print(print_corner_solve(location[0]))
        print(print_corner_solve(location[0][1:] + location[0][:1]))
    else:
        print(print_corner_solve(location[0]))
        print(print_corner_solve(location[0][2:] + location[0][:2]))        

def find_cycle_break():
    if get_edge('UF') != 'WG' and get_edge('UF') != 'GW':
        return 'UF'
    elif get_edge('UL') != 'WO' and get_edge('UL') != 'OW': 
        return 'UL'
    elif get_edge('UB') != 'WB' and get_edge('UB') != 'BW':
        return 'UB'
    elif get_edge('FL') != 'GO' and get_edge('FL') != 'OG':
        return 'FL'
    elif get_edge('BL') != 'BO' and get_edge('BL') != 'OB':
        return 'BL'
    elif get_edge('BR') != 'BR' and get_edge('BR') != 'RB':
        return 'BR'
    elif get_edge('FR') != 'GR' and get_edge('FR') != 'RG':
        return 'FR'
    elif get_edge('DB') != 'YB' and get_edge('DB') != 'BY':
        return 'DB'
    elif get_edge('DL') != 'YO' and get_edge('DL') != 'OY':
        return 'DL'
    elif get_edge('DF') != 'YG' and get_edge('DF') != 'GY':
        return 'DF'
    elif get_edge('DR') != 'YR' and get_edge('DR') != 'RY':
        return 'DR'

def find_corner_break():
    if corners['URF'] != 'WRG' and not is_twisted('URF'):
        print(print_corner_solve('URF'))
    elif corners['UFL'] != 'WGO' and not is_twisted('UFL'):
        print(print_corner_solve('UFL'))
    elif corners['UBR'] != 'WBR' and not is_twisted('UBR'):
        print(print_corner_solve('UBR'))
    elif corners['DRB'] != 'YRB' and not is_twisted('DRB'):
        print(print_corner_solve('DRB'))
    elif corners['DBL'] != 'YBO' and not is_twisted('DBL'):
        print(print_corner_solve('DBL'))
    elif corners['DLF'] != 'YOG' and not is_twisted('DLF'):
        print(print_corner_solve('DFL'))
    elif corners['DFR'] != 'YGR' and not is_twisted('DLF'):
        print(print_corner_solve('DFR'))
    else:
        solve_twisted_corners(twisted_corners())
    

def is_twisted(location):
    return corners[location] == solved_corners[location[1:] + location[:1]] or corners[location] == solved_corners[location[2:] + location[:2]]  

def solve_edges():
    if (edges['UF'] == 'W') and (edges['UL'] == 'W') and (edges['UB'] == 'W') and (edges['UR'] == 'W') and (edges['LD'] == 'O') and (edges['LB'] == 'O') and (edges['LU'] == 'O') and (edges['LF'] == 'O') and (edges['FD'] == 'G') and (edges['FL'] == 'G') and (edges['FU'] == 'G') and (edges['FR'] == 'G') and (edges['RD'] == 'R') and (edges['RF'] == 'R') and (edges['RU'] == 'R') and (edges['RB'] == 'R') and (edges['BD'] == 'B') and (edges['BR'] == 'B') and (edges['BU'] == 'B') and (edges['BL'] == 'B') and (edges['DB'] == 'Y') and (edges['DL'] == 'Y') and (edges['DF'] == 'Y') and (edges['DR'] == 'Y'):
        print('Edges Solved')
        return False

    elif get_edge('UR') == 'WG':
        print(print_edge_solve('UF'))
        solve_edges()

    elif get_edge('UR') == 'WO':
        print(print_edge_solve('UL'))
        solve_edges()

    elif get_edge('UR') == 'WB':
        print(print_edge_solve('UB'))
        solve_edges()

    elif get_edge('UR') == 'OY':
        print(print_edge_solve('LD'))
        solve_edges()

    elif get_edge('UR') == 'OB':
        print(print_edge_solve('LB'))
        solve_edges()

    elif get_edge('UR') == 'OW':
        print(print_edge_solve('LU'))
        solve_edges()

    elif get_edge('UR') == 'OG':
        print(print_edge_solve('LF'))
        solve_edges()

    elif get_edge('UR') == 'GY':
        print(print_edge_solve('FD'))
        solve_edges()

    elif get_edge('UR') == 'GO':
        print(print_edge_solve('FL'))
        solve_edges()

    elif get_edge('UR') == 'GW':
        print(print_edge_solve('FU'))
        solve_edges()

    elif get_edge('UR') == 'GR':
        print(print_edge_solve('FR'))
        solve_edges()

    elif get_edge('UR') == 'RY':
        print(print_edge_solve('RD'))
        solve_edges()

    elif get_edge('UR') == 'RG':
        print(print_edge_solve('RF'))
        solve_edges()

    elif get_edge('UR') == 'RB':
        print(print_edge_solve('RB'))
        solve_edges()

    elif get_edge('UR') == 'BY':
        print(print_edge_solve('BD'))
        solve_edges()

    elif get_edge('UR') == 'BR':
        print(print_edge_solve('BR'))
        solve_edges()

    elif get_edge('UR') == 'BW':
        print(print_edge_solve('BU'))
        solve_edges()

    elif get_edge('UR') == 'BO':
        print(print_edge_solve('BL'))
        solve_edges()

    elif get_edge('UR') == 'YB':
        print(print_edge_solve('DB'))
        solve_edges()

    elif get_edge('UR') == 'YO':
        print(print_edge_solve('DL'))
        solve_edges()

    elif get_edge('UR') == 'YG':
        print(print_edge_solve('DF'))
        solve_edges()

    elif get_edge('UR') == 'YR':
        print(print_edge_solve('DR'))
        solve_edges()

    elif get_edge('UR') == 'WR' or get_edge('UR') == 'RW' and not flipped_edges():
        cycle_break = ''
        cycle_break = find_cycle_break()
        print(print_edge_solve(cycle_break))
        solve_edges()

    elif flipped_edges():
        solve_flipped_edges(flipped_edges())
        solve_edges()

def solve_corners():
    if (corners['URF'] == 'WRG') and (corners['UFL'] == 'WGO') and (corners['ULB'] == 'WOB') and (corners['UBR'] == 'WBR') and (corners['DRB'] == 'YRB') and (corners['DBL'] == 'YBO') and (corners['DLF'] == 'YOG') and (corners['DFR'] == 'YGR'):
        print('Corners Solved')
        return False
    else: 
        target = corners['ULB']
        if target == 'WRG':
            print(print_corner_solve('URF'))
        elif target == 'WGO':
            print(print_corner_solve('UFL'))
        elif target == 'WBR':
            print(print_corner_solve('UBR'))
        elif target == 'OGY':
            print(print_corner_solve('LFD'))
        elif target == 'OYB':
            print(print_corner_solve('LDB'))
        elif target == 'OWG':
            print(print_corner_solve('LUF'))
        elif target == 'GRY':
            print(print_corner_solve('FRD'))
        elif target == 'GYO':
            print(print_corner_solve('FDL'))
        elif target == 'GOW':
            print(print_corner_solve('FLU'))
        elif target == 'GWR':
            print(print_corner_solve('FUR'))
        elif target == 'RBY':
            print(print_corner_solve('RBD'))
        elif target == 'RYG':
            print(print_corner_solve('RDF'))
        elif target == 'RGW':
            print(print_corner_solve('RFU'))
        elif target == 'RWB':
            print(print_corner_solve('RUB'))
        elif target == 'BOY':
            print(print_corner_solve('BLD'))
        elif target == 'BYR':
            print(print_corner_solve('BDR'))
        elif target == 'BRW':
            print(print_corner_solve('BRU'))
        elif target == 'YRB':
            print(print_corner_solve('DRB'))
        elif target == 'YBO':
            print(print_corner_solve('DBL'))
        elif target == 'YOG':
            print(print_corner_solve('DLF'))
        elif target == 'YGR':
            print(print_corner_solve('DFR'))
        elif (target == 'WOB' or target == 'OBW' or target == 'BWO'):
            find_corner_break()       
        solve_corners()
   


# L2 D' F2 L2 U R2 U2 L2 U2 B2 R2 B U' F2 R D' F2 U' L U R2
