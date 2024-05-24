import heapq


def calculate(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        cost = heapq.heappop(cables) + heapq.heappop(cables)
        total_cost += cost
        heapq.heappush(cables, cost)

    return total_cost


if __name__ == "__main__":
    cables = [1, 2, 3, 4]
    costs = calculate(cables)

    print("Total costs: ", costs)
