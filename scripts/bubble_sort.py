class BubbleSort:
    @staticmethod
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    print(arr)
        return arr

    @staticmethod
    def main():
        my_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        BubbleSort.bubble_sort(my_list)
        print("\nSorted:", my_list)