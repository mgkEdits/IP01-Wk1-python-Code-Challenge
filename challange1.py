# Challenge 1: Converting 12-hour time to 24-hour time
def convert_to_24_hour(hour,minute, period):
     
    if minute >59 or hour >12:
        return("Error in time, please try again")

    if period.lower() == "pm" and hour < 12:
        hour += 12
    elif period.lower() == "am" and hour == 12:
        hour = 0
    return f"{hour:02d}{minute:02d}"

# Test cases
print(convert_to_24_hour(13,50, "am"))  