#coding=utf-8
# from django.shortcuts import render
# from django.views.generic.base import View
# from pure_pagination import Paginator,PageNotAnInteger,EmptyPage
# from django.core.cache import cache
# # from django.conf import settings
# from django.views.decorators.cache import cache_page
# from django.http import HttpResponse
from rest_framework import mixins,viewsets
from rest_framework.pagination import PageNumberPagination


from models import ArticleModel,RecommendModel,SentenceModel,LabelModel,NoticeModel,ColumnModel,CommentModel
from .serializers import ArticleSerializer,ColumnSerializer,LabelSerializer,CommentSerializer
# Create your views here.


class ArticlePagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class ArticleListViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticlePagination


class ColumnListViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = ColumnModel.objects.all()
    serializer_class = ColumnSerializer


class LabelListViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = LabelModel.objects.all()
    serializer_class = LabelSerializer


class CommentListViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer


# def get_article():
#     hot_article=cache.get('hot_list')
#     if hot_article is None:
#         hot_article=ArticleModel.objects.all().order_by('-click_nums')[:5]
#         cache.set('hot_list',hot_article)
#         hot_article=cache.get('hot_list',20)
#     return hot_article
#
#
# class IndexView(View):
#     def get(self,request):
#         articles=ArticleModel.objects.all().order_by('-id')
#         recommend=RecommendModel.objects.last()
#         # hot_article=articles.order_by('-click_nums')[:5]
#         sentence=SentenceModel.objects.last()
#         notice=NoticeModel.objects.last()
#         hot_article=get_article()
#
#
#         # hot_article=cache.get('hot_list')
#         # if hot_article is None:
#         #     hot_article=articles.order_by('-click_nums')[:5]
#         #     cache.set('hot_list',hot_article)
#         #     hot_article=cache.get('hot_list')
#
#         try:
#             page=request.GET.get('page','1')
#         except PageNotAnInteger:
#             page=1
#         p=Paginator(articles,5,request=request)
#         article=p.page(page)
#         context={'articles':article,'recommend':recommend,'hot_article':hot_article,'sentence':sentence,'notice':notice}
#         return render(request,'blog/index.html',context)
#
#
# # @cache_page(20)
# def detail(request,article_id):
#     article = ArticleModel.objects.get(id=int(article_id))
#     # article=hot_articles.get(id=int(article_id))
#     taxonomy=LabelModel.objects.get(id=int(article.label.id))#获得分类名称
#     relevant_article=taxonomy.articlemodel_set.all()[:5]#取出分类为taxonomy的所有文章
#     # hot_article=hot_articles[:5]
#     hot_article=get_article()
#     sentence=SentenceModel.objects.last()
#     notice=NoticeModel.objects.last()
#     article_comment=CommentModel.objects.filter(article_id=int(article_id)).order_by('-id')
#     article.click_nums+=1
#     article.save()
#     try:
#         page=request.GET.get('page','1')
#     except PageNotAnInteger:
#         page=1
#     p=Paginator(article_comment,10,request=request)
#     article_comments=p.page(page)
#     context={'article':article,'hot_article':hot_article,'sentence':sentence,'relevant_article':relevant_article,
#              'notice':notice,'article_comment':article_comments}
#     return render(request,'blog/detail.html',context)
#
#
# def recommend(request,recommend_id):
#     recommend=RecommendModel.objects.get(id=int(recommend_id))
#     hot_article=ArticleModel.objects.all().order_by('-click_nums')[:5]
#     sentence=SentenceModel.objects.last()
#     notice=NoticeModel.objects.last()
#     context={'recommend':recommend,'hot_article':hot_article,'sentence':sentence,'notice':notice}
#     return render(request,'blog/recommend.html',context)
#
#
# def list(request,column_id):
#     column=ColumnModel.objects.get(id=int(column_id))
#     articles=column.articlemodel_set.all().order_by('-id')
#     p1=int(column_id)
#     hot_article=ArticleModel.objects.all().order_by('-click_nums')[:5]
#     sentence=SentenceModel.objects.last()
#     notice=NoticeModel.objects.last()
#     try:
#         page=request.GET.get('page','1')
#     except PageNotAnInteger:
#         page=1
#     p=Paginator(articles,1,request=request)
#     article=p.page(page)
#     context={'articles':article,'p':p1,'column':column,'hot_article':hot_article,'sentence':sentence,'notice':notice}
#     return render(request,'blog/list.html',context)
#
#
# def add_comment(request):
#     if not request.user.is_authenticated():
#         return HttpResponse('{"status":"fail","msg":"用户未登录"}',content_type='application/json')
#     article_id=request.POST.get('article_id',0)
#     comment=request.POST.get('comment','')
#     if article_id > 0 and comment:
#         article_comment=CommentModel()
#         article=ArticleModel.objects.get(id=int(article_id))
#         article_comment.article=article
#         article_comment.comment=comment
#         article_comment.user=request.user
#         article_comment.save()
#         return HttpResponse('{"status":"success","msg":"添加成功"}',content_type='application/json')
#     else:
#         return HttpResponse('{"status":"fail","msg":"添加失败"}',content_type='application/json')