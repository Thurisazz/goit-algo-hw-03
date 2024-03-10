from datetime import datetime, timedelta


def get_upcoming_birthdays(users):

    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        next_birthday = birthday.replace(year=today.year)

        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)

        days_until_birthday = (next_birthday - today).days

        if days_until_birthday == 0 or (days_until_birthday == 1
                                        and today.weekday() == 5):
            next_birthday += timedelta(days=2)
        elif days_until_birthday == 0 or (days_until_birthday == 1
                                          and today.weekday() == 6):
            next_birthday += timedelta(days=1)

        if 0 <= days_until_birthday <= 7:
            upcoming_birthdays.append({
                "name":
                user["name"],
                "congratulation_date":
                next_birthday.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


users = [{
    "name": "John Doe",
    "birthday": "1985.01.23"
}, {
    "name": "Jane Smith",
    "birthday": "1990.03.7"
}]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
