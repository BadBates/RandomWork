import argparse
def TrueTriangle(n):
    for row in range(1, n+1):
        start_index = (n-row)
        print("" * start_index, end = "")
        for star in range(row * row -1):
            if star %2 ==0:
                print("*", end = "")
            else:
                print("", end = "")
            print("")   
            
TrueTriangle(5)