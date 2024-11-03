from datetime import datetime

#13.1
with open("today.txt", "w") as file:
    file.write(datetime.now().strftime("%Y-%m-%d"))
#13.2
with open("today.txt", "r") as file:
    today_string = file.read()

print(today_string)

#13.3
parsed_date = datetime.strptime(today_string, "%Y-%m-%d")

print(parsed_date)