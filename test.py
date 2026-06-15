from datetime import datetime
a = "09:00"
b = "10:00"
a_time = datetime.strptime(a,"%H:%M")
b_time = datetime.strptime(b,"%H:%M")
print((a_time - b_time).seconds/3600 )