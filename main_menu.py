import os
import time
from scripts.quick_sort import QuickSort
from scripts.merge_sort import MergeSort
from scripts.insertion_sort import InsertionSort
from scripts.selection_sort import SelectionSort
from scripts.shell_sort import ShellSort
from scripts.bubble_sort import BubbleSort

class Menu:
    def main_menu(self):
        while True:
            print("\nSelect a sorting algorithm:")
            print("1. Quick Sort")
            print("2. Merge Sort")
            print("3. Insertion Sort")
            print("4. Selection Sort")
            print("5. Shell Sort")
            print("6. Bubble Sort")
            print("7. Clear Terminal")
            print("8. Exit")
            option = input("Enter your choice: ")
            if option == "1":
                self.cls()
                QuickSort.main()
            elif option == "2":
                self.cls()
                MergeSort.main()
            elif option == "3":
                self.cls()
                InsertionSort.main()
            elif option == "4":
                self.cls()
                SelectionSort.main()
            elif option == "5":
                self.cls()
                ShellSort.main()
            elif option == "6":
                self.cls()
                BubbleSort.main()
            elif option == "7":
                self.cls()
            elif option == "8":
                break
            else:
                print("Invalid choice.")

    def cls(self):
        time.sleep(0.2)
        os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    Menu().main_menu()
