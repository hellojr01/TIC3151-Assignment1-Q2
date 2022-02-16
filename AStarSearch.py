from queue import PriorityQueue

# Declaring the heuristic function as manhattan distance
def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2
    return abs(x1-x2) + abs(y1-y2)

def aStar(m,start,goal):
    # start=(m.rows,m.cols)
    # inf = infinity
    g_score={cell:float('inf') for cell in m.grid} # distance from the start node
    print(g_score)
    g_score[start]=0
    f_score={cell:float('inf') for cell in m.grid} # total cost by summing up the g and h 
    f_score[start]=h(start,goal)

    open=PriorityQueue() # Priority queue is looking for the f which is having the lowest value
    open.put((h(start,goal),h(start,goal),start))
    aPath={}
    
    while not open.empty():
        currCell=open.get()[2]
        if currCell==goal:
            break
        for d in "ESNW":
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                if d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                if d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_g_score=g_score[currCell]+1
                temp_f_score=temp_g_score+h(childCell,goal)

                if temp_f_score < f_score[childCell]:
                    g_score[childCell]=temp_g_score
                    f_score[childCell]=temp_f_score
                    open.put((temp_f_score,h(childCell,goal),childCell))
                    aPath[childCell]=currCell

    
    fwdPath={}
    cell=goal
    
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return fwdPath