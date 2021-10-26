import argparse
#n = int(input("how many rows for the triangle?:"))

def right_triangle(n):
    for row in range(1, n+1):
        start_index = (n-row)
        print(" " * start_index, end = "")
        for star in range(row):
            print("*", end= "")
        
        print("")

right_triangle(5)