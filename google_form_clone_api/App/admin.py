from django.contrib import admin
from App.models import Choices, Question, Form, Responses, ResponseAnswer

@admin.register(Choices)
class ChoicesAdmin(admin.ModelAdmin):
    list_display = ["id", "choice"]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "question", "question_type", "required"]

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ["id", "code", "title", "creator", "background_color"]

@admin.register(Responses)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ["id", "code", "form", "responder_email"]

@admin.register(ResponseAnswer)
class ResponseAnswerAdmin(admin.ModelAdmin):
    list_display = ["id","answer", "answer_to"]