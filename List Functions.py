numbers = [6 , 12, 19, 45, 22, 25,]
friends = ["John", "Chase", "Julian", "Jabari", "Omar"]
friends.extend(numbers)
friends.append("Scooter")
friends.insert(1, "Kelly")
friends.remove("Chase")
friends.clear()
friends.pop()
friends.sort()
numbers.sort()
numbers.reverse()
friends2 = friends.copy()
print(friends.index("Kevin"))