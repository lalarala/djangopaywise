from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from polls.models import Question


from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from polls.models import Question, Choice

def ultimas_perguntas(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/perguntas.html', context)

def index(request):
    #return HttpResponse('Olá... seja bem vindo a enquete')
 return render(request, 'home.html')
def sobre(request):
    return HttpResponse('Este é um app de enquete!')

def exibe_questao(request, question_id):
    questao = Question.objects.get(id=question_id)
    return HttpResponse(questao.question_text)
    
#codigo wanderson
def exibe_questao(request, question_id):
    questao = Question.objects.get(id=question_id)
    
    if questao is not None:
        # questao.question_text
        return HttpResponse(questao.question_text)
    
    return HttpResponse('Não existe questão a exibir')


def ultimas_perguntas(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'perguntas_recentes.html', context)

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class QuestionCreateView(CreateView):
    model= Question
    fields= ('question_text', 'pub_date')
    success_url: reverse_lazy('index')

class QuestionCreateView(CreateView):
    model = Question
    template_name = 'polls/question_form.html'
    fields = ('question_text', 'pub_date', )
    success_url = reverse_lazy('polls_list')
    def get_context_data(self, **kwargs):
        context = super(QuestionCreateView, self).get_context_data(**kwargs)
        context['form_title'] = 'Criando uma pergunta'

        return context

class QuestionUpdateView(UpdateView):
        model = Question
        template_name = 'polls/question_form.html'
        fields = ('question_text', 'pub_date', )
        success_url = reverse_lazy('polls_list')
        def get_context_data(self, **kwargs):
            context = super(QuestionUpdateView, self).get_context_data(**kwargs)
            context['form_title'] = 'Editando a pergunta'
            
            return context