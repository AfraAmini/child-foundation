# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import AbstractUser
from system.models import information
from django.utils.translation import ugettext_lazy as _




class active_user(AbstractUser):
    AbstractUser._meta.get_field('username').verbose_name = "نام کاربری"
    AbstractUser._meta.get_field('password').verbose_name = "کلمه عبور"

    first_name = models.CharField(max_length=100, null=True, verbose_name="نام")
    last_name = models.CharField(max_length=100, null=True, verbose_name="نام خانوادگی")
    id_number = models.IntegerField(unique=True, null=False, verbose_name="کد ملی")
    phone_number = models.IntegerField(null=True, verbose_name="شماره تلفن")
    address = models.TextField(null=True, verbose_name="آدرس")

    class Meta:
        verbose_name_plural = _("کاربران فعال")
        verbose_name = _("کاربر فعال")

class madadkar(active_user):
    bio = models.TextField(null=True, verbose_name="شرح حال")

    class Meta:
        verbose_name_plural = _("مددکاران")
        verbose_name = _("مددکار")

class hamyar(active_user):
    class Meta:
        verbose_name_plural = _("همیاران")
        verbose_name = _("همیار")


class madadjoo(active_user):
    bio = models.TextField(null=True, verbose_name="شرح حال")
    edu_status = models.TextField(null=True, verbose_name="وضعیت تحصیلی")
    successes = models.TextField(null=True, verbose_name="شرح موفقیت‌ها")
    confirmed = models.BooleanField(default=False, verbose_name="تایید شده")
    removed = models.BooleanField(default=False, verbose_name="حذف شده")
    invest_percentage = models.FloatField(default=0.0, null=True, verbose_name="درصد پس‌انداز")
    corr_madadkar = models.ForeignKey(madadkar, on_delete=models.CASCADE, verbose_name="مددجوی حمایت‌کننده")

    class Meta:
        verbose_name_plural = _("مددجویان")
        verbose_name = _("مددجو")


class madadkar_remove_madadjoo():
    madadkar = models.ForeignKey(madadkar, on_delete=models.CASCADE)
    madadjoo = models.ForeignKey(madadjoo, on_delete=models.CASCADE, unique=True)
    hamyar = models.ForeignKey(hamyar, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField()


class madadjoo_madadkar_letter():
    madadjoo = models.ForeignKey(madadjoo, on_delete=models.CASCADE)
    madadkar = models.ForeignKey(madadkar, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(auto_now=True)

    class Meta:
        unique_together = (("madadjoo", "date"),)


class requirements():
    description = models.TextField(null=True)
    type = models.CharField(choices=['monthly', 'annual', 'instantly'], max_length=60)
    confirmed = models.BooleanField(default=False)
    urgent = models.BooleanField(default=False)
    cash = models.BooleanField(default=True)
    madadjoo = models.ForeignKey(madadjoo, on_delete=models.CASCADE)

class hamyar_system_payment():
    hamyar = models.ForeignKey(hamyar, on_delete=models.CASCADE)
    system = models.ForeignKey(information, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False)
    date = models.DateField(auto_now=True)

    class Meta:
        unique_together = (("hamyar", "date"),)


class sponsership():
    madadjoo = models.ForeignKey(madadjoo, on_delete=models.CASCADE)
    hamyar = models.ForeignKey(hamyar, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("madadjoo", "madadkar"),)

class hamyar_madadjoo_payment():
    madadjoo = models.ForeignKey(madadjoo, on_delete=models.CASCADE)
    hamyar = models.ForeignKey(hamyar, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False)
    type = models.CharField(choices=['monthly', 'annual', 'instantly'], max_length=60)
    date = models.DateField(auto_now=True)

    class Meta:
        unique_together = (("madadjoo", "hamyar", "date"),)


class hamyar_madadjoo_non_cash():
    hamyar = models.ForeignKey(hamyar, on_delete=models.CASCADE)
    madadjoo = models.ForeignKey(madadjoo, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    text = models.TextField()

    class Meta:
        unique_together = (("hamyar", "date", "madadjoo"),)


class hamyar_madadjoo_meeting(): #should process this table when madadkar wants to see her letters
    hamyar = models.ForeignKey(hamyar, on_delete=models.CASCADE)
    madadjoo = models.ForeignKey(madadjoo, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

    class Meta:
        unique_together = (("hamyar", "date", "madadjoo"),)

class madadjoo_hamyar_letter():
    hamyar = models.ForeignKey(hamyar, on_delete=models.CASCADE)
    madadjoo = models.ForeignKey(madadjoo, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    text = models.TextField()
    confirmed = models.BooleanField(default=False)

    class Meta:
        unique_together = (("hamyar", "date", "madadjoo"),)

