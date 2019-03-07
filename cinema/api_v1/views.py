from django.views.decorators.csrf import csrf_exempt
from webapp.models import Movie, Category, Hall, Seat, Show, Book, Ticket, Discount
from rest_framework import viewsets
from api_v1.serializers import MovieCreateSerializer, MovieDisplaySerializer, \
    CategorySerializer, HallSerializer, SeatSerializer, ShowSerializer, BookSerializer, TicketSerializer, DiscountSerializer


# Базовый класс ViewSet, основанный на ModelViewSet,
# но с отключенной проверкой аутентификации, и не блокирующий запросы без токена.
class NoAuthModelViewSet(viewsets.ModelViewSet):
    authentication_classes = []


class MovieViewSet(NoAuthModelViewSet):
    queryset = Movie.objects.active().order_by('-release_date')

    # Метод, который отвечает за то,
    # какой класс сериализатора будет использоваться при обработке запроса.
    # Если запрос сделан методом GET, т.е. запрос на просмотр фильма или списка фильмов,
    # то метод возвращает класс MovieDisplaySerializer (вывод фильмов с вложенными категориями),
    # иначе - MovieCreateSerializer (вывод и сохранение фильмов с категориями в виде списка id категорий).
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieDisplaySerializer
        else:
            return MovieCreateSerializer

    # метод, который выполняет удаление объекта instance.
    # здесь он переопределён для "мягкого" удаления объектов -
    # вместо реального удаления объекта, меняется его свойство is_deleted на True.
    # сам фильм сохраняется в базе, но при этом помечается, как удалённый.
    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class CategoryViewSet(NoAuthModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class HallViewSet(NoAuthModelViewSet):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer


class SeatViewSet(NoAuthModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class ShowViewSet(NoAuthModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer


class BookViewSet(NoAuthModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class TicketViewSet(NoAuthModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class DiscountViewSet(NoAuthModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

