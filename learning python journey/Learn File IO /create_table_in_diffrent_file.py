import os
#Ensure the 'tables' directory exists
tables_dir = "enter you relative path "
os.makedirs(tables_dir, exist_ok=True)

for i in range(2, 21):
    with open(f"{tables_dir}/multiplication_table_of_{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i} X {j} = {i*j}\n")

