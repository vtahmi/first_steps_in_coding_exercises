length = int(input())
width = int(input())
height = int(input())
percent_taken = float(input()) / 100
tank_volume_litres = length * width * height
tank_volume = tank_volume_litres / 1000
total_tank_volume = tank_volume * percent_taken
total = tank_volume - total_tank_volume
print(total)


