from django.shortcuts import HttpResponse
from . import models

def authors(request):
    authors = models.Author.objects.all()
    respons = "<h1>Authors</h1>"
    count = 1
    for i in authors:
        respons += f"""
                <ul>
                    <li><a href='author/{count}'>{i.first_name} {i.last_name}</a></li>
                </ul>
        """
        count += 1
    respons += "<a href='/'>Kitoblar</a>"
    return HttpResponse(respons)

def main(request):
    books = models.Book.objects.all()
    respons = "<h1>Kitoblar</h1>"
    count = 1
    for book in books:
        respons += f"""
            <ul>
                <li><a href='book/{count}'>{book.title}</a></li>
            </ul>
        """
        count += 1
    respons += "<a href='authors/'>Authors</a>"
    return HttpResponse(respons)

def book_1(request):
    books = models.Book.objects.get(title="Kichkina shahzoda")
    respons = f"""
             <h1>{books.title}</h1>
             <h3>Author: <a href='/book/authors/author/1'>{books.author}</a></h3>
             <h3>Publication date: {books.publication_date}</h3>
             <h3>Category: {books.category}</h3>
             <p>{books.description}</p>
             <a href='../', 'book/authors'>Back</a>
        """
    return HttpResponse(respons)


def book_2(request):
    books = models.Book.objects.get(title="Harry Potter")
    respons = f"""
         <h1>{books.title}</h1>
         <h3>Author: <a href='/book/authors/author/2'>{books.author}</a></h3>
         <h3>Publication date: {books.publication_date}</h3>
         <h3>Category: {books.category}</h3>
         <p>{books.description}</p>
         <a href='../'>Back</a>
    """
    return HttpResponse(respons)

def author_1(request):
    authors = models.Author.objects.get(first_name="Antoine Marie Jean-Baptiste Roger")
    respons = f"""
      <h1>{authors.first_name} {authors.last_name}</h1>
      <p>{authors.bio}</p>
      <a href='../'>Back</a>
    """
    return HttpResponse(respons)


def author_2(request):
    authors = models.Author.objects.get(first_name="Joanna Kathleen")
    respons = f"""
      <h1>{authors.first_name} {authors.last_name}</h1>
      <p>{authors.bio}</p>
      <a href='../'>Back</a>
    """
    return HttpResponse(respons)




