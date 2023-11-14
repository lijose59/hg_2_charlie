"* HACK-10"
"agregar después del item 500"
"los alias qux y thud"
"[100,200,300,400,500,600,700]  result >  [100,200,300,400,500,qux,thud,600,700]"

result = [100,200,300,400,500,600,700]
alias1 = ["qux"]
alias2 = ["thud"]
result =  result[:5] + alias1 + alias2 + result[5:]
print (result)