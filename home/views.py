from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from home.serializers import PeopleSerializer
import logging
logger = logging.getLogger(__name__)

# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    courses = {
        'Python': 'A popular programming language',
        'JavaScript': 'A popular web development language',
        'Django': 'A popular web framework for Python',
        'React': 'A popular JavaScript library for building user interfaces'
    }
    if request.method == 'GET':
        course ={'selected_course': request.GET.get('selected_course','')}
        return Response(course)
    
    elif request.method == 'POST':
        return Response(request.data)
        
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    if request.method == 'GET':
        # objs = Person.objects.all()
        objs = Person.objects.filter(color__isnull=False)
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        logger.debug(f"Received Data: {data}")
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            logger.error(f"Validation Errors: {serializer.errors}")
            return Response(serializer.errors, status=400)
    
    elif request.method == 'PUT':
        data = request.data
        logger.debug(f"Received PUT data: {data}")
    # Fetch the object to update using its primary key (id)
        try:
            person = Person.objects.get(id=data.get('id'))
        except Person.DoesNotExist:
            logger.error(f"Person with id {data.get('id')} does not exist.")
            return Response({"error": "Object not found"}, status=404)
        
        # Pass the existing object to the serializer
        serializer = PeopleSerializer(person, data=data)
        if serializer.is_valid():
            serializer.save()
            logger.debug(f"Updated person data: {serializer.data}")
            return Response(serializer.data)
        else:
            logger.error(f"Validation Errors: {serializer.errors}")
            return Response(serializer.errors, status=400)
    
    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id = data["id"])
        logger.debug(f"received patch data :{data}")
        serializer = PeopleSerializer(obj, data=data, partial = True )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            logger.error(f"validation error : {serializer.errors}")
            return Response(serializer.errors, status = 400)

    else:
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'person deleted'})

