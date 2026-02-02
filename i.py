def area_cal(x,y):
    reg_cal = x * y
    tri_cal = (1/2) * x * y
    return (reg_cal, tri_cal)

reg, tri = area_cal(5,3)
print(f'พื้นที่คำนวนสี่เหลี่ยม  : {reg}')
print(f'พื้นที่คำนวนสามเหลี่ยม : {tri}')
