import prime
counter = 0
recp = 0
while True:
    counter = counter + 1
    recp = recp + (1/prime.prime(counter))
    print(recp)