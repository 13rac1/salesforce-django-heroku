# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from salesforce import models


class Contact(models.Model):
    is_deleted = models.BooleanField(verbose_name='Deleted', sf_read_only=models.READ_ONLY)
    master_record = models.ForeignKey('self', related_name='contact_masterrecord_set', sf_read_only=models.READ_ONLY, on_delete=models.DO_NOTHING, blank=True, null=True)
    #account = models.ForeignKey('Account', on_delete=models.DO_NOTHING, blank=True, null=True)
    last_name = models.CharField(max_length=80, verbose_name='Last Name')
    first_name = models.CharField(max_length=40, verbose_name='First Name', blank=True)
    salutation = models.CharField(max_length=40, verbose_name='Salutation', choices=[(u'Mr.', u'Mr.'), (u'Ms.', u'Ms.'), (u'Mrs.', u'Mrs.'), (u'Dr.', u'Dr.'), (u'Prof.', u'Prof.')], blank=True)
    name = models.CharField(max_length=121, verbose_name='Full Name', sf_read_only=models.READ_ONLY)
    other_street = models.TextField(verbose_name='Other Street', blank=True)
    other_city = models.CharField(max_length=40, verbose_name='Other City', blank=True)
    other_state = models.CharField(max_length=80, verbose_name='Other State/Province', blank=True)
    other_postal_code = models.CharField(max_length=20, verbose_name='Other Zip/Postal Code', blank=True)
    other_country = models.CharField(max_length=80, verbose_name='Other Country', blank=True)
    other_latitude = models.DecimalField(max_digits=18, decimal_places=15, verbose_name='Other Latitude', blank=True, null=True)
    other_longitude = models.DecimalField(max_digits=18, decimal_places=15, verbose_name='Other Longitude', blank=True, null=True)
    other_address = models.TextField(verbose_name='Other Address', sf_read_only=models.READ_ONLY, blank=True)  # This field type is a guess.
    mailing_street = models.TextField(verbose_name='Mailing Street', blank=True)
    mailing_city = models.CharField(max_length=40, verbose_name='Mailing City', blank=True)
    mailing_state = models.CharField(max_length=80, verbose_name='Mailing State/Province', blank=True)
    mailing_postal_code = models.CharField(max_length=20, verbose_name='Mailing Zip/Postal Code', blank=True)
    mailing_country = models.CharField(max_length=80, verbose_name='Mailing Country', blank=True)
    mailing_latitude = models.DecimalField(max_digits=18, decimal_places=15, verbose_name='Mailing Latitude', blank=True, null=True)
    mailing_longitude = models.DecimalField(max_digits=18, decimal_places=15, verbose_name='Mailing Longitude', blank=True, null=True)
    mailing_address = models.TextField(verbose_name='Mailing Address', sf_read_only=models.READ_ONLY, blank=True)  # This field type is a guess.
    phone = models.CharField(max_length=40, verbose_name='Business Phone', blank=True)
    fax = models.CharField(max_length=40, verbose_name='Business Fax', blank=True)
    mobile_phone = models.CharField(max_length=40, verbose_name='Mobile Phone', blank=True)
    home_phone = models.CharField(max_length=40, verbose_name='Home Phone', blank=True)
    other_phone = models.CharField(max_length=40, verbose_name='Other Phone', blank=True)
    assistant_phone = models.CharField(max_length=40, verbose_name='Asst. Phone', blank=True)
    reports_to = models.ForeignKey('self', related_name='contact_reportsto_set', on_delete=models.DO_NOTHING, blank=True, null=True)
    email = models.EmailField(verbose_name='Email', blank=True, null=True)
    title = models.CharField(max_length=128, verbose_name='Title', blank=True)
    department = models.CharField(max_length=80, verbose_name='Department', blank=True)
    assistant_name = models.CharField(max_length=40, verbose_name=u"Assistant's Name", blank=True)
    lead_source = models.CharField(max_length=40, verbose_name='Lead Source', choices=[(u'Web', u'Web'), (u'Phone Inquiry', u'Phone Inquiry'), (u'Partner Referral', u'Partner Referral'), (u'Purchased List', u'Purchased List'), (u'Other', u'Other')], blank=True)
    birthdate = models.DateField(verbose_name='Birthdate', blank=True, null=True)
    description = models.TextField(verbose_name='Contact Description', blank=True)
    #owner = models.ForeignKey('User', related_name='contact_owner_set', on_delete=models.DO_NOTHING)
    #created_date = models.DateTimeField(verbose_name='Created Date', sf_read_only=models.READ_ONLY)
    #created_by = models.ForeignKey('User', related_name='contact_createdby_set', sf_read_only=models.READ_ONLY, on_delete=models.DO_NOTHING)
    last_modified_date = models.DateTimeField(verbose_name='Last Modified Date', sf_read_only=models.READ_ONLY)
    #last_modified_by = models.ForeignKey('User', related_name='contact_lastmodifiedby_set', sf_read_only=models.READ_ONLY, on_delete=models.DO_NOTHING)
    system_modstamp = models.DateTimeField(verbose_name='System Modstamp', sf_read_only=models.READ_ONLY)
    last_activity_date = models.DateField(verbose_name='Last Activity', sf_read_only=models.READ_ONLY, blank=True, null=True)
    last_curequest_date = models.DateTimeField(db_column='LastCURequestDate', verbose_name='Last Stay-in-Touch Request Date', sf_read_only=models.READ_ONLY, blank=True, null=True)
    last_cuupdate_date = models.DateTimeField(db_column='LastCUUpdateDate', verbose_name='Last Stay-in-Touch Save Date', sf_read_only=models.READ_ONLY, blank=True, null=True)
    last_viewed_date = models.DateTimeField(verbose_name='Last Viewed Date', sf_read_only=models.READ_ONLY, blank=True, null=True)
    last_referenced_date = models.DateTimeField(verbose_name='Last Referenced Date', sf_read_only=models.READ_ONLY, blank=True, null=True)
    email_bounced_reason = models.CharField(max_length=255, verbose_name='Email Bounced Reason', blank=True)
    email_bounced_date = models.DateTimeField(verbose_name='Email Bounced Date', blank=True, null=True)
    is_email_bounced = models.BooleanField(verbose_name='Is Email Bounced', sf_read_only=models.READ_ONLY)
    class Meta(models.Model.Meta):
        db_table = 'Contact'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        # keyPrefix = '003'

