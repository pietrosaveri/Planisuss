import matplotlib
import random 
import numpy

GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (15, 75, 0)
BLUE =(0, 0, 255)
WATER = 200
GROUND = 300
MATERIALS = (GROUND, WATER)

NUMCELL = 7

class Vegetob():
    def __init__(self):
        self.DENSITY_RANGE = random.randint(0, 100)
        self.DENSITY = self.DENSITY_RANGE
        self.COLOR = BROWN

class Erbast():
    def __init__(self):
        self.ENERGY_RANGE = random.randint(0, 75)
        self.LIFETIME_RANGE = random.randint(1, 100)  #days
        self.SOCIALATTITUDE_RANGE = random.randint(0, 1)
        
        self.COLOR = GREEN
        self.VALUE = 400
        self.MOVED = False
        self.ENERGY = self.ENERGY_RANGE
        self.LIFETIME = self.LIFETIME_RANGE 
        self.AGE = 0 #start from 0 increases every day  
        self.SOCIALATTITUDE = self.SOCIALATTITUDE_RANGE

        if self.AGE == self.LIFETIME:
            pass 
            #dies

        if self.ENERGY == 0:
            pass
            #dies

class Carviz():
    def __init__(self):
        self.ENERGY_RANGE = random.randint(0, 75)
        self.LIFETIME_RANGE = random.randint(1, 100)  #days
        self.SOCIALATTITUDE_RANGE = random.randint(0, 1)
        
        self.COLOR = RED
        self.VALUE = 500
        self.ENERGY = self.ENERGY_RANGE
        self.LIFETIME = self.LIFETIME_RANGE 
        self.AGE = 0 #start from 0 increases every day  
        self.SOCIALATTITUDE = self.SOCIALATTITUDE_RANGE


        if self.AGE == self.LIFETIME:
            pass 
            #dies

        if self.ENERGY == 0:
            pass
            #dies

class Cell():
    def __init__(self):
        self.carviz = Carviz
        self.erbast = Erbast
        self.vegetob = Vegetob
        self.list_GROUND = []
        self.list_WATER = []
        self.list_MATERIALS = []

    def add_ground(self):
        self.list_GROUND.append("ground")
        #print(self.list_GROUND)

    def add_water(self):
        self.list_WATER.append("water")
        #print(self.list_WATER)
    
    def ground_water(self, WATER_OR_GROUND):
        self.list_MATERIALS.append(WATER_OR_GROUND)
        #print(self.list_MATERIALS)


def grid_init(N):
    #Returns an empty NxN grid
    #only this would draw a grid in line
    grid = list()
    for _ in range(0, N):
        r = list()
        for _ in range(0, N):
            r.append(0)
        grid.append(r)
    return grid


def grid_display(grid, N):
    #draw the grid in a square way, not in line
    for row in range(0, N):
        for col in range(0, N):
            print(' ', grid[row][col], end = ' ')
        print()
    print()


def grid_evolve(grid, N):
    #Return the next generation grid
    # evolution of a generation
    next = grid_init(N)
    for row in range(0, N):
        for col in range(0, N):
            # compute the # neighbors of [row][col] cell
            neigh = 0
            for i in range(max(0, row-1), min(N, row+2)):
                # exploring the neighborhood in row direction
                for j in range(max(0, col-1), min(N, col+2)):
                    # exploring the neighborhood in col direction
                    neigh += grid[i][j]                
            neigh -= grid[row][col]
            
            # compute the status of the [row][col] cell in the next generation
            if grid[row][col] == 1:
                # live cell
                if 2 <= neigh <=3:
                    next[row][col] = 1
                # otherwise it is already empty
            else:
                # dead cell
                if neigh == 3:
                    next[row][col] = 1
    return next

def Search(grid):
    for a in range(1, NUMCELL-1):
        for j in range(1, NUMCELL-1):
            if grid[a][j] == Erbast().VALUE:
                if Erbast().SOCIALATTITUDE == 1:
                    #print("i found one! It is in", a, j)
                    pass

            j +=1
        a +=1

def Movement(grid):
    #NEIGH_LIST = []
    #Erbast().MOVED = False
    listerb = []
    max_list = []
    listcar = []
    list_pride = []
    obj = {}

    #moved = False
    for a in range(1, NUMCELL-1, 1):
        for j in range(1, NUMCELL-1, 1):

            #next = grid_display(grid, NUMCELL)
            next = grid
            #print(grid[a][j])
