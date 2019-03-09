def fizzbuzz():
    range_fizzbuzz = []
    for i in range(1, 101):
        range_fizzbuzz.append(check_fizzbuzz(i))
    return ', '.join(map(str, range_fizzbuzz))

def check_fizzbuzz(num):
    if num % 15 == 0:
        return 'fizzbuzz'
    elif num % 3 == 0:
        return 'fizz'
    elif num % 5 == 0:
        return 'buzz'
    else:
        return num
