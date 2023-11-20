a = input("enter the elements ")
b = [c.strip() for c in a.split(" ")]
if a:
  print("First element", repr(b[0]),"Last element",repr(b[-1]))
else:
   print("no element")