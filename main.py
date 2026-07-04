tasks = ["Homework", "Pooping", "Cleaning", "Ironing"]

while True:
    new_tasks = input("Enter a task (or type 'exit' to stop): ")

    if new_tasks == "exit":
        break
    tasks.append(new_tasks)

print(tasks)