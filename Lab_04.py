class Process:
    def __init__(self, id, name, time, priority):
        self.id = id
        self.name = name
        self.time = time
        self.priority = priority

class Table:
    def __init__(self):
        self.processes = []

    def add(self, process):
        self.processes.append(process)

    def sort_id(self):
        self._sort("id")

    def sort_time(self):
        self._sort("time")

    def sort_priority(self):
        priority_order = {"Low": 0, "MID": 1, "High": 2}
        self.processes.sort(key=lambda process: priority_order[process.priority])

    def _sort(self, attr):
        sorted_processes = []
        while self.processes:
            min_process = self.processes[0]
            for process in self.processes:
                if getattr(process, attr) < getattr(min_process, attr):
                    min_process = process
            sorted_processes.append(min_process)
            self.processes.remove(min_process)
        self.processes = sorted_processes

    def display(self):
        for process in self.processes:
            print(f'P_ID: {process.id}, Process: {process.name}, Start Time: {process.time}, Priority: {process.priority}')

if __name__ == "__main__":
    tbl = Table()

    tbl.add(Process("P1", "VSCode", 100, "MID"))
    tbl.add(Process("P23", "Eclipse", 234, "MID"))
    tbl.add(Process("P93", "Chrome", 189, "High"))
    tbl.add(Process("P42", "JDK", 9, "High"))
    tbl.add(Process("P9", "CMD", 7, "High"))
    tbl.add(Process("P87", "NotePad", 23, "Low"))

    print("Sorting Options:")
    print("1. Sort by P_ID")
    print("2. Sort by Start Time")
    print("3. Sort by Priority")

    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        tbl.sort_id()
    elif choice == 2:
        tbl.sort_time()
    elif choice == 3:
        tbl.sort_priority()
    else:
        print("Invalid choice")

    print("\nSorted Flight Table:")
    tbl.display()
