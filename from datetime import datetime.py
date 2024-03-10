from datetime import datetime


def get_days_from_today(date):
    try:
        specific_date = datetime.strptime(date, "%Y-%m-%d")
        difference = today_date - specific_date
        return difference.days
    except ValueError:
        return "Неправильный формат даты"


date = "2022-02-24"
today_date = datetime.today()

print(
    f" Количество дней с  {date} до сегодня прошло {get_days_from_today(date)} "
)
