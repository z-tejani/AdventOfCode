
filepath = "data.txt"
totalPower = 0
with open(filepath, "r") as my_file:
    for game in my_file:
        split_line = game.split(':')
        game_num = int(split_line[0].split(' ')[-1])
        subsets = split_line[1].split(';')
        max_cubes = {'red': 0, 'green': 0, 'blue': 0}
        for subset in subsets: 
            colors = subset.split(',')
            for color in colors:
                nums = color.strip().split(' ')
                if int(nums[0]) > max_cubes[nums[-1]]:
                    max_cubes[nums[-1]] = int(nums[0])
        totalPower += (max_cubes['blue'])*(max_cubes['red'])*(max_cubes['green'])
        
print(totalPower)