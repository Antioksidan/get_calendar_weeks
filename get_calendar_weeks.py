def get_calendar_weeks(year, month, start_day, end_day):
    start_date = date(year, int(month), start_day)
    end_date = date(year, int(month), end_day)
    
    calendar_weeks = []
    current_date = start_date
    while current_date <= end_date:
        calendar_week = current_date.isocalendar()[1]
        calendar_weeks.append(calendar_week)
        if month==1 and calendar_week==52:
            calendar_weeks.remove(calendar_week)
        current_date += timedelta(days=1)

    return np.unique(calendar_weeks)
