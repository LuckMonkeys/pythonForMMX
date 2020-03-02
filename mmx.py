
cipher = []
cipherorigin = ['chreevoahmaeratbiaxxwtnxbeeophbsbqmqeqerbwrvxuoakxaosxxweahbwgjmmqmnkgrfvgxwtrzxwiaklxfpskautemndcmgtsxmxbtuiadngmgpsrelxnjelxvrvprtulhdnqwtwdtygbphxtfaljhasvbfxngllchrzbwelekmsjiknbhwrjgnmgjsglxfeyphagnrbieqjtamrvlcrremndglxrrimgnsnrwchrqhaeyevtaqebbipeewevkakoewadremxmtbhhchrtkdnvrzchrclqohpwqaiiwxnrmgwoiifkee']
for i in cipherorigin[0]:
    cipher.append(ord(i)-ord('a'))
p = [0.082,0.015,0.028,0.043,0.127,0.022,0.02,0.061,0.07,
     0.002,0.008,0.04,0.024,0.067,0.075,0.019,0.001,0.06,
     0.063,0.091,0.028,0.01,0.023,0.001,0.02,0.001]
k0 = []
k1 = []
k2 = []
k3 = []
k4 = []

m0 = []
m1 = []
m2 = []
m3 = []
m4 = []

for i in range(0,26):
    k0.append(0)
    k1.append(0)
    k2.append(0)
    k3.append(0)
    k4.append(0)

#分离
#统计每个字母频率
#添加基数从0-25

for i in range(0,len(cipher)):
    if(i%5 ==0):
        k0[cipher[i]] = k0[cipher[i]]+1
    elif(i%5 ==1):
        k1[cipher[i]] = k1[cipher[i]] + 1
    elif(i % 5 == 2):
        k2[cipher[i]] = k2[cipher[i]]+1
    elif(i % 5 == 3):
        k3[cipher[i]] = k3[cipher[i]]+1
    elif(i % 5 == 4):
        k4[cipher[i]] = k4[cipher[i]]+1
    else:
        print('Error!')


sumM = 0
for g in range(0,26):
    for i in range(0,26):
        sumM = sumM + p[i]*((k0[(i+g)%26])/sum(k0))
    m0.append(round(sumM,3))
    sumM = 0

for g in range(0,26):
    for i in range(0,26):
        sumM = sumM + p[i]*((k1[(i+g)%26])/sum(k1))
    m1.append(round(sumM,3))
    sumM = 0

for g in range(0,26):
    for i in range(0,26):
        sumM = sumM + p[i]*((k2[(i+g)%26])/sum(k2))
    m2.append(round(sumM,3))
    sumM = 0

for g in range(0,26):
    for i in range(0,26):
        sumM = sumM + p[i]*((k3[(i+g)%26])/sum(k3))
    m3.append(round(sumM,3))
    sumM = 0

for g in range(0,26):
    for i in range(0,26):
        sumM = sumM + p[i]*((k4[(i+g)%26])/sum(k4))
    m4.append(round(sumM,3))
    sumM = 0

print(m0)
print(m1)
print(m2)
print(m3)
print(m4)