#a = row     
            #print("alto sinistra", grid[a-1][j-1])
            #print("basso destra", grid[a+1][j+1])
            #print("alto centro", grid[a-1][j])
            #print("basso centro", grid[a+1][j]) 
            ##print("centro sinistra", grid[a][j-1])
            #print("centro destra", grid[a][j+1])
            #print("alto detra", grid[a-1][j+1])
            #print("basso sinistra", grid[a+1][j-1])

            
            
            if grid[a][j] == Erbast().VALUE and Erbast().ENERGY >= 20:
                print('Erbast energetico!')

                if 0< grid[a-1][j-1] <= 100:
                    listerb.append(next[a-1][j-1])
                    grid[a][j] = GROUND
                    #print("alto sinistra")
                    
                if 0< grid[a+1][j+1] <= 100: 
                    listerb.append(next[a+1][j+1])
                    grid[a][j] = GROUND
                    #print('basso destra')

                if 0< grid[a-1][j] <= 100:
                    listerb.append(next[a-1][j])
                    grid[a][j] = GROUND
                    #print("alto centro")

                if 0< grid[a+1][j] <= 100:
                    listerb.append(next[a+1][j])
                    grid[a][j] = GROUND
                    #print('basso centro')
                  
                if 0< grid[a][j-1] <= 100: 
                    listerb.append(next[a][j-1])
                    grid[a][j] = GROUND
                    #print('centro sinistra')
                  
                if 0< grid[a][j+1] <= 100: 
                    listerb.append(grid[a][j+1])
                    grid[a][j] = GROUND
                    #print("centro destra")
                    
                if 0< grid[a-1][j+1] <= 100: 
                    listerb.append(next[a-1][j+1])
                    grid[a][j] = GROUND
                    #print('alto destra')
                
                if 0< grid[a+1][j-1] <= 100: 
                    listerb.append(next[a+1][j-1])
                    grid[a][j] = GROUND
                    #print("basso sinistra")
                  
                if Erbast().SOCIALATTITUDE == 1:
                    #the erbrast has a high social attidude
                    #go to form an herd with another erbast
                    #SEARCH IN ALL GRID SOMNEOONE ELSE WITH 1 AND GO TO HIM
                    Search(grid) #if he find one he has to go to him but do not touch water!
                
                set = (a, j)
                obj["l"+str(set)] = [listerb]

                try:      
                    max_number = max(listerb)
                    max_list.append(max_number)
                    listerb.clear()
                except:
                    print('no move!')
            j +=1
        a +=1
    #grid_display(grid, NUMCELL)
  #in list1 ci sono tutti quelli da cambiare, se li cambiamo dopo aver fatto il loop, non vengono visti piu volte, nella list salviamo quelli da cambiare in 400
    print(max_list)
    print(obj)
    
    #si crea un for loop in range list1 che cerca index ti elemento list1 nella grid e quando trovato lo mette uguale ad 400
    #for i in dizionario prendi una lista alla volta 
    for element in max_list:
        print('for 1')
        for i, lst in enumerate(grid):
            print('for riga')
            for k, item in enumerate(lst):
                print("for colonna")
                if item == element:
                    print(max_list)
                    print(item)
                    print(i, k) #i = row dove si trova numero, k = col dove si trova number
                    grid[i][k] = Erbast().VALUE
    

                    """ coordinates = (i, k)
                    print("coo:", coordinates)
                    #grid[i][k] = Erbast().VALUE
                    if Erbast().VALUE and coordinates in list_pride:
                        print("if", list_pride)
                        grid[i][k] = 800
                        print("pride")

                    else: 
                        grid[i][k] = Erbast().VALUE
                        list_pride.append(coordinates)
                        list_pride.append(400)
                        print("else:", list_pride)
 """
                    
                  
######################################################################################################################################################################################
                  
    for a in range(1, NUMCELL-1, 1):
        for j in range(1, NUMCELL-1,  1):
            #print(Carviz().SOCIALATTITUDE)
            if grid[a][j] == Carviz().VALUE and Carviz().SOCIALATTITUDE == 1 and Carviz().ENERGY >= 20:
                print('Carviz affamato energetico!')
            

                if grid[a-1][j-1] == Erbast().VALUE:
                    listcar.append(next[a-1][j-1])
                    grid[a][j] = GROUND

                elif grid[a+1][j+1] == Erbast().VALUE: 
                        listcar.append(next[a+1][j+1])
                        grid[a][j] = GROUND
        
                elif grid[a-1][j] == Erbast().VALUE:
                        listcar.append(next[a-1][j])
                        grid[a][j] = GROUND

                elif grid[a+1][j] == Erbast().VALUE:
                        listcar.append(next[a+1][j])
                        grid[a][j] = GROUND

                elif grid[a][j-1] == Erbast().VALUE: 
                        listcar.append(next[a][j-1])
                        grid[a][j] = GROUND

                elif  grid[a][j+1] == Erbast().VALUE: 
                        listcar.append(grid[a][j+1])
                        grid[a][j] = GROUND

                elif grid[a-1][j+1] ==Erbast().VALUE: 
                        listcar.append(next[a-1][j+1])
                        grid[a][j] = GROUND

                elif grid[a+1][j-1] ==Erbast().VALUE: 
                        listcar.append(next[a+1][j-1])
                        grid[a][j] = GROUND
            
            #check all gtrid for 400 and walk on ground to reach him

            
 
            j +=1
        a +=1


    #si crea un for loop in range list1 che cerca index ti elemento list1 nella grid e quando trovato lo mette uguale ad 400
    for element in listcar:
        for i, lst in enumerate(grid):
            for k, item in enumerate(lst):
                if item == element:
                  
                    print(i, k) #i = row dove si trova numero, k = col dove si trova number
                    grid[i][k] = Carviz().VALUE
    return next
                


