import csv
import os


class TaskApp:
    def __init__(self):
        self.file_name = "tasks.csv"

        # Keyword groups used for lightweight priority classification.
        self.high_keywords = {
            "fix",
            "bug",
            "submit",
            "report",
            "urgent",
            "meeting",
            "pay",
            "fees",
            "today",
            "deadline",
            "asap",
        }
        self.medium_keywords = {
            "read",
            "book",
            "prepare",
            "slides",
            "buy",
            "groceries",
            "study",
            "practice",
        }
        self.low_keywords = {
            "watch",
            "movie",
            "scroll",
            "instagram",
            "play",
            "games",
            "rest",
            "relax",
        }

        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.tasks = [row for row in reader]
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.file_name, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["task", "priority"])
            writer.writeheader()
            writer.writerows(self.tasks)

    def predict_priority(self, task):
        words = set(task.lower().split())

        high_score = len(words & self.high_keywords)
        medium_score = len(words & self.medium_keywords)
        low_score = len(words & self.low_keywords)

        scores = {"High": high_score, "Medium": medium_score, "Low": low_score}
        priority = max(scores, key=scores.get)

        # Fallback when no keyword matched.
        if scores[priority] == 0:
            priority = "Medium"

        return priority, scores

    def add_task(self, task):
        print("\n[STEP 1] Task Entered:", task)

        priority, scores = self.predict_priority(task)

        print("\n[STEP 2] Priority Probabilities:")
        total = sum(scores.values())
        for level in ["High", "Medium", "Low"]:
            if total == 0:
                probability = 1 / 3
            else:
                probability = scores[level] / total
            print(f"{level}: {probability:.4f}")

        print("\n[STEP 3] Final Priority:", priority)

        # Save task
        self.tasks.append({"task": task, "priority": priority})
        self.save_tasks()

        print("[OK] Task Added Successfully!")

    def list_tasks(self):
        if not self.tasks:
            print("\n[!] No tasks found.")
        else:
            print("\n--- TASK LIST ---")
            for idx, row in enumerate(self.tasks):
                print(f"{idx}: {row['task']}  [{row['priority']}]")

    def remove_task(self, index):
        if not self.tasks:
            print("\n[!] No tasks to remove.")
            return

        if index < 0 or index >= len(self.tasks):
            print("\n[X] Invalid index.")
            return

        self.tasks.pop(index)
        self.save_tasks()
        print("[OK] Task removed successfully.")


# Menu system
def menu():
    app = TaskApp()

    while True:
        print("\n========================")
        print(" TASK MANAGEMENT SYSTEM ")
        print("========================")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter task: ")
            app.add_task(task)

        elif choice == "2":
            app.list_tasks()
            try:
                idx = int(input("Enter index to remove: "))
                app.remove_task(idx)
            except Exception:
                print("[X] Enter valid number")

        elif choice == "3":
            app.list_tasks()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("[X] Invalid choice")


if __name__ == "__main__":
    menu()