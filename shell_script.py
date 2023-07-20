# from shop.models import Product
# from shop.models import Collection
# import pandas as pd

# coll = Collection.objects.all()

# D = pd.read_csv("running_table.csv")
# x = "Diamond Wire"
# c = None
# for i in coll:
#     if i.name == x:
#         c = i

# objects = []

# # print(D.shape[0])
# # exit(0)

# for i in range(D.shape[0]):

#     p = Product(
#         collection=c,
#         attributesName1=D.columns[0],
#         attributes1=D.loc[i, D.columns[0]],
#         name=D.loc[i, D.columns[0]],
#         attributesName2=D.columns[1],
#         attributes2=D.loc[i, D.columns[1]],
#         attributesName3=D.columns[2],
#         attributes3=D.loc[i, D.columns[2]],
#         attributesName4=D.columns[3],
#         attributes4=D.loc[i, D.columns[3]],
#         attributesName5=D.columns[4],
#         attributes5=D.loc[i, D.columns[4]],
#         attributesName6=D.columns[5],
#         attributes6=D.loc[i, D.columns[5]],
#         attributesName7=D.columns[6],
#         attributes7=D.loc[i, D.columns[6]],
#     )

#     objects.append(p)


# print(objects)
# Product.objects.bulk_create(objects)


from shop.models import Product


objs = Product.objects.all()


for obj in objs:
    obj.save()