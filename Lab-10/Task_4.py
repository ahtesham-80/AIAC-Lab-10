def calculate_average(scores):
    total = 0
    for s in scores:
        total += s
    return total / len(scores)

def find_highest(scores):
    highest = scores[0]
    for s in scores:
        if s > highest:
            highest = s
    return highest

def find_lowest(scores):
    lowest = scores[0]
    for s in scores:
        if s < lowest:
            lowest = s
    return lowest

def process_scores(scores):
    avg = calculate_average(scores)
    highest = find_highest(scores)
    lowest = find_lowest(scores)

    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)
print(process_scores([10, 20, 30, 40, 50]))







