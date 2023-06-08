import csv

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
        print(iso3)
        dbObj = dbObj.filter(Admin0_Code_ISO3=iso3)

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
