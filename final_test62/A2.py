# ประโยคภาษาอังกฤษที่จะถูกเรียกว่าเป็นประโยคเต้นรำ (Dancing Sentence) ก็ต่อเมื่อตัวอักษรแรกของประโยคนั้นเป็นตัวอักษรตัวพิมพ์ใหญ่ และตัวอักษรถัดไปจะมีรูปแบบตัวพิมพ์ตรงข้ามกับตัวก่อนหน้า โดยไม่นับรวมช่องว่างในประโยค
# เช่น ประโยค "A bOoK" เป็นประโยคเต้นรำ เนื่องจากตัวอักษรแรก (A) เป็นตัวพิมพ์ใหญ่
# ถัดไป (b) เป็นตัวพิมพ์เล็ก
# ถัดไป (O) เป็นตัวพิมพ์ใหญ่
# ถัดไป (o) เป็นตัวพิมพ์เล็ก
# และถัดไป (K) เป็นตัวพิมพ์ใหญ่
# ให้นิสิตเขียนโปรแกรมเพื่อเปลี่ยนประโยคภาษาอังกฤษที่รับเข้ามาให้เป็นประโยคเต้นรำ
# ข้อมูลเข้า
# บรรทัดที่ 1 เป็นจำนวนเต็มบวก N แทนจำนวนกรณีทดสอบ
# N บรรทัดต่อไป แต่ละบรรทัด เป็นประโยคที่ต้องการเปลี่ยนเป็นประโยคเต้นรำ
# ข้อมูลออก
# มีจำนวน N บรรทัด แต่ละบรรทัดแสดงประโยคที่เปลี่ยนเป็นประโยคเต้นรำแล้วของแต่ละกรณีทดสอบ โดยการเปลี่ยนรูปแบบของตัวพิมพ์ใหญ่-เล็กตามรูปแบบที่กำหนด และคงสภาพช่องว่างไว้ตามเดิม

def dancing():
    text = input()
    dancingText = ""
    dance = True
    
    for t in text:
        if t == " ":
            pass
        else:
            if dance:
                t = t.upper()
                dance = False
            else:
                t = t.lower()
                dance = True
            
        dancingText += t
        
    return dancingText

n = int(input(""))
total = []
counter = 0

while True:
    if counter >= n:
        break
    
    total.append(dancing())
    
    counter += 1

for i in total:
    print(i)