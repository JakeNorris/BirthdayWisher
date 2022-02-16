import pandas
from datetime import datetime
import smtplib
from random import randint

# Enter your email and password here. You'll need to lower the security to allow third part apps access.
MY_EMAIL = ""
MY_PASSWORD = ""

today = (datetime.now().month, datetime.now().day)
# Enter your friend/family information to the birthday.csv prior to running.
data = pandas.read_csv("birthdays.csv")
# Use dict comprehension to set the birthdays_dict key to (month, day) from data
# and the value as the row of information.
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# If the birthdays_dict contains the today tuple then continue.
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    # Select one of three random birthday letter pre-set files.
    file_path = f"letter_templates/letter_{randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")

