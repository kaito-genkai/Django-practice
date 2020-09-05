from django.urls import path
from .views import ItemFilterView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView


urlpatterns = [
    # 一覧
    path("", ItemFilterView.as_view(), name="index"),
    # 詳細
    path("detail/<int:pk>/", ItemDetailView.as_view(), name="detail"),
    # 登録
    path("create/", ItemCreateView.as_view(), name="create"),
    # 更新
    path("update/<int:pk>/", ItemUpdateView.as_view(), name="update"),
    # 削除
    path("delete/<int:pk>/", ItemDeleteView.as_view(), name="delete"),
]
