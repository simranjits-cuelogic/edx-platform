from django.conf.urls import url, patterns
from .views import (
    ReferenceListView, ReferenceView, ReferenceEditView, ReferenceDetailView,
    ReferenceDeleteView
    )

urlpatterns = patterns(
    '',
    url(r'references/$', ReferenceListView.as_view(), name='reference_list' ),
    url(r'references/(?P<pk>[0-9]+)/$', ReferenceDetailView.as_view(),
        name='reference'),
    url(r'references/add/$', ReferenceView.as_view(), name='reference_add'),
    url(r'references/(?P<pk>\d+)/edit/$', ReferenceEditView.as_view(),
        name="edit-reference"),
    url(r'references/(?P<pk>[0-9]+)/delete/$', ReferenceDeleteView.as_view(),
        name='delete-reference'),
)
