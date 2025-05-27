class SelectionSort:
    @staticmethod
    def selectionSort(array, size):
        for step in range(size):
            min_idx = step
            for i in range(step + 1, size):
                if array[i] < array[min_idx]:
                    min_idx = i
            print(array)
            (array[step], array[min_idx]) = (array[min_idx], array[step])

    @staticmethod
    def main():
        data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        size = len(data)
        SelectionSort.selectionSort(data, size)
        print(f"\n{data}")
