s = input()
cnt = 0
for i in range(0, len(s)):
    if s[i] == 'а':
        cnt += 1
        s = s.replace('а', 'о', 1)
print(cnt, len(s))