from django.db import models

class MainLeague(models.Model):
    date = models.DateTimeField()  # Дата
    home = models.CharField(max_length=100)  # Команда дома
    away = models.CharField(max_length=100)  # Команда в гостях
    one_o = models.FloatField()  # Котировка 1(o)
    one_e = models.FloatField()  # Котировка 1(e)
    x_o = models.FloatField()  # Котировка X(o)
    x_e = models.FloatField()  # Котировка X(e)
    two_o = models.FloatField()  # Котировка 2(o)
    two_e = models.FloatField()  # Котировка 2(e)
    bts_o = models.FloatField()  # Котировка BTS(o)
    bts_e = models.FloatField()  # Котировка BTS(e)
    bts_no_o = models.FloatField()  # Котировка BTS_no(o)
    bts_no_e = models.FloatField()  # Котировка BTS_no(e)
    over_o = models.FloatField()  # Котировка Over(o)
    over_e = models.FloatField()  # Котировка Over(e)
    under_o = models.FloatField()  # Котировка Under(o)
    under_e = models.FloatField()  # Котировка Under(e)
    first_half = models.CharField(max_length=50, null=True)  # Первый тайм
    match = models.CharField(max_length=50, null=True)  # Матч
    goals = models.CharField(max_length=50, null=True)  # Голы
    league = models.CharField(max_length=50, null=True)  # Лига
    link = models.URLField(max_length=255, null=True)  # Ссылка
    notes = models.TextField(null=True)  # Заметки
    league_id = models.IntegerField(default=0) # id лиги

    class Meta:
        db_table = 'new_main_league'  # Указываем имя существующей таблицы в БД
        managed = False  # Запрещаем Django управлять жизненным циклом таблицы

    def __str__(self):
        return f"{self.home} vs {self.away} on {self.date}"  # Читаемое представление

    