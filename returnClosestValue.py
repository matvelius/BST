class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # go left
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        # go right
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self


test = (BST(100).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22).insert(1).insert(1).insert(3).insert(1).insert(1).insert(502).insert(
    55000).insert(204).insert(205).insert(207).insert(206).insert(208).insert(203).insert(-51).insert(-403).insert(1001).insert(57).insert(60).insert(4500))


def findClosestValueInBst(tree, target):

    distances = {}

    while tree != None:

        if tree.value == target:
            print("Found the target: ", tree.value)
            return target
        else:
            distances[tree.value] = abs(target - tree.value)

        if target < tree.value and tree.left != None:
            tree = tree.left
        elif target >= tree.value and tree.right != None:
            tree = tree.right
        else:
            break

    print("Didn't find the target, finding closest value...")

    smallestDistance = distances[tree.value]
    closestValue = tree.value

    for value, distance in distances.items():
        if distance < smallestDistance:
            smallestDistance = distance
            closestValue = value

    print("Closest value: ", closestValue)
    return closestValue


findClosestValueInBst(test, 29751)
