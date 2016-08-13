# Enter your code here. Read input from STDIN. Print output to STDOUT
from Queue import PriorityQueue

def heuristic(grid,k):
    h =0
    for i in xrange(0,k):
        for j in xrange(0,k):
            if(grid[i][j]==i*k+j):
                h=h+1                
    return h

def heuristicMan(grid,k):
    h =0
    for i in xrange(0,k):
        for j in xrange(0,k):
            el = grid[i][j]
            if(el!=0):
                correct_pos_r = el//k
                correct_pos_c = el%k
                h = h + abs(correct_pos_r-i) + abs(correct_pos_c - j)              
    return -h

def reshape1D(grid,k):
    newgrid = [None for i in range(k*k)]
    for i in xrange(0,k):
        for j in xrange(0,k):
            newgrid[i*k+j] = grid[i][j]
    return newgrid

def generateKey(grid,k):
    return ''.join(str(x) for x in reshape1D(grid,k))


def copyGrid(grid,k):
    newgrid =  [[0 for i in range(k)] for j in range(k)]
    for i in xrange(0,k):
        for j in xrange(0,k):
            newgrid[i][j] = grid[i][j]
    return newgrid

def findPos(grid,k):
    newgrid = reshape1D(grid,k)
    return (newgrid.index(0)//k,newgrid.index(0)%k)

def generateGoal(grid,k):
    return ''.join(str(x) for x in [i for i in range(k*k)])

def nextMove(grid,k):
       
    queue =  PriorityQueue()    
    links = dict()
    moves = dict()
    cost_so_far = dict()
    
    grid_key = generateKey(grid,k)
    goal = generateGoal(grid,k)
   
    links[grid_key] = None
    moves[grid_key]= None
    
    cost_so_far[grid_key] = 0    
    queue.put(grid,0)
    
    while not queue.empty():
        
        grid = queue.get()
        grid_key = generateKey(grid,k)
        
        if(heuristicMan(grid,k) == 0):
            break
            
        pos = findPos(grid,k)
        blank_r = pos[0]
        blank_c = pos[1]
        
        up_pos = (blank_r-1,blank_c)
        left_pos = (blank_r,blank_c-1)
        right_pos = (blank_r,blank_c+1)
        down_pos =(blank_r+1,blank_c)
        
        neighbours = [up_pos,left_pos,right_pos,down_pos]
       
        for i in range(0,4):
            nextPos = neighbours[i]
            r = nextPos[0]
            c = nextPos[1]
            
            if(r>=0 and r<k and c>=0 and c<k):
                newgrid = copyGrid(grid,k)
                newgrid[blank_r][blank_c] = grid[r][c]
                newgrid[r][c]  = 0
                newgrid_key = generateKey(newgrid,k)
                new_cost = cost_so_far[grid_key] + 1
                if (newgrid_key not in cost_so_far or new_cost < cost_so_far[newgrid_key]):
                    cost_so_far[newgrid_key] = new_cost
                    priority = new_cost + heuristicMan(newgrid,k)
                    queue.put(newgrid, priority)
                    links[newgrid_key] = grid_key
                    if(blank_r - r > 0):
                        moves[newgrid_key] = 'UP'
                    elif(blank_r - r < 0):
                        moves[newgrid_key] = 'DOWN'
                    elif(blank_c - c > 0):
                        moves[newgrid_key] = 'LEFT'
                    elif(blank_c - c < 0):
                        moves[newgrid_key] = 'RIGHT'                 
                    
     
    cameFrom = links[goal]
    path =[moves[goal]]
    while cameFrom != None:  
        if(moves[cameFrom]!=None):
            path = [moves[cameFrom]] + path
        cameFrom = links[cameFrom]   
    
    print len(path)
    #print(','.join("'" + str(x) + "'" for x in path))
    for x in path:
        print(x)     
        
k = int(raw_input().strip())
grid =  [[0 for i in range(k)] for j in range(k)]

for i in xrange(0, k):
    for j in xrange(0,k):
        grid[i][j] = int(raw_input().strip())
        

nextMove(grid,k)

