s1 = input("Enter your exercise time 1 (sec): ")
s2 = input("Enter your exercise time 2 (sec): ")
s3 = int(s1) + int(s2)
hrs = s3 // 3600
s3 = s3 - (int(hrs) * 3600)
mins = s3 // 60
sec = s3 - (int(mins) * 60)
print("It is", str(hrs), "hours", str(mins), "minutes and", str(sec), "seconds.")
