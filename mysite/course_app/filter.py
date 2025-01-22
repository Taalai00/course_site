from django_filters.rest_framework import DjangoFilterBackend

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'course', 'rating']  # Поля для фильтрации

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [SearchFilter]
    search_fields = ['comment']  # Поля для поиска

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['rating']  # Поля для сортировки
    ordering = ['-rating']  # Сортировка по умолчанию