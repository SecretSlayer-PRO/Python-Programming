import datetime

# Getting current date and time
current_datetime = datetime.datetime.now()
print("Current Date and Time: ", current_datetime)

                                                            # Formatting a date
formatted_date = current_datetime.strftime("%d-%m-%Y")      # %Y means year part
print("Formatted Date: ", formatted_date)                   # %m means month part
                                                            # %d means date part