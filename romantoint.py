s="III"

romans = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
l = len(s)

result = 0
for i in range(l-1):
    if romans[s[i]] > romans[s[i+1]]:
        result+=romans[s[i]]
    elif romans[s[i]] == romans[s[i+1]]:
        result+=romans[s[i]]
    else:
        result+=romans[s[i+1]]-romans[s[i]]
print(result)