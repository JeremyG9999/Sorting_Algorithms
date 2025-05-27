class QuickSort:
    @staticmethod
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less = [x for x in arr[1:] if x <= pivot]
            greater = [x for x in arr[1:] if x > pivot]
            print(arr)
            return QuickSort.quick_sort(less) + [pivot] + QuickSort.quick_sort(greater)

    @staticmethod
    def main():
        my_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        sorted_list = QuickSort.quick_sort(my_list)
        print("\nSorted:", sorted_list)
