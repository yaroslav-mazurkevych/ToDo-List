from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from .models import Task, Tag


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "list/tag_list.html"


class TagDetailView(generic.DetailView):
    modal = Tag
    queryset = Tag.objects.all()


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("list:tag-list")


class TaskListView(generic.ListView):
    model = Task
    template_name = "list/index.html"
    context_object_name = "task_list"
    ordering = ["-is_done", "-created_at"]


class TaskDetailView(generic.DetailView):
    model = Task
    queryset = Task.objects.all()


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "list/task_form.html"
    fields = ["content", "deadline", "tag"]
    success_url = reverse_lazy("list:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "list/task_form.html"
    fields = ["content", "deadline", "tag"]
    success_url = reverse_lazy("list:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "list/task_confirm_delete.html"
    success_url = reverse_lazy("list:index")


def complete_or_undo(request: HttpRequest, pk: int) -> HttpResponse:
    task = Task.objects.get(pk=pk)

    if not task.is_done:
        task.is_done = True

    else:
        task.is_done = False

    task.save()

    return redirect("list:index")
