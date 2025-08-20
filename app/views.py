from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.parsers import FormParser, MultiPartParser

from .serializers import serialize
from .models import database

# Create your views here.

#post
class photoupload(APIView):
    parser_classes=[FormParser,MultiPartParser]
    def post(self,req):
        serial=serialize(data=req.data)
        if serial.is_valid():
            serial.save()
            metadata={'file_name':serial.instance.name, 'file_size': f"{round(serial.instance.url.size/1024,2)} KB", 'upload_Time':serial.instance.uploaded_At }
        return Response(metadata)
#get    
class photo(APIView):
    def get(self,req):
        data=database.objects.all()
        serialdata=serialize(data, many=True)
        return Response(serialdata.data)   


# getting the path of base directory
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent 

#delete
class delete(APIView):
    def delete(self,req):
        obj=database.objects.get(id=req.data['id'])
        os.remove(os.path.join(BASE_DIR, 'media',str(obj.url)))
        obj.delete()
        return Response({'messege':'image deletede'})  
       