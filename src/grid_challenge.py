def grid_challenge(grid) -> str:
    yes = 'YES'
    no = 'NO'
    grid_tmp = []

    # sorted row
    for row in grid:
        grid_tmp.append(sorted(row))
    
    # check col
    if len(grid_tmp) > 0:
        for i in range(len(grid_tmp[0])):
            col = [row[i] for row in grid_tmp]
            if col != sorted(col):
                return no

    return yes
