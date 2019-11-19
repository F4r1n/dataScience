import os

for filename in os.listdir('./data/'):
    print(filename)
    if os.stat('./data/' + filename).st_size == 0:
        os.remove('./data/' + filename)
