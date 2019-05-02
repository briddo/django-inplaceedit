# -*- coding: utf-8 -*-
# Copyright (c) 2010-2013 by Yaco Sistemas <goinnn@gmail.com>
#               2015 by Pablo Martín <goinnn@gmail.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this programe.  If not, see <http://www.gnu.org/licenses/>.

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

STATUS = (
    ('available', _('Available')),
    ('order', _('Ordered')),
    ('borrow', _('Borrowed')),
)


class TypeResource(models.Model):
    name = models.CharField(verbose_name=_('name'),
                            max_length=100, null=False)

    class Meta:
        verbose_name = _('Type of resource')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Resource(models.Model):
    name = models.CharField(verbose_name=_('Name'),
                            max_length=100, null=False, blank=False,
                            unique=True)
    created = models.DateField(verbose_name=_('Date of created'))
    description = models.TextField(verbose_name=_('Description'),
                                   blank=True, null=True)
    status = models.CharField(verbose_name=_('Status'),
                              max_length=20, choices=STATUS,
                              default='order', help_text='Status of the resource.',
                              editable=True, null=False, blank=False)
    resource_type = models.ForeignKey(TypeResource, verbose_name=_('Type'),
                                      null=False, blank=False, editable=True)
    owner = models.ManyToManyField(User, verbose_name=_('Owner'))
    amount = models.IntegerField(verbose_name=_('Amount'), null=True, blank=True)
    can_borrow = models.BooleanField(verbose_name=_('Can borrow?'))
    available_from = models.DateTimeField(verbose_name=_("Will be available from"))
    image = models.ImageField(verbose_name=_("Associated Image"), null=True, blank=True, upload_to="images")
    file = models.FileField(verbose_name=_("File Text"), null=True, blank=True, upload_to="files")

    class Meta:
        verbose_name = _('Resources')

    @models.permalink
    def get_absolute_url(self):
        return ('multimediaresources_edit', (self.pk,))

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
