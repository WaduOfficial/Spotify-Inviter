#Credits to Wadu
import random, string
print('How many codes should be generated? \n')
amount = int(input())
f = open('keys.txt', 'a')
fix = 0
while fix <= amount:
    x = ('').join(random.choices(string.ascii_letters + string.digits, k=40))
    print(x)
    f.write(x + '\n')
    fix += 1

f.close()