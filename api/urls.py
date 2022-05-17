from django.urls import path, include


v1_patterns = [
    path('auth/', include(('auth.urls', 'auth'))),
    path('users/', include(('users.urls', 'users'))),
    path('employee/', include(('employee.urls', 'employee'))),
    
]


urlpatterns = [
    path('v1/', include((v1_patterns, 'v1'))),
]
