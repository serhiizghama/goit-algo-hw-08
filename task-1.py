import heapq


def calculate(cables):
    # Create a min-heap from the list of cables
    heapq.heapify(cables)
    costs = []

    # While there is more than one element in the heap
    while len(cables) > 1:
        # Pop the two smallest cables
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)
        # Total cost of connecting the two cables
        total = cable1 + cable2
        # Append the connection cost to the costs list
        costs.append(total)
        # Push the new cable back into the heap
        heapq.heappush(cables, total)

    return costs


if __name__ == "__main__":
    cables = [55, 49, 63, 73, 83, 43, 53]
    costs = calculate(cables)

    # Check if the costs list is not empty
    if costs:
        print("Min cost: ", costs[0])
        print("Total costs: ", sum(costs))
    else:
        print("No costs calculated.")
