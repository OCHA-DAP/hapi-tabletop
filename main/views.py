import csv
from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from main.models import indicator
from scripts import longToWide, transform

# Create your views here.


def index(request):
    return HttpResponse("index")


def transformload(request, indicatorName):
    dbObj = transform.transform(indicatorName)
    indicator.objects.all().filter(Indicator=indicatorName).delete()
    for row in dbObj:
        indicatorObj = indicator(**row)
        indicatorObj.save()

    return JsonResponse({"success": True}, safe=False)


def update(request):
    return render(request, "list.html")


def api(request, indicatorName):
    dbObj = indicator.objects.filter(Indicator=indicatorName)
    iso3 = request.GET.get("iso3", None)
    if iso3 is not None:
        dbObj = dbObj.filter(Admin0_Code_ISO3=iso3)

    # Filter dates
    start_date = request.GET.get("start_date", None)
    if start_date is not None:
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        dbObj = dbObj.filter(Date__gte=start_date)

    end_date = request.GET.get("end_date", None)
    if end_date is not None:
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        dbObj = dbObj.filter(Date__gte=end_date)

    shape = request.GET.get("shape", None)
    if shape == "wide":
        dbObj = dbObj.order_by("Record_ID").order_by("Admin0_Code_ISO3")
        dbObjValues = list(dbObj.values())
        dbObjValues = longToWide.longToWide(dbObjValues)
    else:
        dbObjValues = list(dbObj.values())

    outputFormat = request.GET.get("format", None)
    if outputFormat == "csv":
        response = HttpResponse(
            content_type="text/csv",
            headers={"Content-Disposition": 'attachment; filename="hapi.csv"'},
        )

        cw = csv.DictWriter(
            response,
            dbObjValues[0].keys(),
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL,
        )
        cw.writeheader()
        cw.writerows(dbObjValues)

        return response

    return JsonResponse(dbObjValues, safe=False)
