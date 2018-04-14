from randomizer import Randomizer

def main():
    randomizer = Randomizer()
    for i in range(1001):
        res = randomizer.random()
        output(res, i)

def output(x, i, file_out='dataset.csv'):
    with open(file_out, 'a') as file:
        file.write(str(i) + ',' + str(x) + '\n')

if __name__ == '__main__':
    main()
