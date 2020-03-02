m = 5
cipher = []
cipherorigin = ['chreevoahmaeratbiaxxwtnxbeeophbsbqmqeqerbwrvxuoakxaos'
                'xxweahbwgjmmqmnkgrfvgxwtrzxwiaklxfpskautemndcmgtsxmxb'
                'tuiadngmgpsrelxnjelxvrvprtulhdnqwtwdtygbphxtfaljhasvbf'
                'xngllchrzbwelekmsjiknbhwrjgnmgjsglxfeyphagnrbieqjtamrv'
                'lcrremndglxrrimgnsnrwchrqhaeyevtaqebbipeewevkakoewadre'
                'mxmtbhhchrtkdnvrzchrclqohpwqaiiwxnrmgwoiifkee']
for i in cipherorigin[0]:
    cipher.append(ord(i)-ord('a'))
p = [0.082,0.015,0.028,0.043,0.127,0.022,0.02,0.061,0.07,
     0.002,0.008,0.04,0.024,0.067,0.075,0.019,0.001,0.06,
     0.063,0.091,0.028,0.01,0.023,0.001,0.02,0.001]

Mg =[[0 for i in range(26)] for i in range(m)]
Key = [[0 for i in range(26)] for i in range(m)]
for i in range(0,len(cipher)):
    Key[i%5][cipher[i]] = Key[i%5][cipher[i]] + 1
sumM = 0
for k in range(m):
    for g in range(26):
        sumM = 0
        for i in range(26):
            sumM = sumM + p[i]*((Key[k][(i+g)%26])/sum(Key[k]))
        Mg[k][g] = round(sumM,3)

for i in Mg:
    print(i)
