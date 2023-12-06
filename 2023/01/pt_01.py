if __name__ == '__main__':
    with open('data/2023/01/calibration_document.txt', 'r') as f:
        values = [int(
            next(c for c in line if c.isdigit()) + \
            next(c for c in line[::-1] if c.isdigit())) \
            for line in f
        ]
        print(sum(values))