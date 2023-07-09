count = 0

while count < 5:
    count += 1
    if count == 3:
        continue 
    print("Count:", count)
    if count == 4:
        break
else:
    print("Loop completed successfully")

print("Loop ended")
