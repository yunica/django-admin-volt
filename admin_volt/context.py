from django.conf import settings


def contex(request):
    default_context = {
        "volt_sidebar_name": getattr(settings, "VOLT_SIDEBAR_NAME","Volt Overview"),
        "volt_footer_company": getattr(settings, "VOLT_FOOTER_COMPANY","Themesberg"),
        "volt_footer_caption": getattr(settings, "VOLT_FOOTER_CAPTION", "coded by AppSeed.")

    }

    kwargs = {
        "volt_context": default_context,

    }
    return kwargs
