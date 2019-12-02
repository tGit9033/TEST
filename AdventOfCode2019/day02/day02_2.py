import csv

def op1(pos1, pos2):
	ans = pos1 + pos2;
	return ans;

def op2(pos1, pos2):
	ans = pos1 * pos2;
	return ans;

def compute(l):
    i = 0
    length = len(l)
    opCode = l[i];
    while(99 != opCode and i < length):
        opCode = l[i]
        if (1 == opCode):
            l[l[i+3]] = op1(l[l[i+1]], l[l[i+2]])
        if (2 == opCode):
            l[l[i+3]] = op2(l[l[i+1]], l[l[i+2]])
        i+=4
        
    return l;


def computeMain(p1, p2):
    ans = []
    with open('input', 'r') as f1:
        reader = csv.reader(f1);
        x = list(reader)[0]
        x = [int(i) for i in x]
        x[1] = p1;
        x[2] = p2;
        ans = compute(x)
    return ans[0]

def m():
    for i in range(100):
        for j in range(100):
            if 19690720 == computeMain(i,j):
                return (i,j)
        
def main():          
    x = m()
    ans = 100*x[0] + x[1]
    print("ans=100*%d + %d = %d" %(x[0], x[1], ans));

def test_compute():
	assert compute([1,0,0,0,99]) == [2,0,0,0,99]
	assert compute([2,3,0,3,99]) == [2,3,0,6,99]
	assert compute([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
	assert compute([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]

if __name__ == "__main__":
	main();