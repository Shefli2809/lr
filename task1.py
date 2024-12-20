def costMinimization(time, capacity):
    # Putting all the data we have into a dictionary
    data = {
        "XS": {
            "volume" : 10 , "cost" : {
                "Delhi" : 12,
                "Mumbai" : 14,
                "Kolkata" : 11
            }
        },
        "S": {
            "volume" : 20 , "cost" : {
                "Delhi" : 23,
                "Mumbai" : None,
                "Kolkata" : 20
            }
        },
        "M": {
            "volume" : 40 , "cost" : {
                "Delhi" : 45,
                "Mumbai" : 41.3,
                "Kolkata" : None,
            }
        },
        "L": {
            "volume" : 80 , "cost" : {
                "Delhi" : 77.4,
                "Mumbai" : 89,
                "Kolkata" : 67,
            }
        },
        "XL": {
            "volume" : 160 , "cost" : {
                "Delhi" : 140,
                "Mumbai" : 130,
                "Kolkata" : 118,
            }
        },
        "XXL": {
            "volume" : 320 , "cost" : {
                "Delhi" : 282,
                "Mumbai" : 297,
                "Kolkata" : None,
            }
        }
    }

    cities = ["Delhi", "Mumbai", "Kolkata"]

    # Handle base cases
    if time <= 0 or capacity <= 0:
        return [{"City": city, "Cost": 0, "boxes": {}} for city in cities]

    ans = []

    # Iterating through each city to give cost-minimized results
    for city in cities:

        # Processing the data to remove boxes which have "None" value
        boxesAvl = [
            (key, value["volume"], value["cost"][city])
            for key, value in data.items()
            if value["cost"][city] is not None
        ]

        # Min Cost per volume leads us to minimize the cost
        # Sorting boxes in ascending order of cost/volume
        boxesAvl.sort(key=lambda x: x[2] / x[1])

        remainingCapacity = capacity
        totalCost = 0
        chosenBoxes = {}

        # Iterating through sorted array of boxes
        for box, volume, cost in boxesAvl:
            if remainingCapacity <= 0:
                break

            # Calculate how many boxes are needed for the remaining capacity
            noOfBoxes = remainingCapacity // volume

            # Enters only if atleast 1 box of the next box type in 
            # cost per volume hierarchy can be completely filled
            if noOfBoxes > 0:
                chosenBoxes[box] = noOfBoxes
                totalCost += noOfBoxes * cost * time
                remainingCapacity -= noOfBoxes * volume

        # If remaining capacity is not zero, add the min cost box to fulfill
        if remainingCapacity > 0 and boxesAvl:
            # Find the box with the absolute lowest cost
            minBox = min(boxesAvl, key = lambda x: x[2])
            
            # Increasing the qty of boxes if already in chosen
            if minBox[0] in chosenBoxes:
                chosenBoxes[minBox[0]] += 1
            
            # Creating a new key value pair in the dictionary
            else: 
                chosenBoxes[minBox[0]] = 1

            # Adjusting the cost and remaining capacity
            totalCost += minBox[2] * time
            remainingCapacity -= minBox[1]

        ans.append({
            "City": city,
            "Cost": totalCost,
            "boxes": chosenBoxes
        })
    return ans

def printOutput(results, time, capacity):
    print(f"  Time: {time}")
    print(f"  Capacity: {capacity}\n")
    for result in results:
        print(f"   City: {result['City']}")
        print(f"    Total Cost: {result['Cost']}")
        print(f"    Boxes Allocated:")
        for box, cost in result["boxes"].items():
            print(f"     - {box}: {cost}")
        print()

# Sample Input 1
print("Test Case 1: Regular input")
time = 3
capacity = 1150
printOutput(costMinimization(time, capacity), time, capacity)

# Sample Input 2
print("\nTest Case 2: Zero Capacity")
time = 2
capacity = 0
printOutput(costMinimization(time, capacity), time, capacity)

# Sample Input 3
print("\nTest Case 3: Zero Time")
time = 0
capacity = 1000
printOutput(costMinimization(time, capacity), time, capacity)

# Sample Input 4
print("\nTest Case 4: Large Capacity")
time = 99
capacity = 999999
printOutput(costMinimization(time, capacity), time, capacity)

# Sample Input 5
print("\nTest Case 5: Minimum Capacity")
time = 1
capacity = 1
printOutput(costMinimization(time, capacity), time, capacity)