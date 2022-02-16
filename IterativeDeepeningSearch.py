

def IDS(m, start):
    depth_count = 0
    frontier = [(depth_count, start)]
    explored = [start]
    
    dfsPath = {}
    while len(frontier) > 0:
        frontier.sort(key=lambda x: x[0])
        currCell = frontier.pop(0)
        cell = currCell[1]

        depth_count = currCell[0] + 1

        # explored.append(cell)
        
        # Finding neighbor cells
        for d in "EWSN":
            # A cell has 4 direction East, West, North, and South
            # If the direction has a wall prevent agent to move
            # Then the value of that direction is False, else True
            if m.maze_map[cell][d] == True:
                if d=="N":
                    childCell = (cell[0]-1, cell[1])
                elif d=="S":
                    childCell = (cell[0]+1, cell[1])
                elif d=="W":
                    childCell = (cell[0], cell[1]-1)
                elif d=="E":
                    # next cell
                    # coordinate (row,column)
                    childCell = (cell[0], cell[1]+1)

                # if the location has been explored                
                if childCell in explored:
                    continue
                explored.append(childCell)

                frontier.append((depth_count, childCell))
                # Set parent of this neighbor to the current cell
                dfsPath[childCell] = cell

                if childCell == m._goal:
                    break

    # Trace back from the goal to the START cell
    fwdPath = {}
    while cell != start:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]

    return fwdPath