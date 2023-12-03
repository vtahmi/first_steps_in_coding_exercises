total_pages = int(input())
pages_per_hour = int(input())
days_to_read_current_book = int(input())
hours = total_pages // pages_per_hour
hours_needed = hours / days_to_read_current_book
print(int(hours_needed))



