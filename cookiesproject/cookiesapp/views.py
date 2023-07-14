from django.shortcuts import render


# Create your views here.
# def cookies_count_view(request):
#     count = request.COOKIES.get('count', 0)
#     total_count = int(count) + 1
#     my_dict = {'count': total_count}
#     response = render(request, 'cookies.html', context=my_dict)
#     response.set_cookie('count', total_count)
#     return response
def session_api(request):
    count = request.session.get('count',0)
    total_count = int(count) + 1
    request.session['count'] = total_count
    print(request.session.get_expiry_date())
    return render(request, 'cookies.html',{'count':total_count})