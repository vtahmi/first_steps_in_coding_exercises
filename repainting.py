plastic = int(input())
plastic_price = (plastic + 2) * 1.50
paint = int(input())
paint_more = paint * 0.10
paint_price = (paint + paint_more) * 14.50
dilute = int(input())
dilute_price = dilute * 5
total_before = plastic_price + paint_price + dilute_price + 0.40
labour_hours = int(input())
labour_price_hour = (total_before * 0.30) * labour_hours
total = plastic_price + paint_price + dilute_price + labour_price_hour + 0.40
print(f"{total}")
