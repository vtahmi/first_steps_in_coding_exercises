pen_packs = int(input())
total_pen = pen_packs * 5.80
marker_packs = int(input())
total_marker = marker_packs * 7.20
litres_cleaning = int(input())
total_litres = litres_cleaning * 1.20
discount = int(input())
total = total_pen + total_marker + total_litres
total_discount = total * discount / 100
total_price = total - total_discount
print(total_price)
