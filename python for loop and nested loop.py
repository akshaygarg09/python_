for num in range(1, 6):
    if num == 3:
        continue  
    print("Number:", num)
    if num == 4:
        break  
else:
    print("Loop completed successfully")

print("Loop ended")





adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

