colors = ["Black", "Red", "Maroon", "Yellow"]
codes = ["#000000", "#FF0000", "#800000","#FFFF00"]

output=[]
for i in range(len(colors)):
  empty={}
  empty['color_name']=colors[i]
  empty['color_code']=codes[i]
  output.append(empty)
print(output)