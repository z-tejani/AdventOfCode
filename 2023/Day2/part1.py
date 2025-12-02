
filepath = "data.txt"

max_cubes = {'red': 12, 'green': 13, 'blue': 14}

sum = 0
with open(filepath, "r") as my_file:
    for game in my_file:
        split_line = game.split(':')
        game_num = int(split_line[0].split(' ')[-1])
        subsets = split_line[1].split(';')
        all_games_valid = True
        for subset in subsets: 
            colors = subset.split(',')
            for color in colors:
                nums = color.strip().split(' ')
                if max_cubes[nums[-1]] < int(nums[0]):
                    all_games_valid = False  

        if(all_games_valid):
            sum += game_num

print(sum)