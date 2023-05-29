from django.http import JsonResponse, HttpResponse
from .models import Reminder
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
def index(request):
    reminders = Reminder.objects.all()
    return JsonResponse({"reminders": list(reminders.values())})


# Cross Site Request Forgery
@csrf_exempt
def new_reminder(request):
    try:
        data = json.loads(request.body)
        title = data.get("title")
        description = data.get("description")
        reminder = Reminder.objects.create(title=title, description=description)
        return JsonResponse(reminder.to_json())
    except:
        return JsonResponse({"message": "Something bad happened"}, status=500)

# TODO: Design a DELETE action
@csrf_exempt
def delete_reminder(request, id):
    """
    id - also know as primary key, represents the ID in the reminders_reminder table.
    """
    if request.method == 'DELETE':
        print("To be implemented by student")
        # TODO: Write your code here - it should delete a reminder
    
    
    empty =  []
    for reminder in reminders:
     empty.delete({'id':reminder.id, 'title':reminder.title, 'description': reminder.description })
    print(empty)
    
    
# Do not touch code below
    else:
    return JsonResponse({"message": "This method is not allowed, only DELETE"}, status=500)

#TODO: 2. Math question
def calculate(request):
    # accessing a query parameter is done as follows
    
    query_dictionary = request.GET
    operation = query_dictionary.get('operation', '')
    if operation == '':
        return JsonResponse({'message': 'operation missing'}, status=500)
    a = query_dictionary.get('a', 0)
    b = query_dictionary.get('b', 0)
    # Do not change the code above!
    # TODO: Fill in the blanks below
@api_view(['GET'])
def details(request,id):
    if request.method=='GET':
        order = get_object_or_404(Orders,id=id,applications=application)
        collection = get_object_or_404(Payments,orders=id,direction='COLLECTION',is_active=True) 
        transfer = get_object_or_404(Payments,orders=order,direction='TRANSEFER',is_active=True)
        content =  {
                    'orders': {
                        "id":id,
                        "purpose_code":order.purpose_code,
                        "amount":order.amount,
                        'collection_payments':{
                            "id":collection_payments.id,
                            "amount":collection_payments.amount,
                            "datetime":collection_payments.datetime,
                            'transfer': [
                                     {
                                         "id":transfer.id,
                                         "amount":transfer.amount,
                                        "datetime":transfer.datetime,
                                     }    
                                ]
                            }
                       }
                    }
        return Response(content, status=status.HTTP_200_OK)


