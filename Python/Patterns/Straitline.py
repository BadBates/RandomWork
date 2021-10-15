import argparse
def Straitline(n):
    for row in range(1, n+1):
        start_index = (n-row)
        print("" * start_index, end = "")
        for star in range(row * row -1):
            if star %2 ==0:
                print("*", end = "")
            else:
                print("", end = "")
            #print("")    #add this to make it vertical.
            
Straitline(5)