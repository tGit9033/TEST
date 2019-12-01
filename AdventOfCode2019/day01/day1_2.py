def main():
    total = 0;
    with open("input", "r") as f1:
        for line in f1:
            x = int(line)
            total += compute(x);
                
            
        print("total = %d" %(total))
            
def compute(mass):
    fuel = 0;
    while (mass > 0):
        mass = mass // 3 - 2; 
        if (mass > 0 ):
            fuel += mass
    return fuel;
    
if __name__ == "__main__":
	main()
