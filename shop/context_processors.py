from .models import Collection, Category

def get_collections(request):

    constructions_ = Collection.objects.filter(category__name__contains="Construction Tools")
    stones_ = Collection.objects.filter(category__name__contains="Stone Tools")

    return {
        "collections_construction" : constructions_,
        "collections_stone" : stones_,
        "collections" : Collection.objects.all(),
    }