from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import MemberForm

# Create your views here.
def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def list_view(request):
  context = {}
  members = Member.objects.all()
  form = MemberForm()

  if request.method == "POST":
    form = MemberForm(request.POST or None, request.FILES or None)
    if form.is_valid():
      form.save()
      return redirect('members:list_view')

  context['form'] = form
  context['members'] = members
  return render(request, 'members/list_view.html', context)

def detail_view(request, id):
  context = {}
  member = Member.objects.get(id=id)
  form = MemberForm(instance=member)

  if request.method == "POST":
    form = MemberForm(request.POST or None, request.FILES or None, instance=member)
    print("\npost\n", form)
    if form.is_valid():
      form.save()
      return redirect('members:detail_view', id=id)

  if request.method == "GET":
    print("\nget\n")
    context['form'] = form
    context['member'] = member
  
    return render(request, 'members/detail_view.html', context)

def delete_view(request, id):
  member = Member.objects.get(id=id)
  member.delete()
  return redirect('members:list_view')
  
