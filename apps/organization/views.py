from django.shortcuts import render

from django.views.generic.base import View
from .models import CityDict, CourseOrg


# 课程机构列表功能
class OrgView(View):
    def get(self, request):
        # 查找所有的城市信息
        all_citys = CityDict.objects.all()
        # 查找所有的课程机构信息
        all_orgs = CourseOrg.objects.all()
        # 统计课程机构的数量
        org_nums = all_orgs.count()

        content = {
            "all_citys": all_citys,
            "all_orgs": all_orgs,
            "org_nums": org_nums
        }
        return render(request, "org-list.html", content)
