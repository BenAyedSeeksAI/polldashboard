from django.shortcuts import render
from .models import poll,choice
from .forms import pollForm

# Create your views here.
def show_poll(request):
    file ='poll/pollchecker.html'
    poll_data = poll.objects.all()
    choice_data = choice.objects.all()
    register = {}
    for element in poll_data:
        register[element.question] = choice_data.filter(poll_id=element.id)
    context = {
        'register': register,
    }
    return render(request, file, context)

def add_poll(request):
    form = pollForm()
    context = {'form': form}
    if request.method == 'POST':
        form = pollForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'poll/addpoll.html', context)
