from urllib.request import urlopen

url_middle = "" # To store the moves for the alg.garron URL

def notation_to_URL(moves):
    """Turns notation into part of the alg.garron URL
    >>> notation_to_URL("R U R' U' R' F R2 U' R' U' R U R' F'")
    'R_U_R-_U-_R-_F_R2_U-_R-_U-_R_U_R-_F-'
    >>> notation_to_URL("(R) F R U' R' U' R U R' F' R U R' U' R' F R F' (R')")
    '(R)_F_R_U-_R-_U-_R_U_R-_F-_R_U_R-_U-_R-_F_R_F-_(R-)'
    >>> notation_to_URL("(R D2) F R U' R' U' R U R' F' R U R' U' R' F R F' (D2 R')")
    '(R_D2)_F_R_U-_R-_U-_R_U_R-_F-_R_U_R-_U-_R-_F_R_F-_(D2_R-)'
    >>> notation_to_URL("(l' D L2) R U R' U' R' F R2 U' R' U' R U R' F' (L2 D' l)")
    '(l-_D_L2)_R_U_R-_U-_R-_F_R2_U-_R-_U-_R_U_R-_F-_(L2_D-_l)'
    """
    url = ""
    moves = moves.split()
    for move in moves:
        if "'" in move:
            if "(" in move and ")" in move:
                move = move[:2] + "-" + ")"
            elif "(" in move:
                move = move[:2] + "-"
            elif ")" in move:
                move = move[0] + "-)"
            else:
                move = move[0] + "-"
        url += move + "_"
    return url[:len(url)-1]

# Initial Cube State (White top, green front)


corners = {'URF': 'WRG', 'UFL': 'WGO', 'ULB': 'WOB', 'UBR': 'WBR',
                'LFD': 'OGY', 'LDB': 'OYB', 'LBU': 'OBW', 'LUF': 'OWG',
                'FRD': 'GRY', 'FDL': 'GYO', 'FLU': 'GOW', 'FUR': 'GWR',
                'RBD': 'RBY', 'RDF': 'RYG', 'RFU': 'RGW', 'RUB': 'RWB',
                'BLD': 'BOY', 'BDR': 'BYR', 'BRU': 'BRW', 'BUL': 'BWO',
                'DRB': 'YRB', 'DBL': 'YBO', 'DLF': 'YOG', 'DFR': 'YGR'}

solved_corners = dict(corners)

edges = {'UF': 'WG', 'UL': 'WO', 'UB': 'WB', 'UR': 'WR',
        'LD': 'OY', 'LB': 'OB', 'LU': 'OW', 'LF': 'OG',
        'FD': 'GY', 'FL': 'GO', 'FU': 'GW', 'FR': 'GR',
        'RD': 'RY', 'RF': 'RG', 'RU': 'RW', 'RB': 'RB',
        'BD': 'BY', 'BR': 'BR', 'BU': 'BW', 'BL': 'BO',
        'DB': 'YB', 'DL': 'YO', 'DF': 'YG', 'DR': 'YR'}

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

edge_swap_count = 0
t_perm = 'R U R\' U\' R\' F R2 U\' R\' U\' R U R\' F\''
y_perm = 'F R U\' R\' U\' R U R\' F\' R U R\' U\' R\' F R F\''

