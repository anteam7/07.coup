#from rest_framework import serializers
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from django.shortcuts import render
import json

# 크롤링용 임포트
import requests
from bs4 import BeautifulSoup

# Create your views here.
class CrawlerAPI(APIView):
    def get(self, request):
        result = []

        url = 'https://www.clien.net/service/board/park'
        response = requests.get(url)  
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
    #    list_items = soup.find_all("span", "subject")
    #    list_items = soup.find_all("span", {"data-role":"list-title"})
        list_items = soup.find_all("div", "list_item symph_row")
        
        for item in list_items:
        #    title = item.find("span","subject")["title"]
            title = item.find("span","subject_fixed")["title"]
            hit = item.find("span","hit").text
            timestamp = item.find("span","timestamp").text


            obj = {
                "title" : title, 
                "hit":hit, 
                "timestamp":timestamp
                }

            result.append(obj)

        json_data={"crawled list" : result}
        
        return JsonResponse(json_data, status=200)