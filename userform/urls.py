
from django.urls import path
from . import views

urlpatterns = [
    path('user-form/' , views.user_form_view, name='user_form'),
    path('submitted-forms/' , views.submitted_forms_view, name='submitted_forms'),

]