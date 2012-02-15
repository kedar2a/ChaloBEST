from mumbai.models import *

#"Road, Area, Landmark, Stop"
def copynames2display_name():
    print "Copying names to display_name field..."
    for obj in Stop.objects.all():
        obj.display_name =obj.name
        obj.save()
    for obj in Area.objects.all():
        obj.display_name =obj.name
        obj.save()
    for obj in Landmark.objects.all():
        obj.display_name =obj.name
        obj.save()
    for obj in Road.objects.all():
        obj.display_name =obj.name
        obj.save()

def copydefaultStopLocations():
    print "Loading default locations for Stop.point field..."
    for stp in Stop.objects.all():
        if stp.stoplocation_set.count()>0 :
            stp.point = stp.stoplocation_set.all()[0].point
            stp.save()
"""
def addStopstoRoutes():
    print "Getting stops linked to Routes..."
    for r in Route.objects.all():
        try:
            r.stop = Stop.objects.get(name=)
"""

def routeWithLocationData(route):
    # get the route detail
    routeDetails = RouteDetail.objects.filter(route_code=route.code).order_by('serial')

    for rd in routeDetails :        
        if rd.stop.point is None:
            return False
        else:
            pass

    return True

def getRoutes_w_loc():
    filteredroutes = []
    for route in Route.objects.all():
        if routeWithLocationData(route):
            filteredroutes.append(route)

    return filteredroutes

