from datetime import datetime, timedelta


def get_days_from_today(date):
    try:
        current_datetime = datetime.today().date()
        print(current_datetime)
        datetime_objects = datetime.strptime(date, "%Y-%m-%d").date()
        difference = (current_datetime - datetime_objects).days
        print(f"Difference in days: {abs(difference)}")
        return abs(difference)
    except ValueError:
        print("Incorrect date format")
        return None

#Restart if Error
while True:
    date = str(input("Enter your date in the format YYYY-MM-DD: "))
    if get_days_from_today(date) is not None:
        break