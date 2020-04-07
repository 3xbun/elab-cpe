# ขณะที่คุณกำลังทำรายงานสำหรับส่งในวิชาภาษาอังกฤษ เครื่องพิมพ์ของคุณได้ติดไวรัสคอมพิวเตอร์และทำให้เครื่องพิมพ์ทำงานผิดพลาด
# หลังจากที่พิมพ์รายงานเพี้ยน ๆ ออกมาได้ 3 หน้าแล้ว คุณได้สังเกตว่าข้อความที่พิมพ์ออกมาจากเครื่องพิมพ์แต่ละบรรทัดนั้นพิมพ์จากด้านในของประโยคออกมา
# หรือกล่าวว่าประโยคแต่ละบรรทัดถูกแบ่งครึ่ง แต่ละครึ่งจะพิมพ์จากตัวสุดท้ายมาตัวแรก
# ตัวอย่างเช่น ประโยค "THIS LINE IS GIBBERISH"
# จะถูกพิมพ์โดยเครื่องพิมพ์ที่ติดไวรัสเป็น "I ENIL SIHTHSIREBBIG S"
# หรือประโยค " ABCDEF "
# จะถูกพิมพ์เป็น "CBA  FED"
# งานของคุณคือให้เขียนโปรแกรมเพื่อเปลี่ยนข้อความที่ถูกพิมพ์ด้วยเครื่องพิมพ์ที่ติดไวรัสเป็นข้อความที่ถูกต้อง
# ข้อมูลเข้า
# บรรทัดแรก เป็นจำนวนเต็มบวก N แทนจำนวนกรณีทดสอบ
# N บรรทัดต่อไป แต่ละบรรทัด เป็นข้อความที่ถูกพิมพ์ด้วยเครื่องพิมพ์ที่ติดไวรัส ซึ่งจะมีจำนวนตัวอักษรเป็นจำนวนคู่เสมอ
# ข้อมูลออก
# มีจำนวน N บรรทัด แต่ละบรรทัดแสดงประโยคที่ถูกต้องซึ่งจะถูกพิมพ์หากเครื่องพิมพ์ไม่ติดไวรัส
# ตัวอย่างข้อมูลออก/ข้อมูลออก
# ข้อมูลเข้า	ข้อมูลออก

                
# 4
# I ENIL SIHTHSIREBBIG S
# RETUPMOCECNEICS-
# N rof spiT 01srepoleveD we
# L .taerg era yehTsediug eht ta koo
                

            	
                
# THIS LINE IS GIBBERISH
# COMPUTER-SCIENCE
# 10 Tips for New Developers
# They are great. Look at the guides
                

            

                
# 4
# elpmaxe roF:enil eht ,
# i enil sihT""hsirebbig s
# p gnieb si:sa detnir
# This line i""s gibberish
                

            	
                
# For example, the line:
# "This line is gibberish"
# is being printed as:
# "i enil sihThsirebbig s"
                
def coding():
    text = input()
    count = len(text)//2


    first = list(text[:count])
    second = text[count:]
    fullText = ""

    for i in range(len(first)):
        i += 1
        fullText += first[-i]

    for i in range(len(second)):
        i += 1
        fullText += second[-i]

    return fullText

n = int(input(""))
total = []
counter = 0

while True:
    if counter >= n:
        break

    total.append(coding())
    
    counter += 1

for i in total:
    print(i)