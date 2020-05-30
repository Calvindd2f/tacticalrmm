from django.urls import path
from . import views

urlpatterns = [
    path("checks/", views.GetAddCheck.as_view()),
    path("<int:pk>/check/", views.GetUpdateDeleteCheck.as_view()),
    path("<pk>/loadchecks/", views.load_checks),
    path("<pk>/loadpolicychecks/", views.load_policy_checks),
    path("checkrunner/", views.check_runner),
    path("getstandardcheck/<checktype>/<pk>/", views.get_standard_check),
    path("editstandardcheck/", views.edit_standard_check),
    path("deletestandardcheck/", views.delete_standard_check),
    path("getdisks/<pk>/", views.get_disks),
    path("getalldisks/", views.get_disks_for_policies),
    path("runchecks/<pk>/", views.run_checks),
    path("checkresults/", views.check_results),
]
