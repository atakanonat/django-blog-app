from .forms import ArticleForm
from .models import Article, Comment
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def articles(request):
    keyword = request.GET.get('keyword')

    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, 'articles.html', {'articles': articles})

    articles = Article.objects.all().order_by('created_date').reverse()

    return render(request, 'articles.html', {'articles': articles})


@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author=request.user)

    if articles.count() != 0:
        return render(request, "dashboard.html", {"articles": articles})
    messages.info(request, "You have not any articles yet.")
    return render(request, "dashboard.html")


@login_required(login_url="user:login")
def createArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        # Add author information to form before committing to database.
        article = form.save(commit=False)
        article.author = request.user
        if request.FILES:
            article.article_img = request.FILES["article_img"]

        article.save()
        print(article.id)
        messages.success(request, "Article created successfully!")
        return redirect(reverse('article:details', kwargs={'id': article.id}))

    return render(request, "createArticle.html", {"form": form})


def details(request, id):
    # article = Article.objects.get(id=id)
    article = get_object_or_404(Article, id=id)

    # We can reach comments like this because we assigned related_name value as comments in model.py
    comments = article.comments.all()
    return render(request, "details.html", {"article": article, "comments": comments})


@login_required(login_url="user:login")
def editArticle(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None,
                       request.FILES or None, instance=article)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user

        article.save()

        messages.success(request, "Article updated successfully!")
        return redirect(reverse('article:details', kwargs={'id': id}))

    return render(request, "editArticle.html", {"form": form})


@login_required(login_url="user:login")
def deleteArticle(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    messages.success(request, "Article deleted.")

    return redirect("article:dashboard")


def addComment(request, id):
    article = get_object_or_404(Article, id=id)

    if request.method == 'POST':
        comment_author = request.user.username
        comment_content = request.POST.get('comment_content')

        newComment = Comment(comment_author=comment_author,
                             comment_content=comment_content, article=article)

        newComment.save()

    return redirect(reverse('article:details', kwargs={'id': id}))