def Growing():
    #in this way the vegetob gros on all grid with a random density in a random place
    for a in range(1, NUMCELL):
        for j in range(1, NUMCELL):
            if grid[a][j] != WATER:
                #RANGE_VEGETOB_GROWING_COL= random.randint(1, NUMCELL-2)
                #RANGE_VEGETOB_GROWING_ROW= random.randint(1, NUMCELL-2)
                grid[a][j] = Vegetob().DENSITY

                if grid[a][j] == 0: #if there is no vegetob, draw only ground, (300)
                    grid[a][j] = GROUND


                  
            j +=1
        a +=1







def Draw_Map(grid):

    #water has to be all around
    for col in range(0, NUMCELL):
        grid[col][-1] = WATER #two sides are always water
        grid[col][0] = WATER

        if col == 0:
            for i in range(1, NUMCELL):
                grid[col][-i] = WATER

        if col == NUMCELL-1:
            for i in range(1, NUMCELL):
                grid[col][-i] = WATER

    #inside is random water and ground
    
    #for i in range(NUMCELL*NUMCELL):
        for a in range(1, NUMCELL-1):
            for j in range(1, NUMCELL-1):
                if grid[a][j] == 0:
                    RANGE_VEGETOB_GROWING_COL= random.randint(1, NUMCELL-2)
                    RANGE_VEGETOB_GROWING_ROW= random.randint(1, NUMCELL-2)

                    WATER_OR_GROUND = random.choice(MATERIALS)
                    grid[a][j] = WATER_OR_GROUND
                    cell = Cell()
                    cell.ground_water(WATER_OR_GROUND)
                    
                    if WATER_OR_GROUND == GROUND:
                        #Cell().list_GROUND.append(WATER_OR_GROUND)
                        #cell = Cell()
                        #cell.add_ground()
                        pass

                    if WATER_OR_GROUND == WATER:
                        #cell = Cell()
                        #cell.add_water()
                        pass
 
                j +=1 
            a +=1
    #print(grid) #the grid here only has round and water


def Spawn_Erbast():
    #we have to spawn the erbast insiede the ground only
    NUMCELL_RANGE = random.randint(0, NUMCELL)
    for a in range(1, NUMCELL_RANGE):
        for j in range(1, NUMCELL_RANGE):
            if 0<= grid[a][j] <= 100:
                grid[a][j] = Erbast().VALUE
            j +=1
        a +=1

def Spawn_Carviz():
    #we have to spawn the erbast insiede the ground only
    NUMCELL_RANGE = random.randint(0, NUMCELL)

    for a in range(1, NUMCELL_RANGE):
        for j in range(1, NUMCELL_RANGE):
            if 0 <= grid[a][j] <= 100 and grid[a][j] != Erbast().VALUE:
                grid[a][j] = Carviz().VALUE
            j +=1
        a +=1


grid = grid_init(NUMCELL)
Draw_Map(grid) #we draw a water ground map

Growing() #vegetob can grow only on ground
Spawn_Erbast() #spawn erbast on ground in random order
Spawn_Carviz() #spawn carviz on ground in random order where there isent a erbast

grid_display(grid, NUMCELL) #print the grid with everything
#grid = the grid with everything insiede



steps = 3 # duration of the simulation

for s in range(1, steps+1):
    #Movement(grid)
    print("time: ", s)
    grid = Movement(grid)
    #Growing()
    grid_display(grid, NUMCELL)
    #print(grid) '''



#grid  = the grid with vegetob


# visualization
#grid_display(grid, NUMCELL)

""" for s in range(1, steps+1):
    # next generation
    print('time:', s)
    grid = grid_evolve(grid, NUMCELL)
    grid_display(grid, NUMCELL) """

