n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
mime = {}
for i in range(n):
    ext, mt = input().split()
    mime[ext.lower()] = mt

for i in range(q):
    fname = input().split('.')  # One file name per line.
    try:
        if len(fname) > 1:
            print(mime[fname[-1].lower()])
        else:
            print("UNKNOWN")
    except:
        print("UNKNOWN")
