input_data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

input_data="""..f........................8......................
G............8..u.................................
........G...p.....................................
......d.....................n.....................
..................................................
.....................................K............
..................F...8.n...B.K...................
....b.........8..u................................
...............F.p.......B.............4.....5....
....f..d..U.........................c.............
...........U.....d.n.u.0................5.........
...Y.......f..........................5...........
..........................u.....d.....e.........4.
..F...p.............v........n....................
....s.............0...............................
...US.s....g.....D..........................4.....
......wG...............S..........................
.............................B.....e..............
.........w.........................A..............
.............9w.g..........................4......
U....9..g.....v.....P....D.....f.K................
.s.............0..9........pP..........5..........
..9s...................P..........................
.............b..................0.....A..2....e...
....................b.....V..v....................
.......7........B......................A..........
..................D6...V....q.....................
...v............D....PV...........................
.........Y...........g.......................e..y.
.......SW......V..7....................c..........
.......bY7.....................N........A.........
.....................q.N..........y...............
........................N.........c...............
..................................................
.........C..7..................q........2.........
............................N...q.................
...W......C3...Q................a1.........y......
.......W.......................3......2...........
........3...........6.............1...............
....3............C.1....................k.........
E..................................a.....c........
.............................................w....
..S.......................Q..........2......k.....
......................C....6.......Q......ak......
..................................................
.................E.............a1............y....
W..........E......................................
......E...........6...........Q...................
...........................k......................
..................................................
"""

array_of_antennas = input_data.split('\n')
array_of_antinodes = array_of_antennas.copy()
array_of_antennas.remove('')
print (array_of_antennas)
max_row=len(array_of_antennas)
max_col=len(array_of_antennas[0])
antenna_locations = {}

def find_other_antennas(row, col, antenna):
    print(f'{row},{col},{antenna}')

    r = 0
    for line in array_of_antennas:
        for c in range(len(line)):
            if (line[c] == antenna):
                if (antenna in antenna_locations):
                    locations = antenna_locations[antenna]
                    print (f'antenna {antenna} found in dict {locations}')

                    print (locations)
                    coordinate = (row, col)
                    print (f'checking coordinate {coordinate}')

                    if (coordinate not in locations):
                        print (f'location {coordinate} added')
                        locations.append(coordinate)
                        antenna_locations[antenna]=locations

                    else:
                        print (f'location {coordinate} found ')
                    
                    #print(f'locations : {antenna_locations}')

                else:
                    print (f'antenna not found in dict')
                    coordinate = (row, col)
                    locations = []
                    locations.append(coordinate)
                    antenna_locations[antenna]=locations
                    print(f'antenna added : {antenna_locations}')

    
        r += 1


    print(antenna_locations)
    print('SCAN COMPLETE')

def getNewLoc2(a, b):

    x = a[0] - b[0]
    y = a[1] - b[1]

    return (x,y)
        
def getNewLoc(a, b):
        
    x = a[0] +  b[0]
    y = a[1] +  b[1]

    return (x,y)

def check(coord):
    if (coord[0] < 0 or coord[0] >= max_row):
        return False
    if (coord[1] < 0 or coord[1] >= max_col):
        return False
    
    return True
        
def getDiff(coord1, coord2):
    x = coord1[0]-coord2[0]
    y = coord1[1]-coord2[1]
    return (x,y)

def check_antenna_locations(loc):
    for antenna in antenna_locations:
        coords = antenna_locations[antenna]
        for coord in coords:
            if (coord == loc):
                return True
    
    return False

def start():
    row = 0
    for line in array_of_antennas:
        for col in range(len(line)):
            if line[col] != '.' :
                find_other_antennas(row, col, line[col])


        row += 1

    print ('RESULT-------')
    anti_nodes = {}
    anti_nodes ['#']=[]
    

    for antenna in antenna_locations:
        coords = antenna_locations [antenna]
        print(f'Antenna {antenna}')
        for index in range(0,len(coords)-1):
            for index2 in range(index+1, len(coords)):
                coord1 = coords[index]
                coord2 = coords[index2]
                
                diff = getDiff(coord1, coord2)
                print (f'{coord1}, {coord2}, {diff}')

                while True:
                    new_loc = getNewLoc(coord1, diff)
                    if (check(new_loc)):
                        print (new_loc)

                        if (new_loc not in anti_nodes['#']):
                            if check_antenna_locations(new_loc) is False:
                                anti_nodes['#'].append(new_loc)

                        coord1 = new_loc
                    else:
                        print(f'out of bounds')
                        break

                while True:
                    new_loc = getNewLoc2(coord2, diff)

                    if (check(new_loc)):
                        print (new_loc)

                        if (new_loc not in anti_nodes['#']):
                            if check_antenna_locations(new_loc) is False:
                                anti_nodes['#'].append(new_loc)

                        coord2 = new_loc

                    else:
                        print(f'out of bounds')
                        break

                print ('==============')
    
    print (anti_nodes)
    anti_nodes_count = len(anti_nodes['#'])
    for antenna in antenna_locations:
        anti_nodes_count += len(antenna_locations[antenna])
    
    print (anti_nodes_count)

start()