import os, time, datetime

print(os.getcwd())

file = "./somefile.txt"
print(file)

print("Modified")
print(os.path.getmtime(file))

print()

print("Created")
print(os.path.getctime(file))

print()

modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("Date modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))

print()

created = os.path.getctime(file)
year,month,day,hour,minute,second=time.localtime(created)[:-3]
print("Date created: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))