temperatura= int(input("informe a temperatura atual"))
if temperatura <=15:
 print("frio")
elif temperatura >=15 and temperatura <= 25:
  print("agradavel")
elif temperatura >=26 and temperatura <= 35:
  print("quente")
else:
  print("muito quente")