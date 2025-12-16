import requests
from bs4 import BeautifulSoup
import pandas as pd
from cleaner import clean_data
import os

# URL سایت واقعی (مثال آموزشی)
url = "https://www.w3schools.com/html/html_tables.asp"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", {"id": "customers"})

output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

if table is None:
    print("No table found on the page. Scraping stopped.")
else:
    rows = []
    for tr in table.find_all("tr")[1:]:
        cells = tr.find_all("td")
        rows.append([cell.text.strip() for cell in cells])

    df = pd.DataFrame(rows, columns=["Name", "Country", "City"])

    # مسیر فایل‌های خروجی
    output_csv = os.path.join(output_folder, "cleaned_data.csv")
    report_file = os.path.join(output_folder, "report.txt")

    # فراخوانی تابع با تمام آرگومان‌ها
    cleaned_df, report = clean_data(df, output_csv, report_file)

    print("Scraping and cleaning completed successfully.")
    print(f"CSV saved at: {output_csv}")
    print(f"Report saved at: {report_file}")
