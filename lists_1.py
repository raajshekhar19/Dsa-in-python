foods  = ["cake","brownie"]

foods.append("tatti")#just like push in js and push_back in cpp
foods.remove("tatti")#removes the mentioned element
foods.pop()#poopsmout /removes the last element in the lisst
foods.insert(0,"pastry")#.insert(index,element)
foods.sort()#sorts the foods list in ascending order
foods.clear()#cleans/deletes the elements of the list
for food in foods:
    print(food)