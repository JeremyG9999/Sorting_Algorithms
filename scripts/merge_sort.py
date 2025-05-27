class MergeSort:
    @staticmethod
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]
            MergeSort.merge_sort(left_half)
            MergeSort.merge_sort(right_half)
            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1
            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1
            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
        print(arr)

    @staticmethod
    def main():
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        MergeSort.merge_sort(arr)
        print("\nSorted:", arr)
