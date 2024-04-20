from datetime import datetime, timedelta


def get_days_from_today(date):
    try:
        current_datetime = datetime.now()
        datetime_objects = datetime.strptime(date, "%Y-%m-%d")
        difference = current_datetime - datetime_objects
        print(f"Difference in days: {abs(difference.days)}")
        return abs(difference.days)
    except ValueError:
        print("Incorrect date format")
        return None

#Restart if Error
while True:
    date = str(input("Enter your date in the format YYYY-MM-DD: "))
    if get_days_from_today(date) is not None:
        break