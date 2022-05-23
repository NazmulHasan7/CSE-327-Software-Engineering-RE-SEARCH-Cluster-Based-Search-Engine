
from typing import List
from django.contrib.auth import models
from django.core import paginator
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_filters.views import FilterView
from django.urls import reverse_lazy
from .forms import UrlForm
from .models import Cluster, Url
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# To create page restrictions
from django.contrib.auth.mixins import LoginRequiredMixin
# Elastic Search
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from base_app.es_paginator import SearchResults
from base_app.export import link
import requests
from bs4 import BeautifulSoup
# A list view of clusters
class ClusterList(LoginRequiredMixin, FilterView):
    model = Cluster
    context_object_name = 'clusters'
    template_name = 'base_app/clusterList.html'
    paginate_by = 5

    # Restricts user to view other users data
    def get_queryset(self):
        user = self.request.user
        return Cluster.objects.filter(user=user)
    '''
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['clusters'] = context['clusters'].filter(user=self.request.user)
        return context;'''


# A detailed view of Cluster
class ClusterDetail(LoginRequiredMixin, DetailView):
    model = Cluster
    context_object_name = 'cluster'
    template_name = 'base_app/clusterDetail.html'
    query_pk_and_slug = True


# Cluster creation view
class ClusterCreate(LoginRequiredMixin, CreateView):
    model = Cluster
    fields = ['title', 'description']
    # After successful creation of Cluster, redirects user to Cluster view
    success_url = reverse_lazy('clusters')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ClusterCreate, self).form_valid(form)


# Update an existing cluster
class ClusterUpdate(LoginRequiredMixin, UpdateView):
    model = Cluster
    fields = ['title', 'description']
    success_url = reverse_lazy('clusters')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ClusterUpdate, self).form_valid(form)


# Delete an existing cluster
class ClusterDelete(LoginRequiredMixin, DeleteView):
    model = Cluster
    context_object_name = 'cluster'
    success_url = reverse_lazy('clusters')


# URL
# A list view of urls in a Cluster
class UrlList(FilterView):
    model = Url
    context_object_name = 'urls'
    template_name = 'base_app/url_list.html'
    

# URL creation view
class UrlCreate(CreateView):
    model = Url
    form_class = UrlForm
    # After successful creation of URL, redirects user

    def form_valid(self, form):
        url = form.cleaned_data['cluster_url']
        depth = form.cleaned_data['depth']
        id= form.cleaned_data['cluster']
        # print(url, depth, id )
        # begin_crawl(url, depth, id)
        return super(UrlCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'cluster',
            kwargs={'pk': self.object.cluster.id,
                    'slug': self.object.cluster.slug}
        )

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs['cluster_id'] = self.kwargs.get('pk')
        return kwargs

# Cluster-Search view
class SearchView(LoginRequiredMixin, DetailView):
    model = Cluster
    context_object_name = 'cluster'
    template_name = 'base_app/cluster_search.html'
    query_pk_and_slug = True
    pagination = 10

'''
es = Elasticsearch()
def es_search(**filters):
    result = dict()
    result_set = list()
    search_terms = list()
    for key, value in filters.items():
        search_terms.append({"match": {key: value}})
    print("Search terms: ", search_terms)
    size = es.count(index="2").get("count")
    res = es.search(index="2", size=size, body=json.dumps({"query": {"bool": {"must": search_terms}}}))
    for hit in res["hits"]["hits"]:
        result = {"total": res["hits"]["total"], \
                        "content": hit["_source"]["content"]
                        }
        if "quote" in hit["_source"]:
            result.update({"quote": hit["_source"]["quote"]})
        result_set.append(result)
    #return result_set
    print(result)
'''

def search(request, pk, slug):
    es = Elasticsearch()
    es_client = Elasticsearch(['http://127.0.0.1:9200'])
    print('called search')
    search_text = request.GET.get('qq')
    print('Search text: {}'.format(search_text))
    af = request.GET.get('link')
    print('passed url: {}'.format(af))
    print('cluster id/ ealstic search index: {}'.format(pk))
    s = None
    count = 0
    status = False
    page_obj = None
    print('going to export')
    
    
    try:
        if search_text:
            if af is not None:
                print('going to export')
                link(af)
            s = Search(index=str(pk)).using(es_client).query("match", content=search_text)
            response = s.execute()
            count = 0
            for hit in s:
                count += 1
                print(str(count) + ' - ' + str(hit.currnet_url))
            else:
                
                print('nothing more found')
                #paginate_by = 3
                search_results = SearchResults(s)
                print(search_results)
                '''
                paginator = Paginator(search_results, paginate_by)
                page_number = request.GET.get("page")
                try:
                    page_obj = paginator.page(page_number)
                except PageNotAnInteger:
                    # If page parameter is not an integer, show first page.
                    page_obj = paginator.page(1)
                except EmptyPage:
                    # If page parameter is out of range, show last existing page.
                    page_obj = paginator.page(paginator.num_pages)'''
        else:
            print('No text to search')
                    
    except Exception as e:
        count = 0
        status = True
        print('slug: {}'.format(slug))
        print('Exception caught')
        msg = 'Warning! Cluster is not yet ready for searching'
        return render(request, 'base_app/cluster_search.html', 
                {'cluster':slug, 'warning':msg, 'count':count, 'status':status})
    
    return render(request, 'base_app/cluster_search.html', 
            {'cluster':slug, 'hits':s, 'count':count, 'page_obj':page_obj, "search": search_text})


# payment process
def testpayment(request):
    return render(request, 'donation/testpayment.html')