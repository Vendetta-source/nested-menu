from django.db import models


class ItemMenu(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Название')
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True,
                               verbose_name='Родитель')
    menu_name = models.CharField(max_length=100,
                                 verbose_name='Название меню',
                                 blank=True,
                                 null=True)

    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'

    def children(self):
        return self.itemmenu_set.all()

    def get_elder_ids(self):
        if self.parent:
            return self.parent.get_elder_ids() + [self.parent.pk]
        else:
            return []

    def __str__(self):
        return self.title
