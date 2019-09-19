total = 0
i = 1

while i <= 20:
  if i % 3 == 0:
    i += 1
    continue
  total += i
  i += 1
print (total)
