from rest_framework import serializers
from App.models import Question, Form, Choices, ResponseAnswer, Responses

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = ["created_at", "updated_at"]

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        exclude = ["created_at", "updated_at", "creator", "id"]

    def to_representation(self, instance):
        print(instance)
        questions = []
        for question in instance.questions.all():
            # print(question)

            choices = []
            if question.question_type in ["Multiple Choices", "Checkbox"]:
                for choice in question.choices.all():
                    print(choice)
                    choices.append({"id": choice.id, "choice": choice.choice})

            questions.append({
                "question": question.question,
                "question_type": question.question_type,
                "required": question.required,
                "choices": choices
            })

        data = {
            "code": instance.code,
            "title": instance.title,
            "background_color": instance.background_color,
            "questions": questions
        }

        return data
    
class ResponseAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseAnswer
        fields = ["created_at", "updated_at"]

    def to_representation(self, instance):
        data = {
            "answer": instance.answer,
            "answer_to": {
                "question": instance.answer_to.question,
                "question_type": instance.answer_to.question_type
            }
        }
        return data

class ResponsesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responses
        fields = ["created_at", "updated_at"]

    def to_representation(self, instance):
        
        data = {
            "code": instance.code,
            "responder_email": instance.responder_email,
            "answers":ResponseAnswerSerializer(instance.responses.all(), many=True).data
        }

        return data
    
class FormResponsesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ["created_at", "updated_at"]

    def to_representation(self, instance):
        queryset = Responses.objects.filter(form = instance)
        print(queryset)
        data = {
            "code": instance.code,
            "title": instance.title,
            "background_color": instance.background_color,
            "responses": ResponsesSerializer(queryset, many=True).data
        }
        return data