def print_edge_solve(location):
    global url_middle
    edges['UR'], edges[location] = edges[location], edges['UR']
    edges['RU'], edges[location[::-1]] = edges[location[::-1]], edges['RU']

    if location == 'UF':
        solution = 'R U R\' F\' R U R\' U\' R\' F R2 U\' R\' U\''
    elif location == 'UL':
        solution = t_perm
    elif location == 'UB':
        solution = '(l2 D\' L2) ' + t_perm + ' (L2 D l2)'
    elif location == 'LD':
        solution = '(L d L\') ' + t_perm + ' (L d\' L\')'
    elif location == 'LB':
        solution = '(d L\') ' + t_perm + ' (L d\')'
    elif location == 'LU':
        solution = '(L\' d L\') ' + t_perm + ' (L d\' L)'
    elif location == 'LF':
        solution = '(d\' L) ' + t_perm + ' (L\' d)'
    elif location == 'FD':
        solution = '(F L\' F\') ' + t_perm + ' (F L F\')'
    elif location == 'FL':
        solution = '(L\') ' + t_perm + ' (L)'
    elif location == 'FU':
        solution = '(l D\' L2) ' + t_perm + ' (L2 D l\')'
    elif location == 'FR':
        solution = '(d2 L) ' + t_perm + ' (L\' d2)'
    elif location == 'RD':
        solution = '(D\' F L\' F\') ' + t_perm + ' (F L F\' D)'
    elif location == 'RF':
        solution = '(d\' L\') ' + t_perm + ' (L d)'
    elif location == 'RB':
        solution = '(d L) ' + t_perm + ' (L\' d\')'
    elif location == 'BD':
        solution = '(l\' D\' L2) ' + t_perm + ' (L2 D l)'
    elif location == 'BR':
        solution = '(d2 L\') ' + t_perm + ' (L d2)'
    elif location == 'BU':
        solution = '(l\' D L2) ' + t_perm + ' (L2 D\' l)'
    elif location == 'BL':
        solution = '(L) ' + t_perm + ' (L\')'
    elif location == 'DB':
        solution = '(D L2) ' + t_perm + ' (L2 D\')'
    elif location == 'DL':
        solution = '(L2) ' + t_perm + ' (L2)'
    elif location == 'DF':
        solution = '(D\' L2) ' + t_perm + ' (L2 D)'
    elif location == 'DR':
        solution = '(D2 L2) ' + t_perm + ' (L2 D2)'
    url_middle += notation_to_URL(solution) + "%0A"
    return solution

def print_corner_solve(location):
    global url_middle
    corners['ULB'], corners[location] = corners[location], corners['ULB']
    corners['LBU'], corners[location[1:] + location[:1]] = corners[location[1:] + location[:1]], corners['LBU']
    corners['BUL'], corners[location[2:] + location[:2]] = corners[location[2:] + location[:2]], corners['BUL']
    
    if location == 'URF':
        solution = y_perm
    elif location == 'UFL':
        solution = '(F2 D R2) ' + y_perm + ' (R2 D\' F2)'
    elif location == 'UBR':
        solution = '(R2 D R2) ' + y_perm + ' (R2 D\' R2)'
    elif location == 'LFD':
        solution = '(D R) ' + y_perm + ' (R\' D\')'
    elif location == 'LDB':
        solution = '(D2 F\') ' + y_perm + ' (F D2)'
    elif location == 'LUF':
        solution = '(F) ' + y_perm + ' (F\')'
    elif location == 'FRD':
        solution = '(R) ' + y_perm + ' (R\')'
    elif location == 'FDL':
        solution = '(D F\') ' + y_perm + ' (F D\')'
    elif location == 'FLU':
        solution = '(F2 R) ' + y_perm + ' (R\' F2)'
    elif location == 'FUR':
        solution = '(F R) ' + y_perm + ' (R\' F\')'
    elif location == 'RBD':
        solution = '(D\' R) ' + y_perm + ' (R\' D)'
    elif location == 'RDF':
        solution = '(F\') ' + y_perm + ' (F)'
    elif location == 'RFU':
        solution = '(R\' F\') ' + y_perm + ' (F R)'
    elif location == 'RUB':
        solution = '(R D\' R) ' + y_perm + ' (R\' D R\')'
    elif location == 'BLD':
        solution = '(D2 R) ' + y_perm + ' (R\' D2)'
    elif location == 'BDR':
        solution = '(D\' F\') ' + y_perm + ' (F D)'
    elif location == 'BRU':
        solution = '(R\') ' + y_perm + ' (R)'
    elif location == 'DRB':
        solution = '(R2) ' + y_perm + ' (R2)'
    elif location == 'DBL':
        solution = '(D\' R2) ' + y_perm + ' (R2 D)'
    elif location == 'DLF':
        solution = '(F2) ' + y_perm + ' (F2)'
    elif location == 'DFR':
        solution = '(D R2) ' + y_perm + ' (R2 D\')'
    url_middle += notation_to_URL(solution) + "%0A"
    return solution

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
        if edges[edge] == flipped_position:
            return edge
    return False

