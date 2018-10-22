from django.shortcuts import render

from django.views.generic.base import View


# 课程机构列表功能
class OrgView(View):
    def get(self, request):
        return render(request, "org-list.html", {})
