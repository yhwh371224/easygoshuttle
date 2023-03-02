from django.urls import path
from . import views
from .views import server_error
from basecamp.area import suburbs

app_name = "basecamp"

handler500 = server_error

urlpatterns = [
    path('', views.index),
    path('home/', views.home, name='home'),
    path('about_us/', views.about_us),
    path('sitemap/', views.sitemap),
    path('information/', views.information),    
    path('service/', views.service),
    path('terms/', views.terms),
    path('privacy/', views.privacy),
    path('price_detail/', views.price_detail, name='price_detail'),
    path('inquiry/', views.inquiry, name="inquiry"),
    path('inquiry1/', views.inquiry1, name="inquiry1"),
    path('inquiry3/', views.inquiry3, name="inquiry3"),
    path('inquiry_details/', views.inquiry_details),
    path('inquiry_details1/', views.inquiry_details1),    
    path('p2p_single/', views.p2p_single),
    path('p2p/', views.p2p, name="p2p"),
    path('booking/', views.booking, name="booking"),
    path('booking_detail/', views.booking_detail, name="booking_detail"),
    path('booking_form/', views.booking_form, name="booking_form"),
    path('confirmation/', views.confirmation, name="confirmation"),
    path('booking_form_detail/', views.booking_form_detail, name='booking_form_detail'), 
    path('confirm_booking/', views.confirm_booking, name="confirm_booking"),
    path('confirm_booking_detail/', views.confirm_booking_detail, name='confirm_booking_detail'), 
    path('confirmation_detail/', views.confirmation_detail, name='confirmation_detail'),   
    path('payonline/', views.payonline, name='payonline'),
    path('meeting_point/', views.meeting_point),
    path('retrieve_inquiry/', views.retrieve_inquiry, name="retrieve_inquiry"),
    path('retrieve_inquiry_detail/', views.retrieve_inquiry_detail),
    path('retrieve_post/', views.retrieve_post, name="retrieve_post"),
    path('retrieve_post_detail/', views.retrieve_post_detail),
    path('retrieve_inquiry_to_inquiry/', views.retrieve_inquiry_to_inquiry, name='retrieve_inquiry_to_inquiry'),
    path('retrieve_inquiry_to_inquiry_detail/', views.retrieve_inquiry_To_inquiry_detail),
    path('return_trip/', views.return_trip, name="return_trip"),
    path('return_trip_detail/', views.return_trip_detail),
    path('re_confirm/', views.re_confirm, name="re_confirm"),
    path('re_confirm_detail/', views.re_confirm_detail),
    path('re_confirm_email/', views.re_confirm_email, name="re_confirm_email"),
    path('re_confirm_email_detail/', views.re_confirm_email_detail),
    path('save_data_only/', views.save_data_only, name="save_data_only"),
    path('save_data_only_detail/', views.save_data_only_detail),
    path('airport-transfer-sydney-city/', views.sydney_city),
    path('airport-transfers-blacktown/', views.blacktown),
    path('airport-transfers-epping/', views.epping),
    path('airport-transfers-hornsby/', views.hornsby),
    path('airport-transfers-north-shore/', views.north_shore),
    path('airport-transfers-north-west/', views.north_west),
    path('airport-transfers-parramatta/', views.parramatta),
    path('airport-transfers-ryde/', views.ryde),
    path('airport-transfers-st-ives/', views.st_ives),
    path('airport-transfers-thornleigh/', views.thornleigh),
    path('airport-transfers-toongabbie/', views.toongabbie),
    path('airport-transfers-chatswood/', views.chatswood),
    path('airport-transfers-westleigh/', views.westleigh),
    path('airport-transfers-pennant-hills/', views.pennant_hills),
    path('airport-transfers-normanhurst/', views.normanhurst),
    path('airport-transfers-wahroonga/', views.wahroonga),
    path('airport-transfers-asquith/', views.asquith),
    path('airport-transfers-turramurra/', views.turramurra),
    path('airport-transfers-waitara/', views.waitara),
    path('airport-transfers-pymble/', views.pymble),
    path('airport-transfers-gordon/', views.gordon),
    path('airport-transfers-killara/', views.killara),
    path('airport-transfers-mount-kuring-gai/', views.mount_kuring_gai),
    path('airport-transfers-warrawee/', views.warrawee),
    path('airport-transfers-lane-cove/', views.lane_cove),
    path('airport-transfers-middle-cove/', views.middle_cove),
    path('airport-transfers-linfield/', views.linfield),
    path('airport-transfers-west-pymble/', views.west_pymble),
    path('airport-transfers-doonside/', views.doonside),
    path('airport-transfers-marsfield/', views.marsfield),
    path('airport-transfers-eastwood/', views.eastwood),
    path('airport-transfers-macquarie-park/', views.macquarie_park),
    path('airport-transfers-mini-bus/', views.mini_bus),
    path('airport-transfers-willoughby/', views.willoughby),
]