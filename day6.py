class Planet:
    def __init__(self, orbits):
        self.orbits = orbits

if __name__ == '__main__':
    with open('day6data.txt') as f:
        planets = {p.split(')')[1]: p.split(')')[0] for p in f.read().strip().split('\n')}

    ## Part 1
    # total = 0
    # for k, v in planets.items():
    #     orbits = 1
    #     while v != 'COM':
    #         v = planets[v]
    #         orbits += 1
    #     total += orbits
    # print(total)
    
    ## Part 2
    my_path = set()
    santa_path = set()
    my_planet = planets['YOU']
    santa_planet = planets['SAN']
    while my_planet != 'COM':
        my_path.add(my_planet)
        my_planet = planets[my_planet]
    while santa_planet != 'COM':
        santa_path.add(santa_planet)
        santa_planet = planets[santa_planet]
    print(len(my_path.symmetric_difference(santa_path)))