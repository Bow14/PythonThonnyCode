from os.path import exist
import sys

def main():
    filename = input("Enter File name")
    
    if not exist(filename):
        print("Dosent Exist")
        
        return
    
if __main__ == "__main__":
    main()