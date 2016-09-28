#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from SALT.views import key_list, execute

urlpatterns = patterns('',
        #salt_key
        url(r'^key_list/$', key_list),
        url(r'^execute/$', execute),
    )
