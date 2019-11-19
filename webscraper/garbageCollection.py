import os
#cleaning up empty scrapted files which were uploaded as pdfs 
for filename in os.listdir('./data/'):
    print(filename)
    if os.stat('./data/' + filename).st_size == 0:
        os.remove('./data/' + filename)

#result: 27 files
