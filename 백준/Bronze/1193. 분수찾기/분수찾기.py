n = int(input())

line = 0
end = 0  # 1, 2, 6, 10

while n > end:
    line += 1
    end += line

gap = end - n

if line % 2 == 0:
    bunmo = gap + 1  # 오름차순
    bunja = line - gap  # 내림차순

else:
    bunmo = line - gap
    bunja = gap + 1

print("%d/%d" % (bunja, bunmo))
