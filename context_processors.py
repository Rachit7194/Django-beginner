from SVX.settings import SITE_NAME


def common_details(request):
    return {
        "SITE_NAME" : SITE_NAME
    }