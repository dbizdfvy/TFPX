def bresenham(x0, y0, x1, y1):
    """
    Bresenham's Line Algorithm
    Returns a list of coordinates representing the line from (x0, y0) to (x1, y1)
    """
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    
    line = []
    x, y = x0, y0
    
    while True:
        line.append([x, y])
        
        if x == x1 and y == y1:
            break
        
        err2 = 2 * err
        
        if err2 > -dy:
            err -= dy
            x += sx
        
        if err2 < dx:
            err += dx
            y += sy
    
    return line

def make_sublists(sorted_list):
    '''
    Given a sorted list, returns a nested list with each sublist consisting of elements with the same x coordinate.
    ex)

    sorted_list = [[0,0],[0,1],[0,2],[1,3],[1,6],[2,2]]
    make_sublists(sorted_list) returns [ [ [0,0],[0,1],[0,2] ],[ [1,3],[1,6] ],[ [2,2] ]].

    '''

    sublists = []
    current_x = None
    current_sublist = []
    
    for x, y in sorted_list:
        if x != current_x:
            if current_sublist:
                sublists.append(current_sublist)
                current_sublist = []
            current_x = x
        
        current_sublist.append([x, y])
    
    # Add the last sublist
    if current_sublist:
        sublists.append(current_sublist)
    
    return sublists


def polyPoints(vertices):
    '''
    Given a list of ordered vertices, returns a list of points within the polygon with the respective vertices.
    '''


    vertices.append(vertices[0]) 

    edges = []
    points = []


    for i in range(len(vertices) - 1):
        edges.extend(bresenham(vertices[i][0],vertices[i][1],vertices[i+1][0],vertices[i+1][1]))

    sortedList = make_sublists(sorted(edges))

    for i in range(len(sortedList)):
        for j in range(sortedList[i][0][1],sortedList[i][len(sortedList[i])-1][1]+1):
            points.append([sortedList[i][0][0],j])

    return points
