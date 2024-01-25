from backend_api.views import MovieViewset
from rest_framework.routers import DefaultRouter
from backend_api import views

router = DefaultRouter()
router.register(r'movies',views.MovieViewset,basename='movie')
urlspatterns = router.urls