def solve_flipped_edges(location):
    global edge_swap_count
    print(print_edge_solve(location))
    print(print_edge_solve(location[::-1]))
    edge_swap_count += 1

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
    if edges['UF'] != 'WG' and not is_flipped('UF'):
        print(print_edge_solve('UF'))
    elif edges['UL'] != 'WO' and not is_flipped('UL'):
        print(print_edge_solve('UL'))
    elif edges['UB'] != 'WB' and not is_flipped('UB'):
        print(print_edge_solve('UB'))        
    elif edges['FL'] != 'GO' and not is_flipped('FL'):
        print(print_edge_solve('FL'))       
    elif edges['BL'] != 'BO' and not is_flipped('BL'):
        print(print_edge_solve('BL'))        
    elif edges['BR'] != 'BR' and not is_flipped('BR'):
        print(print_edge_solve('BR'))        
    elif edges['FR'] != 'GR' and not is_flipped('FR'):
        print(print_edge_solve('FR'))        
    elif edges['DB'] != 'YB' and not is_flipped('DB'):
        print(print_edge_solve('DB'))        
    elif edges['DL'] != 'YO' and not is_flipped('DL'):
        print(print_edge_solve('DL'))        
    elif edges['DF'] != 'YG' and not is_flipped('DF'):
        print(print_edge_solve('DF'))        
    elif edges['DR'] != 'YR' and not is_flipped('DR'):
        print(print_edge_solve('DR'))
    else:
        solve_flipped_edges(flipped_edges())

def is_flipped(location):
    return edges[location] == solved_edges[location[::-1]]

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
    global edge_swap_count

    if (edges['UF'] == 'WG') and (edges['UL'] == 'WO') and (edges['UB'] == 'WB') and (edges['UR'] == 'WR') and (edges['FL'] == 'GO') and (edges['LB'] == 'OB') and (edges['RB'] == 'RB') and (edges['RF'] == 'RG') and (edges['DB'] == 'YB') and (edges['DL'] == 'YO') and (edges['DF'] == 'YG') and (edges['DR'] == 'YR') and edge_swap_count % 2 == 0:
        print('// Edges Solved')
        return False
    elif (edges['UF'] == 'WG') and (edges['UL'] == 'WO') and (edges['UB'] == 'WB') and (edges['UR'] == 'WR') and (edges['FL'] == 'GO') and (edges['LB'] == 'OB') and (edges['RB'] == 'RB') and (edges['RF'] == 'RG') and (edges['DB'] == 'YB') and (edges['DL'] == 'YO') and (edges['DF'] == 'YG') and (edges['DR'] == 'YR') and edge_swap_count % 2 == 1:
        print(print_edge_solve('UL'))
        return False
    else:
        target = edges['UR']
        if target == 'WG':
            print(print_edge_solve('UF'))

        elif target == 'WO':
            print(print_edge_solve('UL'))

        elif target == 'WB':
            print(print_edge_solve('UB'))

        elif target == 'OY':
            print(print_edge_solve('LD'))

        elif target == 'OB':
            print(print_edge_solve('LB'))

        elif target == 'OW':
            print(print_edge_solve('LU'))

        elif target == 'OG':
            print(print_edge_solve('LF'))

        elif target == 'GY':
            print(print_edge_solve('FD'))

        elif target == 'GO':
            print(print_edge_solve('FL'))

        elif target == 'GW':
            print(print_edge_solve('FU'))

        elif target == 'GR':
            print(print_edge_solve('FR'))

        elif target == 'RY':
            print(print_edge_solve('RD'))

        elif target == 'RG':
            print(print_edge_solve('RF'))

        elif target == 'RB':
            print(print_edge_solve('RB'))

        elif target == 'BY':
            print(print_edge_solve('BD'))

        elif target == 'BR':
            print(print_edge_solve('BR'))

        elif target == 'BW':
            print(print_edge_solve('BU'))

        elif target == 'BO':
            print(print_edge_solve('BL'))

        elif target == 'YB':
            print(print_edge_solve('DB'))

        elif target == 'YO':
            print(print_edge_solve('DL'))

        elif target == 'YG':
            print(print_edge_solve('DF'))

        elif target == 'YR':
            print(print_edge_solve('DR'))

        elif target == 'WR' or target == 'RW':
            find_cycle_break()

        edge_swap_count += 1
        solve_edges()

