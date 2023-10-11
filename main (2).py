def linearsearchProduct(ProductList,targetProduct):
 indices =[]
 for index, product in enumerate(ProductList):
   if product==targetProduct:
      indices.append(index)
 return indices

#example usage
Products= ["shoes","boot","loafer","shoes","sandal","shoes"]
target = "shoes"
target2 = "apple"
result = linearsearchProduct(Products, target)
print(result)
