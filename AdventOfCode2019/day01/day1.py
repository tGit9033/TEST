
def main():
    total = 0;
    with open("input", "r") as f1:
        for line in f1:
            x = int(line)
            total += x // 3 - 2;
            
        print("total = %d" %(total))
            
if __name__ == "__main__":
	main()