def solve_corners():
    global url_middle
    if (corners['URF'] == 'WRG') and (corners['UFL'] == 'WGO') and (corners['ULB'] == 'WOB') and (corners['UBR'] == 'WBR') and (corners['DRB'] == 'YRB') and (corners['DBL'] == 'YBO') and (corners['DLF'] == 'YOG') and (corners['DFR'] == 'YGR') and edge_swap_count % 2 == 0:
        print('// Corners Solved')
        return False
    elif (corners['URF'] == 'WRG') and (corners['UFL'] == 'WGO') and (corners['ULB'] == 'WOB') and (corners['UBR'] == 'WBR') and (corners['DRB'] == 'YRB') and (corners['DBL'] == 'YBO') and (corners['DLF'] == 'YOG') and (corners['DFR'] == 'YGR') and edge_swap_count % 2 == 1:
        solution = "U2 R2 U R U R\' U\' R\' U\' R\' U R\' U2"
        print(solution + "// Parity fix")
        url_middle += notation_to_URL(solution) + "%0A"
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
   
solve_edges()
solve_corners()

# For generating the URL 

def tiny_url(url):
    """Given a link, generates a tinyurl"""
    apiurl = "http://tinyurl.com/api-create.php?url="
    # need to convert from bytes to string! =)
    tinyurl = urlopen(apiurl + url).read().decode("utf-8")
    return tinyurl

url_start = "https://alg.cubing.net/?alg="
url_end = "&setup=" + notation_to_URL(scramble_input) + "&title=alg.garron.us"
garron_url = url_start + url_middle + url_end
url = tiny_url(garron_url)
goal = "https://alg.cubing.net/?alg=(D2_L2)_R_U_R-_U-_R-_F_R2_U-_R-_U-_R_U_R-_F-_(L2_D2)%0A(l-_D_L2)_R_U_R-_U-_R-_F_R2_U-_R-_U-_R_U_R-_F-_(L2_D-_l)%0AR_U_R-_F-_R_U_R-_U-_R-_F_R2_U-_R-_U-%0A(l-_D-_L2)_R_U_R-_U-_R-_F_R2_U-_R-_U-_R_U_R-_F-_(L2_D_l)%0A(D-_L2)_R_U_R-_U-_R-_F_R2_U-_R-_U-_R_U_R-_F-_(L2_D)%0A(L-_d_L-)_R_U_R-_U-_R-_F_R2_U-_R-_U-_R_U_R-_F-_(L_d-_L)%0A(d-_L-)_R_U_R-_U-_R-_F_R2_U-_R-_U-_R_U_R-_F-_(L_d)%0A(L)_R_U_R-_U-_R-_F_R2_U-_R-_U-_R_U_R-_F-_(L-)%0AR_U_R-_F-_R_U_R-_U-_R-_F_R2_U-_R-_U-%0A(d2_L-)_R_U_R-_U-_R-_F_R2_U-_R-_U-_R_U_R-_F-_(L_d2)%0A(L_d_L-)_R_U_R-_U-_R-_F_R2_U-_R-_U-_R_U_R-_F-_(L_d-_L-)%0A(d2_L-)_R_U_R-_U-_R-_F_R2_U-_R-_U-_R_U_R-_F-_(L_d2)%0A(L-)_R_U_R-_U-_R-_F_R2_U-_R-_U-_R_U_R-_F-_(L)%0A(d-_L)_R_U_R-_U-_R-_F_R2_U-_R-_U-_R_U_R-_F-_(L-_d)%0A%0A(D_R2)_F_R_U-_R-_U-_R_U_R-_F-_R_U_R-_U-_R-_F_R_F-_(R2_D-)%0A(D-_R2)_F_R_U-_R-_U-_R_U_R-_F-_R_U_R-_U-_R-_F_R_F-_(R2_D)%0A(R_D-_R)_F_R_U-_R-_U-_R_U_R-_F-_R_U_R-_U-_R-_F_R_F-_(R-_D_R-)%0AF_R_U-_R-_U-_R_U_R-_F-_R_U_R-_U-_R-_F_R_F-%0A(D_F-)_F_R_U-_R-_U-_R_U_R-_F-_R_U_R-_U-_R-_F_R_F-_(F_D-)%0A(F2_R)_F_R_U-_R-_U-_R_U_R-_F-_R_U_R-_U-_R-_F_R_F-_(R-_F2)%0A(D-_F-)_F_R_U-_R-_U-_R_U_R-_F-_R_U_R-_U-_R-_F_R_F-_(F_D)%0A(R-_F-)_F_R_U-_R-_U-_R_U_R-_F-_R_U_R-_U-_R-_F_R_F-(F_R)%0A&setup=D2_B-_L-_D2_F2_U_D-_R-_B-_U2_L-_U2_B2_L-_D2_L-_U2_F2_R_F2&title=alg.garron.us"
print(url)

