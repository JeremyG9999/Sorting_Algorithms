class ShellSort:
    @staticmethod
    def shellSort(array, n):
        interval = n // 2
        while interval > 0:
            for i in range(interval, n):
                temp = array[i]
                j = i
                while j >= interval and array[j - interval] > temp:
                    array[j] = array[j - interval]
                    j -= interval
                array[j] = temp
                print(array)
            interval //= 2

    @staticmethod
    def main():
        data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        size = len(data)
        ShellSort.shellSort(data, size)
        print(f"\n{data}")
