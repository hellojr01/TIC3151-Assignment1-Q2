def IDS(m, start):
    level = 0
    frontier = [(level, start)]
    explored = [start]
    
    idsPath = {}
    while len(frontier) > 0:
        currCell = frontier.pop(0)
        cell = currCell[1]
        level = currCell[0] + 1

        if cell == m._goal:
            break
        
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
                    childCell = (cell[0], cell[1]+1)

                # if the location has been explored                
                if childCell in explored:
                    continue
                explored.append(childCell)

                frontier.append((level, childCell))
                # Set parent of this neighbor to the current cell
                idsPath[childCell] = cell 

    # Trace back from the goal to the START cell
    fwdPath = {}
    while cell != start:
        fwdPath[idsPath[cell]] = cell
        cell = idsPath[cell]

    return fwdPath