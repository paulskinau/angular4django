class robot(object):

    def __init__(self):
        self.terrain = None
        self.sunk_cost = -1

    def parse_terrain(self, terrain):
        self.terrain = None
        self.sunk_cost = -1
        str_lines = terrain.split("\n")
        rslt = []

        for line in str_lines:
            try:
                rslt_line = [ int(x,16) for x in line.strip().replace('  ',' ').split(' ')]
                if len(rslt) > 0:
                    if len(rslt_line) != len(rslt[0]):
                        raise ValueError('Not all lines contain {} values'.format(len(rslt[0])))

                rslt.append(rslt_line)
            except ValueError as e:
                raise ValueError('Cannot parse input... not all values are numbers. {}'.format(e))
        
        self.terrain = rslt

    def walk(self, x,y,sunk_cost=0, result=''):
        sunk_cost += self.terrain[y][x]
        hasmove = False
        if y < len(self.terrain) - 1:
            self.walk(x,y+1, sunk_cost, result + 'd,')
            hasmove = True
        if x < len(self.terrain[0]) - 1:
            self.walk(x+1,y, sunk_cost, result + 'r,')
            hasmove = True
        if not hasmove:
            if self.sunk_cost == -1 or self.sunk_cost > sunk_cost:
                self.result = result.strip(',')
                self.sunk_cost = sunk_cost
