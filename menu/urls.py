from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.cupcake_list,name="cupcake_list"),
	url(r'^cupcake/(?P<pk>\d+)/$',views.cupcake_detail,name="cupcake_detail"),
	url(r'^cupcake/new/$',views.cupcake_new,name='cupcake_new'),
	url(r'^cupcake/price/hightolow',views.cupcake_orderby_price_descending,name='cupcake_orderby_price_descending'),
	url(r'^cupcake/price/lowtohigh',views.cupcake_orderby_price_ascending,name='cupcake_orderby_price_ascending'),
	url(r'^cupcake/rating',views.cupcake_orderby_rating,name='cupcake_orderby_rating'),
	url(r'^minty/testpage',views.minty_testpage,name='minty_testpage')
]