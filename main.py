import os
from time import sleep

# Stolen this funct from https://thispointer.com
def delete_line(original_file, line_number):
    is_skipped = False
    current_index = 0
    dummy_file = original_file + '.bak'
    with open(original_file, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        for line in read_obj:
            if current_index != line_number:
                write_obj.write(line)
            else:
                is_skipped = True
            current_index += 1
    if is_skipped:
        os.remove(original_file)
        os.rename(dummy_file, original_file)
    else:
        os.remove(dummy_file)

print("Welcome, Moura!")
while True:
  sleep(3)
  os.system("clear")
  cmd = input("What are we doing today? >> ")
  os.system("clear")
  if cmd == "help":
   os.system("clear")
   print("view - View your task list")
   print("add - Add a task to your task list")
   print("delete - Delete a task from your task list")
   sleep(4)
  if cmd == "view":
   f = open("tasks.txt","r+")
   try:
     lines = f.readlines()
     os.system("clear")
     for line in lines:
       marker_1 = line.find("[")
       marker_2 = line.find("]")
       it = line[marker_1+2:marker_2-1]
       print(it)
   except Exception:
     os.system("clear")
     print("No tasks!")
  if cmd == "add":
   f = open("tasks.txt","a")
   task = input("Task: ")
   f.write("['" + task + "']" + "\n")
   f.close()
   os.system("clear")
   print("Task added to your list")
  if cmd == "delete":
    f = "tasks.txt"
    liner = int(input("What is the task line? >> "))
    line = liner - 1
    delete_line(f,line)