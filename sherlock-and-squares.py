def squares(x,y):
  count = 0
  if min(x,y)**0.5 == int(min(x,y)**0.5):
    start = min(x,y)**0.5
  else:
    start = int(min(x,y)**0.5) + 1
  while start**2 < max(x,y)+1:
    count += 1
    start += 1
  return count

test_cases = int(raw_input().strip())

for _ in xrange(test_cases):
    a,b = (int(i) for i in raw_input().strip().split())
    print squares(a,b)
