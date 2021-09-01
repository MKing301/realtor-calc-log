from django.shortcuts import render


def index(request):
    return render(request=request,
                  template_name="commission/index.html"
                )

def calculator(request):
    return render(request=request,
                  template_name="commission/calculator.html"
                )
