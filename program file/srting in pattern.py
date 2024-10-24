def printPattern(s):
    n = len(s)
    for i in range (0, n):
        for j in range(0, n - i) :
            print(s[j], end = "")
        print("")       
s =input()
printPattern(s)
  