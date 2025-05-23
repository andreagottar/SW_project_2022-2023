"""
URL configuration for Iqueue project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import django.contrib
from django.urls import path
from IqueueAP.views import InitialLoading, scan_qr, write_review, Scan_product, Purchase_list, QR_print, Edit_product, \
    ProductShow
from IqueueAP.views import registration_view, login_view
from IqueueAP.views import success
from IqueueAP.views import selectRole
from IqueueAP.views import account_view
from IqueueAP.views import ShopOwner_view
from IqueueAP.views import Shop_view
from IqueueAP.views import Product_view
from IqueueAP.views import SuccessProductRegistration
from IqueueAP.views import SuccessShopRegistration
from IqueueAP.views import Customer_view
from IqueueAP.views import Customer_CategorySelection_view
from IqueueAP.views import Booking_view
# from IqueueAP.views import Customer_category_view
from IqueueAP.views import Booking_view
from IqueueAP.views import MyShops_view
from IqueueAP.views import Reservation_view
from IqueueAP.views import ShopQueueList
from IqueueAP.views import Wish_list
from IqueueAP.views import DeleteShop
from IqueueAP.views import DeleteQR
from IqueueAP.views import DeleteAdv
from IqueueAP.views import Advertisement_view
from IqueueAP.views import SuccessAdvertisementRegistration
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('Customer/WriteReview/', write_review, name='Reservation_view'),
    path('', InitialLoading, name='InitialLoading'),
    path('login/', login_view, name='login_View'),
    path('registration/', registration_view, name='registration'),
    path('registration/success/', success, name='success'),
    path('login/SelectRole/', selectRole, name='selectRole'),
    path('account/', account_view, name='account_view'),  # Serve??
    path('ShopOwner/', ShopOwner_view, name='ShopOwner_view'),
    path('ShopOwner/MyShops/', MyShops_view, name='MyShops_view'),
    path('ShopOwner/Scan_product/<str:idc>/', Scan_product, name='Scan_product'),
    path('Customer/Purchase_list/', Purchase_list, name='Purchase_list'),
    path('ShopOwner/MyShops/NewShop/', Shop_view, name='Shop_view'),
    path('ShopOwner/MyShops/NewShop/success/', SuccessShopRegistration, name='SuccessShopRegistration'),
    path('ShopOwner/MyShops/QueueList/<str:ids>/', ShopQueueList, name='ShopQueueList'),
    path('ShopOwner/MyShops/DeleteShop/<str:ids>/', DeleteShop, name='DeleteShop'),
    path('ShopOwner/MyShops/DeleteAdv/<str:ids>/', DeleteAdv, name='DeleteAdv'),
    path('ShopOwner/Product/', Product_view, name='Product_view'),
    path('ShopOwner/Product/success/', SuccessProductRegistration, name='SuccessProductRegistration'),
    path('ShopOwner/Advertisement/', Advertisement_view, name='Advertisement_view'),
    path('ShopOwner/Advertisement/success/<str:ids>/', SuccessAdvertisementRegistration,
         name='SuccessAdvertisementRegistration'),
    path('ShopOwner/Scan/', scan_qr, name='scan'),
    path('Customer/', Customer_view, name='Customer_view'),
    path('Customer/Selection/', Customer_CategorySelection_view, name='Customer_CategorySelection_view'),
    path('Customer/Selection/(?P<selected_category>\s+)/', Booking_view, name='Booking_view'),
    path('Customer/Reservations/', Reservation_view, name='Reservation_view'),
    path('Customer/Reservations/<str:idQR>/', DeleteQR, name='DeleteQR'),
    path("admin/", django.contrib.admin.site.urls),
    path('ShopOwner/QR_print/', QR_print, name='QR_print'),
    path('Customer/WishList/', Wish_list, name='WishList'),
    path('ShopOwner/Product/Edit', Edit_product, name='Edit_Product'),
    path('ShopOwner/Product/Show/', ProductShow, name='ProductShow'),
    # path('Customer/bakery/', booking, name='booking'),
    # path('booking-submit', bookingSubmit, name='bookingSubmit'),
]

# Da commentare e togliere da commento ogni volta che si aggiunge un URL!!
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
