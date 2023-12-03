chicken_menu = 10.35
fish_menu = 12.40
veg_menu = 8.15

num_chicken_menu = int(input()) * chicken_menu
num_fish_menu = int(input()) * fish_menu
num_veg_menu = int(input()) * veg_menu

order = num_chicken_menu + num_fish_menu + num_veg_menu
desert = order * 0.20
total_order = order + desert + 2.50
print(f"{total_order}")
