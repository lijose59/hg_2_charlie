"* HACK-4"
"//eliminar los items 300 y 500"
"[100,200,300,400,500,600,700]  result >  [100,200,400,600,700]"

result = [100,200,300,400,500,600,700]
result.remove(300)
result.remove(500)
print(result)