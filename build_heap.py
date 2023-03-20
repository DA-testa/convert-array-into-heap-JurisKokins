def min_heapify(array, i):
    l = 2 * i + 1
    r = 2 * i + 2
    smallest = i
    swaps = []

    if l < len(array) and array[l] < array[smallest]:
        smallest = l
    if r < len(array) and array[r] < array[smallest]:
        smallest = r

    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        swaps.append((i, smallest))
        swaps += min_heapify(array, smallest)

    return swaps

def build_heap(data):
    last_non_leaf_node = (len(data) // 2) - 1
    swaps = []
    for i in range(last_non_leaf_node, -1, -1):
        swaps += min_heapify(data, i)

    return swaps


def main():
    swaps = []
    text = input()
    if text == "I":
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)
    elif text == "F":
        with open(input()) as file:
            file.readline()
            swaps = build_heap(list(map(int,file.readline().split())))

    print(len(swaps))
    for i, j in swaps:
        print(i, j,end=' ')


if __name__ == "__main__":
    main()
