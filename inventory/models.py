from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Section(models.Model):
    name = models.CharField(_('section_name'),max_length=30,unique=True)
    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')

    def __unicode__(self):
        return self.name
class Room(models.Model):
    name = models.CharField(_('room_name'),max_length=30,unique=True)
    section = models.ForeignKey(Section,related_name="rooms",verbose_name=_('room_section'))
    class Meta:
        verbose_name = _('Room')
        verbose_name_plural = _('Rooms')

    def __unicode__(self):
        return self.name
class Item(models.Model):
    section = models.ForeignKey(Room,related_name="items",verbose_name=_('item_room'))
    item_number = models.CharField(_('item_number'),max_length=20,unique=True)
    name = models.CharField(_('item_name'),max_length=60)
    unit = models.CharField(_('item_unit'),max_length=40)
    count = models.IntegerField(verbose_name=_('item_count'),validators=[MinValueValidator(0)])
    comment = models.CharField(_('comment'),max_length=20)
    class Meta:
        verbose_name = _('Item')
        verbose_name_plural = _('Items')
    def __unicode__(self):
        return self.item_number

