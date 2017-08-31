# แตกหน่วยวินาที
จงเขียนโปรแกรมเพื่อรับจำนวนวินาทีที่ใช้ออกกำลังกาย 2 ครั้ง แล้วแสดงผลเวลารวมที่ใช้ในการออกกำลังกายในรูปของจำนวนชั่วโมง นาที และวินาที ตามลำดับ

## ข้อมูลเข้า
* บรรทัดแรก แสดงข้อความ "Enter your exercise time 1: " และรอรับจำนวนเต็ม s1 แทนจำนวนวินาทีที่ใช้ออกกำลังกาย ครั้งที่ 1
* บรรทัดสอง แสดงข้อความ "Enter your exercise time 2: " และรอรับจำนวนเต็ม s2 แทนจำนวนวินาทีที่ใช้ออกกำลังกาย ครั้งที่ 2

## ข้อมูลออก
* แสดงจำนวนชั่วโมง นาที และวินาที ของเวลาออกกำลังกายรวมทั้งสองครั้ง ในรูปแบบตามตัวอย่าง

## ตัวอย่าง Input/Output
> Enter your exercise time 1: `345`
>
> Enter your exercise time 2: `440`
>
> It is 0 hours 13 minutes and 5 seconds.

### *เฉลย*
```python
s1 = input("Enter your exercise time 1: ")
s2 = input("Enter your exercise time 2: ")
s3 = int(s1) + int(s2)

hrs = s3 // 3600
s3 = s3 - (int(hrs) * 3600)
mins = s3 // 60
sec = s3 - (int(mins) * 60)

print("It is", str(hrs), "hours", str(mins), "minutes and", str(sec), "seconds.")
```
