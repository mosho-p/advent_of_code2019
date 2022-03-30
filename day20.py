with open('day20data.txt') as f:
    s = f.read()

print(s.count('Tile'))

# if there are exactly 4 tiles that have 2 edges that don't appear anywhere else then those must be the tiles
