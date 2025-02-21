for i in range(1,10):
    print(i)
s = 0
for i in range(1,11):
    s += i
print(s)

counter = 0
sum = 0
while counter <= 10:
    sum += counter
    counter += 1
    print(counter)
print(f"Sum while using while is also {sum}")

# Infinite loop with for
# list = [1, 2]
# for i in list:
#     list.append(i+1)
#     print(i)