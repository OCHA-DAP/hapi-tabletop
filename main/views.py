import csv
import logging
from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from main.models import Indicator, MetaData
from scripts import get_indicator, get_metadata, longToWide

# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("index")


def transformload(request, indicator_name):
    logger.info("Getting metadata")
    metadata_data = get_metadata.transform(indicator_name)
    MetaData.objects.all().filter(indicator_name=indicator_name).delete()
    for row in metadata_data:
        metadata_obj = MetaData(**row)
        metadata_obj.save()

    logger.info("Getting indicator data")
    indicator_data = get_indicator.transform(indicator_name)
    Indicator.objects.all().filter(indicator_name=indicator_name).delete()
    for row in indicator_data:
        indicator_obj = Indicator(**row)
        indicator_obj.save()

    logger.info("Success")
    return JsonResponse({"success": True}, safe=False)


def update(request):
    return render(request, "list.html")


def api(request, indicator_name):
    dbObj = Indicator.objects.filter(indicator_name=indicator_name)
    iso3 = request.GET.get("iso3", None)
    if iso3 is not None:
        dbObj = dbObj.filter(admin0_code_iso3=iso3)

    # Filter dates
    start_date = request.GET.get("start_date", None)
    if start_date is not None:
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        dbObj = dbObj.filter(date__gte=start_date)

    end_date = request.GET.get("end_date", None)
    if end_date is not None:
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        dbObj = dbObj.filter(date__lte=end_date)

    shape = request.GET.get("shape", None)
    if shape == "wide":
        dbObj = dbObj.order_by("record_id").order_by("admin0_code_iso3")
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
