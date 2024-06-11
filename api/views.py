from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .serializer import ItemSerializer
from base.models import Item


@api_view(['GET','POST','PUT','DELETE'])
def getData(request):
    if request.method == 'GET':
         items=Item.objects.all()
         serializer=ItemSerializer(items, many=True)
         return Response(serializer.data)
         
    elif request.method=='POST':
         serializer=ItemSerializer(data = request.data)
         if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)

    elif request.method=='PUT':
        data = request.data
        obj = Item.objects.get(id=data['id'])
        serializer=ItemSerializer(obj, data = data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    else:
            data = request.data
            obj = Item.objects.get(id=data['id'])
            obj.delete()
            return Response({'message':'Item Deleted'})