from rest_framework.views import APIView
from rest_framework.response import Response
from App.models import Question, Form, Responses, ResponseAnswer, Choices
from App.serializers import QuestionSerializer, FormSerializer, ResponsesSerializer, FormResponsesSerializer
from django.db import transaction

class QuestionAPI(APIView):
    def get(self, request):
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response({
            "status": True,
            "message":"Questions fetched successfully!",
            "data": serializer.data
        })
    
class FormAPI(APIView):
    def get(self, request, pk=None):
        queryset = Form.objects.get(code=pk)
        serializer = FormSerializer(queryset)
        return Response({
            "status": True,
            "message":"Questions fetched successfully!",
            "data": serializer.data
        })
    
class FormResponsesAPI(APIView):
    def get(self, request, pk=None):

        queryset = Form.objects.get(code=pk)
        print(queryset)
        serializer = FormResponsesSerializer(queryset)
        return Response({
            "status": True,
            "message": "Responses Fetch successfully!!!",
            "data": serializer.data
        })


class StoreResponsesAPI(APIView):
    def post(self, request):
        data = request.data
        print("Data: ", data)

        with transaction.atomic():
            if data.get("form_code") is None or data.get("responses") is None:
                return Response({
                    "status": False,
                    "message":"form_code and responses both are required!",
                    "data":{}
                })
            
            responses = data.get("responses")
            print("Response: ", responses)
            response_obj = Responses.objects.create(
                form = Form.objects.get(code = data.get("form_code"))
            )
            print("Response Obj: ", response_obj)

            for response in responses:
                print("Response: ", response)

                question = Question.objects.get(id=response["question_id"])
                for answer in response["answers"]:
                    print("Answer: ", answer)
                    if question.question_type in ["Short Answer", "Long Answer"]:
                        answer_obj = ResponseAnswer.objects.create(
                            answer = answer,
                            answer_to = question
                        )
                    else:
                        answer_obj = ResponseAnswer.objects.create(
                            answer = Choices.objects.get(id=answer),
                            answer_to = question
                        )
                    response_obj.responses.add(answer_obj)
            
            return Response({
                "status": True,
                "message": "Your response has been captured!",
                "data":{}
            })