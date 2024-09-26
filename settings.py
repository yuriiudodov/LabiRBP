
DB_PATH                 = 'databaserbp'
SAVE_DIR ="C:\MHAD"
EXCEL_TEMPLATE_PATH = "C:/MHAD/shablon.xlsx"
MAIN_REPORT_PAGE        = 'Sheet1'
def date_format_from(date):
    year = date[0]
    month = date[1]
    day =date[2]
    return day+"."+month+"."+year

def date_format(date):
    date_day=str(date[8]+date[9])
    date_month = str(date[5]+date[6])
    date_year=str(date[0]+date[1]+date[2]+date[3])
    formated_date= date_day + "." + date_month + "." + date_year
    return formated_date