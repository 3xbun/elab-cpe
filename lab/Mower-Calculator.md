# ค่าตัดหญ้า
กำหนดให้อาณาเขตของตัวบ้าน (house) และรั้วบ้าน (block) เป็นรูปสี่เหลี่ยมผืนผ้า พื้นที่รอบตัวบ้านเป็นสนามหญ้าทั้งหมด
จงเขียนโปรแกรมเพื่อรับความกว้างและยาวของรั้วบ้าน และความกว้างและยาวของตัวบ้านในหน่วยเมตร เพื่อคำนวณหาค่าใช้จ่ายในการตัดหญ้า (mowing cost) เมื่อกำหนดให้อัตราค่าตัดหญ้าคิดเป็น 35 บาทต่อตารางเมตร

## ข้อมูลเข้า
* บรรทัดแรก แสดงข้อความ "Enter block length: " และรอรับจำนวนเต็ม แทนความยาวของรั้วบ้าน
* บรรทัดที่สอง แสดงข้อความ "Enter block width: " และรอรับจำนวนเต็ม แทนความกว้างของรั้วบ้าน
* บรรทัดที่สาม แสดงข้อความ "Enter house length: " และรอรับจำนวนเต็ม แทนความยาวของตัวบ้าน
* บรรทัดที่สี่ แสดงข้อความ "Enter house width: " และรอรับจำนวนเต็ม แทนความกว้างของตัวบ้าน

โดยข้อมูลนำเข้าในชุดทดสอบ ขนาดพื้นที่ของรั้วบ้านมีค่ามากกว่าหรือเท่ากับของตัวบ้านเสมอ

## ตัวอย่าง Input/Output
> Enter block length: `12`
>
> Enter block width: `9`
>
> Enter house length: `7`
>
> Enter house width: `6`
>
> Mowing cost is 2310 baht.

### *เฉลย*
```python
blen = int(input('Enter block length: '))
bwid = int(input('Enter block width: '))
hlen = int(input('Enter house length: '))
hwid  = int(input('Enter house width: '))

barea = blen * bwid
harea = hlen * hwid

price = ((barea * 35) - (harea * 35))
print('Mowing cost is ' + str(price) + ' baht.')
```
