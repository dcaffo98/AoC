from collections import OrderedDict


DIGITS = OrderedDict(zip('one two three four five six seven eight nine'.split(' '), range(1, 10)))
NOT_FOUND = ('', float('inf'))

if __name__ == '__main__':
    values = []
    with open('data/2023/01/calibration_document.txt', 'r') as f:
        for line in f:
            try:
                first_w = min(
                    [tpl for tpl in ((word, line.find(word)) for word in DIGITS) if tpl[-1] != -1],
                        key=lambda x: x[1]
                )
            except (StopIteration, ValueError):
                first_w = NOT_FOUND
                
            try:
                first_n = next((c, idx) for idx, c in enumerate(line) if c.isdigit())
            except StopIteration:
                first_n = NOT_FOUND

            if first_w[1] < first_n[1]:
                first_digit = str(DIGITS[first_w[0]])
            else:
                first_digit = first_n[0]


            try:
                second_w = min(
                    [tpl for tpl in ((word, line[::-1].find(word[::-1])) for word in DIGITS) if tpl[-1] != -1],
                    key=lambda x: x[1]
                )
            except (StopIteration, ValueError):
                second_w = NOT_FOUND

            try:
                second_n = next((c, idx) for idx, c in enumerate(line[::-1]) if c.isdigit())
            except StopIteration:
                second_n = NOT_FOUND

            if second_w[1] < second_n[1]:
                second_digit = str(DIGITS[second_w[0]])
            else:
                second_digit = second_n[0]
            
            values.append(int(first_digit + second_digit))
    print(sum(values))