#assigment 1.1.1

scnd=int(input("a numebr of seconds is"))
hour=int(scnd/3600)
minute=int(scnd%3600/60)
second=int(scnd%60)
print("hours", hour)
print("minutes", minute)
print("seconds", second)

#assignment 1.1.2

f=float(input("value of money after 10 years"))
p=float(f/1.0299**10)
print("the money you need to deposit is", p)
