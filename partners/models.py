from django.db import models


class Partner(models.Model):
    updtick_0 = models.IntegerField(db_column='UPDTICK_0')
    bp = models.CharField(db_column='BPRNUM_0', unique=True, max_length=15)
    is_active = models.SmallIntegerField(db_column='ENAFLG_0')
    category = models.CharField(db_column='BRGCOD_0', max_length=5)
    customer_or_supplier_origin_category = models.CharField(
        db_column='BRGOBJ_0', max_length=3
    )
    company_name_0 = models.CharField(db_column='BPRNAM_0', max_length=35)
    company_name_1 = models.CharField(db_column='BPRNAM_1', max_length=35)
    short_description = models.CharField(db_column='BPRSHO_0', max_length=10)
    european_vat_number = models.CharField(db_column='EECNUM_0', max_length=20)
    is_inter_site = models.SmallIntegerField(db_column='BETFCY_0')
    site = models.CharField(db_column='FCY_0', max_length=5)
    country = models.CharField(db_column='CRY_0', max_length=3)
    site_identification_number = models.CharField(db_column='CRN_0', max_length=20)
    standard_industrial_classification_code = models.CharField(
        db_column='NAF_0', max_length=1
    )
    currency = models.CharField(db_column='CUR_0', max_length=3)
    language = models.CharField(db_column='LAN_0', max_length=3)
    acronym = models.CharField(db_column='BPRLOG_0', max_length=10)
    italian_tax_number = models.CharField(db_column='VATNUM_0', max_length=1)
    fiscal_code = models.CharField(db_column='FISCOD_0', max_length=1)
    consolidation_group = models.CharField(db_column='GRUGPY_0', max_length=5)
    consolidation_code = models.CharField(db_column='GRUCOD_0', max_length=1)
    is_customer = models.SmallIntegerField(db_column='BPCFLG_0')
    is_supplier = models.SmallIntegerField(db_column='BPSFLG_0')
    is_grantor = models.SmallIntegerField(db_column='CCNFLG_0')
    is_carrier = models.SmallIntegerField(db_column='BPTFLG_0')
    is_factor = models.SmallIntegerField(db_column='FCTFLG_0')
    is_sales_representative = models.SmallIntegerField(db_column='REPFLG_0')
    is_miscellaneous_business_partner = models.SmallIntegerField(db_column='BPRACC_0')
    is_prospect = models.SmallIntegerField(db_column='PPTFLG_0')
    is_service_supplier = models.SmallIntegerField(db_column='PRVFLG_0')
    is_service_caller = models.SmallIntegerField(db_column='DOOFLG_0')
    accounting_code = models.CharField(db_column='ACCCOD_0', max_length=10)
    ship_to = models.SmallIntegerField(db_column='PTHFLG_0')
    miscellaneous_flag_0 = models.SmallIntegerField(db_column='BPRFLG_0')
    miscellaneous_flag_1 = models.SmallIntegerField(db_column='BPRFLG_1')
    miscellaneous_flag_2 = models.SmallIntegerField(db_column='BPRFLG_2')
    miscellaneous_flag_3 = models.SmallIntegerField(db_column='BPRFLG_3')
    default_address = models.CharField(db_column='BPAADD_0', max_length=5)
    default_contact = models.CharField(db_column='CNTNAM_0', max_length=35)
    default_bank_id = models.CharField(db_column='BIDNUM_0', max_length=30)
    country_bank_id = models.CharField(db_column='BIDCRY_0', max_length=3)
    report_access_code = models.CharField(db_column='ACS_0', max_length=10)
    export_number = models.IntegerField(db_column='EXPNUM_0')
    expense_entry_type = models.CharField(db_column='BPRGTETYP_0', max_length=5)
    is_mailing_prohibited = models.SmallIntegerField(db_column='BPRFBDMAG_0')
    cfonb_payment_method = models.CharField(db_column='MODPAM_0', max_length=20)
    non_resident_account = models.CharField(db_column='ACCNONREI_0', max_length=5)
    is_physical_person = models.SmallIntegerField(db_column='LEGETT_0')
    is_cash_excluded = models.SmallIntegerField(db_column='CFOEXD_0')
    create_user = models.CharField(db_column='CREUSR_0', max_length=5)
    create_date = models.DateTimeField(db_column='CREDAT_0')
    update_user = models.CharField(db_column='UPDUSR_0', max_length=5)
    update_date = models.DateTimeField(db_column='UPDDAT_0')
    document_type = models.SmallIntegerField(db_column='DOCTYP_0')
    is_public_sector = models.SmallIntegerField(db_column='BPPFLG_0')
    create_datetime = models.DateTimeField(db_column='CREDATTIM_0')
    update_datetime = models.DateTimeField(db_column='UPDDATTIM_0')
    auuid = models.BinaryField(db_column='AUUID_0')
    related_company = models.SmallIntegerField(db_column='CPYREL_0')
    consolidation_partner = models.CharField(db_column='CSLBPR_0', max_length=1)
    registration_number = models.CharField(db_column='REGNUM_0', max_length=1)
    vat_number = models.CharField(db_column='VATNO_0', max_length=1)
    zpagitm_0 = models.SmallIntegerField(db_column='ZPAGITM_0')
    eori_number = models.CharField(db_column='EORINUM_0', max_length=35)
    service_code = models.CharField(db_column='INTSRVCOD_0', max_length=1)
    zeditor_0 = models.SmallIntegerField(db_column='ZEDITOR_0')
    routing_code = models.CharField(db_column='RTGCOD_0', max_length=1)
    electronic_invoice_type = models.SmallIntegerField(db_column='EINVTYP_0')
    zintvsp_0 = models.SmallIntegerField(db_column='ZINTVSP_0')
    e_invoicing_mapping_code = models.CharField(db_column='MAPCOD_0', max_length=1)
    zagente_0 = models.SmallIntegerField(db_column='ZAGENTE_0')
    zgesflg_0 = models.SmallIntegerField(db_column='ZGESFLG_0')
    zanaflg_0 = models.SmallIntegerField(db_column='ZANAFLG_0')
    zexpflg_0 = models.SmallIntegerField(db_column='ZEXPFLG_0')
    id = models.BigAutoField(db_column='ROWID', primary_key=True)

    class Meta:
        managed = False
        db_table = 'BPARTNER'
        unique_together = (('is_inter_site', 'site', 'bp'),)


class Address(models.Model):
    updtick_0 = models.IntegerField(db_column='UPDTICK_0')
    entity_type = models.SmallIntegerField(db_column='BPATYP_0')
    entity_number = models.CharField(db_column='BPANUM_0', max_length=15)
    code = models.CharField(db_column='BPAADD_0', max_length=5)
    description = models.CharField(db_column='BPADES_0', max_length=30)
    default_bank_id = models.CharField(db_column='BPABID_0', max_length=30)
    is_default = models.SmallIntegerField(db_column='BPAADDFLG_0')
    address_line_0 = models.CharField(db_column='BPAADDLIG_0', max_length=50)
    address_line_1 = models.CharField(db_column='BPAADDLIG_1', max_length=50)
    address_line_2 = models.CharField(db_column='BPAADDLIG_2', max_length=50)
    postal_code = models.CharField(db_column='POSCOD_0', max_length=10)
    city = models.CharField(db_column='CTY_0', max_length=40)
    federal_id_code = models.CharField(db_column='CODSEE_0', max_length=1)
    state = models.CharField(db_column='SAT_0', max_length=35)
    country = models.CharField(db_column='CRY_0', max_length=3)
    country_name = models.CharField(db_column='CRYNAM_0', max_length=40)
    telephone_0 = models.CharField(db_column='TEL_0', max_length=40)
    telephone_1 = models.CharField(db_column='TEL_1', max_length=40)
    telephone_2 = models.CharField(db_column='TEL_2', max_length=40)
    telephone_3 = models.CharField(db_column='TEL_3', max_length=40)
    telephone_4 = models.CharField(db_column='TEL_4', max_length=40)
    fax = models.CharField(db_column='FAX_0', max_length=40)
    mobile_phone = models.CharField(db_column='MOB_0', max_length=40)
    email_address_0 = models.CharField(db_column='WEB_0', max_length=80)
    email_address_1 = models.CharField(db_column='WEB_1', max_length=80)
    email_address_2 = models.CharField(db_column='WEB_2', max_length=80)
    email_address_3 = models.CharField(db_column='WEB_3', max_length=80)
    email_address_4 = models.CharField(db_column='WEB_4', max_length=80)
    website = models.CharField(db_column='FCYWEB_0', max_length=250)
    external_id = models.CharField(db_column='EXTNUM_0', max_length=30)
    export_number = models.IntegerField(db_column='EXPNUM_0')
    create_user = models.CharField(db_column='CREUSR_0', max_length=5)
    create_date = models.DateTimeField(db_column='CREDAT_0')
    update_user = models.CharField(db_column='UPDUSR_0', max_length=5)
    update_date = models.DateTimeField(db_column='UPDDAT_0')
    create_datetime = models.DateTimeField(db_column='CREDATTIM_0')
    update_datetime = models.DateTimeField(db_column='UPDDATTIM_0')
    auuid = models.BinaryField(db_column='AUUID_0')
    is_valid = models.SmallIntegerField(db_column='ADRVAL_0')
    gln = models.CharField(db_column='GLNCOD_0', max_length=13)
    site_tax_id = models.CharField(db_column='CRN_0', max_length=20)
    id = models.BigAutoField(db_column='ROWID', primary_key=True)

    class Meta:
        managed = False
        db_table = 'BPADDRESS'
        unique_together = (('entity_type', 'entity_number', 'code'),)


class Supplier(models.Model):
    updtick_0 = models.IntegerField(db_column='UPDTICK_0')
    supplier = models.CharField(db_column='BPSNUM_0', unique=True, max_length=15)
    company_name = models.CharField(db_column='BPSNAM_0', max_length=35)
    short_description = models.CharField(db_column='BPSSHO_0', max_length=10)
    supplier_type = models.SmallIntegerField(db_column='BPSTYP_0')
    category = models.CharField(db_column='BSGCOD_0', max_length=5)
    pay_to = models.CharField(db_column='BPRPAY_0', max_length=15)
    pay_to_address = models.CharField(db_column='BPAPAY_0', max_length=5)
    supplier_invoice = models.CharField(db_column='BPSINV_0', max_length=15)
    billing_address = models.CharField(db_column='BPAINV_0', max_length=5)
    supplier_group = models.CharField(db_column='BPSGRU_0', max_length=15)
    risk_supplier = models.CharField(db_column='BPSRSK_0', max_length=15)
    customer_number = models.CharField(db_column='BPCNUMBPS_0', max_length=15)
    carrier = models.CharField(db_column='BPTNUM_0', max_length=15)
    default_contact = models.CharField(db_column='CNTNAM_0', max_length=35)
    location = models.CharField(db_column='LOC_0', max_length=10)
    abc_class = models.SmallIntegerField(db_column='ABCCLS_0')
    unavailable = models.CharField(db_column='UVYCOD_0', max_length=5)
    currency = models.CharField(db_column='CUR_0', max_length=3)
    rate_type = models.SmallIntegerField(db_column='CHGTYP_0')
    payment_term = models.CharField(db_column='PTE_0', max_length=15)
    discount_code = models.CharField(db_column='DEP_0', max_length=5)
    tax_rule = models.CharField(db_column='VACBPR_0', max_length=5)
    delivery_mode = models.CharField(db_column='MDL_0', max_length=5)
    incoterm = models.CharField(db_column='EECICT_0', max_length=5)
    intrastat_transport_location = models.SmallIntegerField(db_column='EECLOC_0')
    statistical_group_0 = models.CharField(db_column='TSSCOD_0', max_length=20)
    statistical_group_1 = models.CharField(db_column='TSSCOD_1', max_length=20)
    statistical_group_2 = models.CharField(db_column='TSSCOD_2', max_length=20)
    statistical_group_3 = models.CharField(db_column='TSSCOD_3', max_length=20)
    statistical_group_4 = models.CharField(db_column='TSSCOD_4', max_length=20)
    invoice_amount_0 = models.DecimalField(
        db_column='INVDTAAMT_0', max_digits=20, decimal_places=5
    )
    invoice_amount_1 = models.DecimalField(
        db_column='INVDTAAMT_1', max_digits=20, decimal_places=5
    )
    invoice_amount_2 = models.DecimalField(
        db_column='INVDTAAMT_2', max_digits=20, decimal_places=5
    )
    invoice_amount_3 = models.DecimalField(
        db_column='INVDTAAMT_3', max_digits=20, decimal_places=5
    )
    invoice_amount_4 = models.DecimalField(
        db_column='INVDTAAMT_4', max_digits=20, decimal_places=5
    )
    invoice_amount_5 = models.DecimalField(
        db_column='INVDTAAMT_5', max_digits=20, decimal_places=5
    )
    invoice_amount_6 = models.DecimalField(
        db_column='INVDTAAMT_6', max_digits=20, decimal_places=5
    )
    invoice_amount_7 = models.DecimalField(
        db_column='INVDTAAMT_7', max_digits=20, decimal_places=5
    )
    invoice_amount_8 = models.DecimalField(
        db_column='INVDTAAMT_8', max_digits=20, decimal_places=5
    )
    invoice_amount_9 = models.DecimalField(
        db_column='INVDTAAMT_9', max_digits=20, decimal_places=5
    )
    invoice_amount_10 = models.DecimalField(
        db_column='INVDTAAMT_10', max_digits=20, decimal_places=5
    )
    invoice_amount_11 = models.DecimalField(
        db_column='INVDTAAMT_11', max_digits=20, decimal_places=5
    )
    invoice_amount_12 = models.DecimalField(
        db_column='INVDTAAMT_12', max_digits=20, decimal_places=5
    )
    invoice_amount_13 = models.DecimalField(
        db_column='INVDTAAMT_13', max_digits=20, decimal_places=5
    )
    invoice_amount_14 = models.DecimalField(
        db_column='INVDTAAMT_14', max_digits=20, decimal_places=5
    )
    invoice_amount_15 = models.DecimalField(
        db_column='INVDTAAMT_15', max_digits=20, decimal_places=5
    )
    invoice_amount_16 = models.DecimalField(
        db_column='INVDTAAMT_16', max_digits=20, decimal_places=5
    )
    invoice_amount_17 = models.DecimalField(
        db_column='INVDTAAMT_17', max_digits=20, decimal_places=5
    )
    invoice_amount_18 = models.DecimalField(
        db_column='INVDTAAMT_18', max_digits=20, decimal_places=5
    )
    invoice_amount_19 = models.DecimalField(
        db_column='INVDTAAMT_19', max_digits=20, decimal_places=5
    )
    invoice_amount_20 = models.DecimalField(
        db_column='INVDTAAMT_20', max_digits=20, decimal_places=5
    )
    invoice_amount_21 = models.DecimalField(
        db_column='INVDTAAMT_21', max_digits=20, decimal_places=5
    )
    invoice_amount_22 = models.DecimalField(
        db_column='INVDTAAMT_22', max_digits=20, decimal_places=5
    )
    invoice_amount_23 = models.DecimalField(
        db_column='INVDTAAMT_23', max_digits=20, decimal_places=5
    )
    invoice_amount_24 = models.DecimalField(
        db_column='INVDTAAMT_24', max_digits=20, decimal_places=5
    )
    invoice_amount_25 = models.DecimalField(
        db_column='INVDTAAMT_25', max_digits=20, decimal_places=5
    )
    invoice_amount_26 = models.DecimalField(
        db_column='INVDTAAMT_26', max_digits=20, decimal_places=5
    )
    invoice_amount_27 = models.DecimalField(
        db_column='INVDTAAMT_27', max_digits=20, decimal_places=5
    )
    invoice_amount_28 = models.DecimalField(
        db_column='INVDTAAMT_28', max_digits=20, decimal_places=5
    )
    invoice_amount_29 = models.DecimalField(
        db_column='INVDTAAMT_29', max_digits=20, decimal_places=5
    )
    invoicing_element_0 = models.SmallIntegerField(db_column='INVDTA_0')
    invoicing_element_1 = models.SmallIntegerField(db_column='INVDTA_1')
    invoicing_element_2 = models.SmallIntegerField(db_column='INVDTA_2')
    invoicing_element_3 = models.SmallIntegerField(db_column='INVDTA_3')
    invoicing_element_4 = models.SmallIntegerField(db_column='INVDTA_4')
    invoicing_element_5 = models.SmallIntegerField(db_column='INVDTA_5')
    invoicing_element_6 = models.SmallIntegerField(db_column='INVDTA_6')
    invoicing_element_7 = models.SmallIntegerField(db_column='INVDTA_7')
    invoicing_element_8 = models.SmallIntegerField(db_column='INVDTA_8')
    invoicing_element_9 = models.SmallIntegerField(db_column='INVDTA_9')
    invoicing_element_10 = models.SmallIntegerField(db_column='INVDTA_10')
    invoicing_element_11 = models.SmallIntegerField(db_column='INVDTA_11')
    invoicing_element_12 = models.SmallIntegerField(db_column='INVDTA_12')
    invoicing_element_13 = models.SmallIntegerField(db_column='INVDTA_13')
    invoicing_element_14 = models.SmallIntegerField(db_column='INVDTA_14')
    invoicing_element_15 = models.SmallIntegerField(db_column='INVDTA_15')
    invoicing_element_16 = models.SmallIntegerField(db_column='INVDTA_16')
    invoicing_element_17 = models.SmallIntegerField(db_column='INVDTA_17')
    invoicing_element_18 = models.SmallIntegerField(db_column='INVDTA_18')
    invoicing_element_19 = models.SmallIntegerField(db_column='INVDTA_19')
    invoicing_element_20 = models.SmallIntegerField(db_column='INVDTA_20')
    invoicing_element_21 = models.SmallIntegerField(db_column='INVDTA_21')
    invoicing_element_22 = models.SmallIntegerField(db_column='INVDTA_22')
    invoicing_element_23 = models.SmallIntegerField(db_column='INVDTA_23')
    invoicing_element_24 = models.SmallIntegerField(db_column='INVDTA_24')
    invoicing_element_25 = models.SmallIntegerField(db_column='INVDTA_25')
    invoicing_element_26 = models.SmallIntegerField(db_column='INVDTA_26')
    invoicing_element_27 = models.SmallIntegerField(db_column='INVDTA_27')
    invoicing_element_28 = models.SmallIntegerField(db_column='INVDTA_28')
    invoicing_element_29 = models.SmallIntegerField(db_column='INVDTA_29')
    amount_code_0 = models.SmallIntegerField(db_column='AMTCOD_0')
    amount_code_1 = models.SmallIntegerField(db_column='AMTCOD_1')
    amount_code_2 = models.SmallIntegerField(db_column='AMTCOD_2')
    amount_code_3 = models.SmallIntegerField(db_column='AMTCOD_3')
    amount_code_4 = models.SmallIntegerField(db_column='AMTCOD_4')
    amount_code_5 = models.SmallIntegerField(db_column='AMTCOD_5')
    amount_code_6 = models.SmallIntegerField(db_column='AMTCOD_6')
    amount_code_7 = models.SmallIntegerField(db_column='AMTCOD_7')
    amount_code_8 = models.SmallIntegerField(db_column='AMTCOD_8')
    amount_code_9 = models.SmallIntegerField(db_column='AMTCOD_9')
    amount_code_10 = models.SmallIntegerField(db_column='AMTCOD_10')
    amount_code_11 = models.SmallIntegerField(db_column='AMTCOD_11')
    amount_code_12 = models.SmallIntegerField(db_column='AMTCOD_12')
    amount_code_13 = models.SmallIntegerField(db_column='AMTCOD_13')
    amount_code_14 = models.SmallIntegerField(db_column='AMTCOD_14')
    amount_code_15 = models.SmallIntegerField(db_column='AMTCOD_15')
    amount_code_16 = models.SmallIntegerField(db_column='AMTCOD_16')
    amount_code_17 = models.SmallIntegerField(db_column='AMTCOD_17')
    amount_code_18 = models.SmallIntegerField(db_column='AMTCOD_18')
    amount_code_19 = models.SmallIntegerField(db_column='AMTCOD_19')
    amount_code_20 = models.SmallIntegerField(db_column='AMTCOD_20')
    amount_code_21 = models.SmallIntegerField(db_column='AMTCOD_21')
    amount_code_22 = models.SmallIntegerField(db_column='AMTCOD_22')
    amount_code_23 = models.SmallIntegerField(db_column='AMTCOD_23')
    amount_code_24 = models.SmallIntegerField(db_column='AMTCOD_24')
    amount_code_25 = models.SmallIntegerField(db_column='AMTCOD_25')
    amount_code_26 = models.SmallIntegerField(db_column='AMTCOD_26')
    amount_code_27 = models.SmallIntegerField(db_column='AMTCOD_27')
    amount_code_28 = models.SmallIntegerField(db_column='AMTCOD_28')
    amount_code_29 = models.SmallIntegerField(db_column='AMTCOD_29')
    price_list_structure = models.CharField(db_column='PLISTC_0', max_length=10)
    payment_bank = models.CharField(db_column='PAYBAN_0', max_length=5)
    accounting_code = models.CharField(db_column='ACCCOD_0', max_length=10)
    dimension_type_code_0 = models.CharField(db_column='DIE_0', max_length=3)
    dimension_type_code_1 = models.CharField(db_column='DIE_1', max_length=3)
    dimension_type_code_2 = models.CharField(db_column='DIE_2', max_length=3)
    dimension_type_code_3 = models.CharField(db_column='DIE_3', max_length=3)
    dimension_type_code_4 = models.CharField(db_column='DIE_4', max_length=3)
    dimension_type_code_5 = models.CharField(db_column='DIE_5', max_length=3)
    dimension_type_code_6 = models.CharField(db_column='DIE_6', max_length=3)
    dimension_type_code_7 = models.CharField(db_column='DIE_7', max_length=3)
    dimension_type_code_8 = models.CharField(db_column='DIE_8', max_length=3)
    dimension_type_code_9 = models.CharField(db_column='DIE_9', max_length=3)
    dimension_type_code_10 = models.CharField(db_column='DIE_10', max_length=3)
    dimension_type_code_11 = models.CharField(db_column='DIE_11', max_length=3)
    dimension_type_code_12 = models.CharField(db_column='DIE_12', max_length=3)
    dimension_type_code_13 = models.CharField(db_column='DIE_13', max_length=3)
    dimension_type_code_14 = models.CharField(db_column='DIE_14', max_length=3)
    dimension_type_code_15 = models.CharField(db_column='DIE_15', max_length=3)
    dimension_type_code_16 = models.CharField(db_column='DIE_16', max_length=3)
    dimension_type_code_17 = models.CharField(db_column='DIE_17', max_length=3)
    dimension_type_code_18 = models.CharField(db_column='DIE_18', max_length=3)
    dimension_type_code_19 = models.CharField(db_column='DIE_19', max_length=3)
    dimension_0 = models.CharField(db_column='CCE_0', max_length=15)
    dimension_1 = models.CharField(db_column='CCE_1', max_length=15)
    dimension_2 = models.CharField(db_column='CCE_2', max_length=15)
    dimension_3 = models.CharField(db_column='CCE_3', max_length=15)
    dimension_4 = models.CharField(db_column='CCE_4', max_length=15)
    dimension_5 = models.CharField(db_column='CCE_5', max_length=15)
    dimension_6 = models.CharField(db_column='CCE_6', max_length=15)
    dimension_7 = models.CharField(db_column='CCE_7', max_length=15)
    dimension_8 = models.CharField(db_column='CCE_8', max_length=15)
    dimension_9 = models.CharField(db_column='CCE_9', max_length=15)
    dimension_10 = models.CharField(db_column='CCE_10', max_length=15)
    dimension_11 = models.CharField(db_column='CCE_11', max_length=15)
    dimension_12 = models.CharField(db_column='CCE_12', max_length=15)
    dimension_13 = models.CharField(db_column='CCE_13', max_length=15)
    dimension_14 = models.CharField(db_column='CCE_14', max_length=15)
    dimension_15 = models.CharField(db_column='CCE_15', max_length=15)
    dimension_16 = models.CharField(db_column='CCE_16', max_length=15)
    dimension_17 = models.CharField(db_column='CCE_17', max_length=15)
    dimension_18 = models.CharField(db_column='CCE_18', max_length=15)
    dimension_19 = models.CharField(db_column='CCE_19', max_length=15)
    default_address = models.CharField(db_column='BPAADD_0', max_length=5)
    multi_line_order = models.SmallIntegerField(db_column='SEVLIN_0')
    order_text = models.CharField(db_column='ORDTEX_0', max_length=17)
    return_text = models.CharField(db_column='RTNTEX_0', max_length=17)
    lead_time_ranking_coefficient = models.DecimalField(
        db_column='LTIMRKCOE_0', max_digits=18, decimal_places=7
    )
    price_ranking_coefficient = models.DecimalField(
        db_column='PRIMRKCOE_0', max_digits=18, decimal_places=7
    )
    quality_ranking_coefficient = models.DecimalField(
        db_column='QLYMRKCOE_0', max_digits=18, decimal_places=7
    )
    quantity_ranking_coefficient = models.DecimalField(
        db_column='QTYMRKCOE_0', max_digits=18, decimal_places=7
    )
    free_ranking_coefficient = models.DecimalField(
        db_column='RSKMRKCOE_0', max_digits=18, decimal_places=7
    )
    lead_time_ranking = models.DecimalField(
        db_column='LTIMRK_0', max_digits=7, decimal_places=3
    )
    price_ranking = models.DecimalField(
        db_column='PRIMRK_0', max_digits=7, decimal_places=3
    )
    quality_ranking = models.DecimalField(
        db_column='QLYMRK_0', max_digits=7, decimal_places=3
    )
    quantity_ranking = models.DecimalField(
        db_column='QTYMRK_0', max_digits=7, decimal_places=3
    )
    free_ranking = models.DecimalField(
        db_column='RSKMRK_0', max_digits=7, decimal_places=3
    )
    total_ranking = models.DecimalField(
        db_column='GENMRK_0', max_digits=8, decimal_places=3
    )
    minimum_order_amount = models.DecimalField(
        db_column='ORDMINAMT_0', max_digits=27, decimal_places=13
    )
    credit_control = models.SmallIntegerField(db_column='OSTCTL_0')
    authorized_credit = models.DecimalField(
        db_column='OSTAUZAMT_0', max_digits=27, decimal_places=13
    )
    intrastat_statistical_increase = models.DecimalField(
        db_column='EECINCRAT_0', max_digits=8, decimal_places=3
    )
    notes = models.CharField(db_column='BPSREM_0', max_length=250)
    due_date_origin = models.SmallIntegerField(db_column='DUDCLC_0')
    currency_rate_determination = models.SmallIntegerField(db_column='CURCLC_0')
    must_remind_delivery = models.SmallIntegerField(db_column='FUPFLG_0')
    must_remind_acknowledgment = models.SmallIntegerField(db_column='OCNFLG_0')
    is_das_2_submitted = models.SmallIntegerField(db_column='DADFLG_0')
    service_supplier_code = models.CharField(db_column='PRVNUM_0', max_length=1)
    dispute_status = models.SmallIntegerField(db_column='DOUFLG_0')
    is_active = models.SmallIntegerField(db_column='ENAFLG_0')
    is_payment_held = models.SmallIntegerField(db_column='PAYLOKFLG_0')
    must_print_order_form = models.SmallIntegerField(db_column='NORPRNFLG_0')
    must_print_receipt_note = models.SmallIntegerField(db_column='NREPRNFLG_0')
    must_print_return_slip = models.SmallIntegerField(db_column='NRTPRNFLG_0')
    withholding_code = models.CharField(db_column='RITCOD_0', max_length=1)
    number_of_codes = models.SmallIntegerField(db_column='RITNBR_0')
    withholding_tax_allowance = models.DecimalField(
        db_column='RITRAT_0', max_digits=28, decimal_places=8
    )
    number_of_partners = models.SmallIntegerField(db_column='RITPARNBR_0')
    name_of_partner = models.CharField(db_column='RITPARNAM_0', max_length=1)
    partner_held = models.DecimalField(
        db_column='RITPARCOE_0', max_digits=28, decimal_places=8
    )
    cai_number = models.CharField(db_column='CAI_0', max_length=1)
    cai_validity_date = models.DateTimeField(db_column='DATVLYCAI_0')
    vat_collection_agent = models.SmallIntegerField(db_column='AGTPCP_0')
    regional_taxes = models.SmallIntegerField(db_column='AGTSATTAX_0')
    provinces = models.CharField(db_column='SATTAX_0', max_length=1)
    collection_agent = models.SmallIntegerField(db_column='FLGSATTAX_0')
    customer_number_for_supplier = models.CharField(db_column='BPCNUM_0', max_length=1)
    template_code = models.CharField(db_column='TPMCOD_0', max_length=5)
    account_structure = models.CharField(db_column='DIA_0', max_length=10)
    expense_allocation = models.CharField(db_column='IPTEXS_0', max_length=20)
    export_number = models.IntegerField(db_column='EXPNUM_0')
    create_user = models.CharField(db_column='CREUSR_0', max_length=5)
    create_date = models.DateTimeField(db_column='CREDAT_0')
    update_user = models.CharField(db_column='UPDUSR_0', max_length=5)
    update_date = models.DateTimeField(db_column='UPDDAT_0')
    matching_tolerance = models.CharField(db_column='MATTOL_0', max_length=5)
    form_1099 = models.SmallIntegerField(db_column='FRM1099_0')
    box_1099 = models.CharField(db_column='BOX1099_0', max_length=1)
    create_datetime = models.DateTimeField(db_column='CREDATTIM_0')
    update_datetime = models.DateTimeField(db_column='UPDDATTIM_0')
    auuid = models.BinaryField(db_column='AUUID_0')
    is_281_submitted = models.SmallIntegerField(db_column='FLG281_0')
    amount_type = models.SmallIntegerField(db_column='PURPRITYP_0')
    is_cash_vat = models.SmallIntegerField(db_column='CSHVAT_0')
    cash_vat_deadline = models.DateTimeField(db_column='CSHDAT_0')
    auto_invoice_code = models.CharField(db_column='AUTINVCOD_0', max_length=5)
    free_freight_threshold = models.DecimalField(
        db_column='ORDFREFRT_0', max_digits=27, decimal_places=13
    )
    payroll_interface_distribution = models.CharField(db_column='BPRDSP_0', max_length=10)
    rex_number = models.CharField(db_column='REXNUM_0', max_length=30)
    has_no_whit_list_verification = models.SmallIntegerField(db_column='WLFLG_0')
    zeditor_0 = models.SmallIntegerField(db_column='ZEDITOR_0')
    default_invoicing_module = models.SmallIntegerField(db_column='INVORIMOD_0')
    zarrlqd_0 = models.DateTimeField(db_column='ZARRLQD_0')
    id = models.BigAutoField(db_column='ROWID', primary_key=True)

    class Meta:
        managed = False
        db_table = 'BPSUPPLIER'


class Customer(models.Model):
    updtick_0 = models.IntegerField(db_column='UPDTICK_0')
    customer = models.CharField(db_column='BPCNUM_0', max_length=15)
    company_name = models.CharField(db_column='BPCNAM_0', max_length=35)
    short_description = models.CharField(db_column='BPCSHO_0', max_length=10)
    category = models.CharField(db_column='BCGCOD_0', max_length=5)
    group = models.CharField(db_column='GRP_0', max_length=5)
    type = models.SmallIntegerField(db_column='BPCTYP_0')
    bill_to_customer = models.CharField(db_column='BPCINV_0', max_length=15)
    bill_address = models.CharField(db_column='BPAINV_0', max_length=5)
    pay_by_customer = models.CharField(db_column='BPCPYR_0', max_length=15)
    pay_address = models.CharField(db_column='BPAPYR_0', max_length=5)
    customer_group = models.CharField(db_column='BPCGRU_0', max_length=15)
    risk_customer = models.CharField(db_column='BPCRSK_0', max_length=15)
    default_address = models.CharField(db_column='BPAADD_0', max_length=5)
    ship_to_customer_address = models.CharField(db_column='BPDADD_0', max_length=5)
    default_contact = models.CharField(db_column='CNTNAM_0', max_length=35)
    is_active = models.SmallIntegerField(db_column='BPCSTA_0')
    prospect = models.SmallIntegerField(db_column='PPTFLG_0')
    supplier_number = models.CharField(db_column='BPCBPSNUM_0', max_length=15)
    factor = models.CharField(db_column='FCTNUM_0', max_length=15)
    currency = models.CharField(db_column='CUR_0', max_length=3)
    rate_type = models.SmallIntegerField(db_column='CHGTYP_0')
    commission_category = models.SmallIntegerField(db_column='COMCAT_0')
    sales_rep_0 = models.CharField(db_column='REP_0', max_length=15)
    sales_rep_1 = models.CharField(db_column='REP_1', max_length=15)
    tax_rule = models.CharField(db_column='VACBPR_0', max_length=5)
    exemption_number = models.CharField(db_column='VATEXN_0', max_length=15)
    payment_term = models.CharField(db_column='PTE_0', max_length=15)
    freight_invoicing = models.SmallIntegerField(db_column='FREINV_0')
    settlement_discount = models.CharField(db_column='DEP_0', max_length=5)
    invoice_amount_0 = models.DecimalField(
        db_column='INVDTAAMT_0', max_digits=20, decimal_places=5
    )
    invoice_amount_1 = models.DecimalField(
        db_column='INVDTAAMT_1', max_digits=20, decimal_places=5
    )
    invoice_amount_2 = models.DecimalField(
        db_column='INVDTAAMT_2', max_digits=20, decimal_places=5
    )
    invoice_amount_3 = models.DecimalField(
        db_column='INVDTAAMT_3', max_digits=20, decimal_places=5
    )
    invoice_amount_4 = models.DecimalField(
        db_column='INVDTAAMT_4', max_digits=20, decimal_places=5
    )
    invoice_amount_5 = models.DecimalField(
        db_column='INVDTAAMT_5', max_digits=20, decimal_places=5
    )
    invoice_amount_6 = models.DecimalField(
        db_column='INVDTAAMT_6', max_digits=20, decimal_places=5
    )
    invoice_amount_7 = models.DecimalField(
        db_column='INVDTAAMT_7', max_digits=20, decimal_places=5
    )
    invoice_amount_8 = models.DecimalField(
        db_column='INVDTAAMT_8', max_digits=20, decimal_places=5
    )
    invoice_amount_9 = models.DecimalField(
        db_column='INVDTAAMT_9', max_digits=20, decimal_places=5
    )
    invoice_amount_10 = models.DecimalField(
        db_column='INVDTAAMT_10', max_digits=20, decimal_places=5
    )
    invoice_amount_11 = models.DecimalField(
        db_column='INVDTAAMT_11', max_digits=20, decimal_places=5
    )
    invoice_amount_12 = models.DecimalField(
        db_column='INVDTAAMT_12', max_digits=20, decimal_places=5
    )
    invoice_amount_13 = models.DecimalField(
        db_column='INVDTAAMT_13', max_digits=20, decimal_places=5
    )
    invoice_amount_14 = models.DecimalField(
        db_column='INVDTAAMT_14', max_digits=20, decimal_places=5
    )
    invoice_amount_15 = models.DecimalField(
        db_column='INVDTAAMT_15', max_digits=20, decimal_places=5
    )
    invoice_amount_16 = models.DecimalField(
        db_column='INVDTAAMT_16', max_digits=20, decimal_places=5
    )
    invoice_amount_17 = models.DecimalField(
        db_column='INVDTAAMT_17', max_digits=20, decimal_places=5
    )
    invoice_amount_18 = models.DecimalField(
        db_column='INVDTAAMT_18', max_digits=20, decimal_places=5
    )
    invoice_amount_19 = models.DecimalField(
        db_column='INVDTAAMT_19', max_digits=20, decimal_places=5
    )
    invoice_amount_20 = models.DecimalField(
        db_column='INVDTAAMT_20', max_digits=20, decimal_places=5
    )
    invoice_amount_21 = models.DecimalField(
        db_column='INVDTAAMT_21', max_digits=20, decimal_places=5
    )
    invoice_amount_22 = models.DecimalField(
        db_column='INVDTAAMT_22', max_digits=20, decimal_places=5
    )
    invoice_amount_23 = models.DecimalField(
        db_column='INVDTAAMT_23', max_digits=20, decimal_places=5
    )
    invoice_amount_24 = models.DecimalField(
        db_column='INVDTAAMT_24', max_digits=20, decimal_places=5
    )
    invoice_amount_25 = models.DecimalField(
        db_column='INVDTAAMT_25', max_digits=20, decimal_places=5
    )
    invoice_amount_26 = models.DecimalField(
        db_column='INVDTAAMT_26', max_digits=20, decimal_places=5
    )
    invoice_amount_27 = models.DecimalField(
        db_column='INVDTAAMT_27', max_digits=20, decimal_places=5
    )
    invoice_amount_28 = models.DecimalField(
        db_column='INVDTAAMT_28', max_digits=20, decimal_places=5
    )
    invoice_amount_29 = models.DecimalField(
        db_column='INVDTAAMT_29', max_digits=20, decimal_places=5
    )
    invoicing_element_0 = models.SmallIntegerField(db_column='INVDTA_0')
    invoicing_element_1 = models.SmallIntegerField(db_column='INVDTA_1')
    invoicing_element_2 = models.SmallIntegerField(db_column='INVDTA_2')
    invoicing_element_3 = models.SmallIntegerField(db_column='INVDTA_3')
    invoicing_element_4 = models.SmallIntegerField(db_column='INVDTA_4')
    invoicing_element_5 = models.SmallIntegerField(db_column='INVDTA_5')
    invoicing_element_6 = models.SmallIntegerField(db_column='INVDTA_6')
    invoicing_element_7 = models.SmallIntegerField(db_column='INVDTA_7')
    invoicing_element_8 = models.SmallIntegerField(db_column='INVDTA_8')
    invoicing_element_9 = models.SmallIntegerField(db_column='INVDTA_9')
    invoicing_element_10 = models.SmallIntegerField(db_column='INVDTA_10')
    invoicing_element_11 = models.SmallIntegerField(db_column='INVDTA_11')
    invoicing_element_12 = models.SmallIntegerField(db_column='INVDTA_12')
    invoicing_element_13 = models.SmallIntegerField(db_column='INVDTA_13')
    invoicing_element_14 = models.SmallIntegerField(db_column='INVDTA_14')
    invoicing_element_15 = models.SmallIntegerField(db_column='INVDTA_15')
    invoicing_element_16 = models.SmallIntegerField(db_column='INVDTA_16')
    invoicing_element_17 = models.SmallIntegerField(db_column='INVDTA_17')
    invoicing_element_18 = models.SmallIntegerField(db_column='INVDTA_18')
    invoicing_element_19 = models.SmallIntegerField(db_column='INVDTA_19')
    invoicing_element_20 = models.SmallIntegerField(db_column='INVDTA_20')
    invoicing_element_21 = models.SmallIntegerField(db_column='INVDTA_21')
    invoicing_element_22 = models.SmallIntegerField(db_column='INVDTA_22')
    invoicing_element_23 = models.SmallIntegerField(db_column='INVDTA_23')
    invoicing_element_24 = models.SmallIntegerField(db_column='INVDTA_24')
    invoicing_element_25 = models.SmallIntegerField(db_column='INVDTA_25')
    invoicing_element_26 = models.SmallIntegerField(db_column='INVDTA_26')
    invoicing_element_27 = models.SmallIntegerField(db_column='INVDTA_27')
    invoicing_element_28 = models.SmallIntegerField(db_column='INVDTA_28')
    invoicing_element_29 = models.SmallIntegerField(db_column='INVDTA_29')
    statistical_group_0 = models.CharField(db_column='TSCCOD_0', max_length=20)
    statistical_group_1 = models.CharField(db_column='TSCCOD_1', max_length=20)
    statistical_group_2 = models.CharField(db_column='TSCCOD_2', max_length=20)
    statistical_group_3 = models.CharField(db_column='TSCCOD_3', max_length=20)
    statistical_group_4 = models.CharField(db_column='TSCCOD_4', max_length=20)
    price_type = models.SmallIntegerField(db_column='PRITYP_0')
    notes = models.CharField(db_column='BPCREM_0', max_length=250)
    credit_control = models.SmallIntegerField(db_column='OSTCTL_0')
    authorized_credit = models.DecimalField(
        db_column='OSTAUZ_0', max_digits=27, decimal_places=13
    )
    min_order_amount = models.DecimalField(
        db_column='ORDMINAMT_0', max_digits=27, decimal_places=13
    )
    credit_insurance = models.DecimalField(
        db_column='CDTISR_0', max_digits=27, decimal_places=13
    )
    insurance_date = models.DateTimeField(db_column='CDTISRDAT_0')
    insurance_company = models.CharField(
        db_column='BPCCDTISR_0',
        max_length=15,
    )
    reminder_type = models.SmallIntegerField(db_column='FUPTYP_0')
    minimum_reminder = models.DecimalField(
        db_column='FUPMINAMT_0', max_digits=27, decimal_places=13
    )
    note_type = models.SmallIntegerField(db_column='SOIPER_0')
    payment_bank = models.CharField(db_column='PAYBAN_0', max_length=5)
    accounting_code = models.CharField(db_column='ACCCOD_0', max_length=10)
    dimension_type_code_0 = models.CharField(db_column='DIE_0', max_length=3)
    dimension_type_code_1 = models.CharField(db_column='DIE_1', max_length=3)
    dimension_type_code_2 = models.CharField(db_column='DIE_2', max_length=3)
    dimension_type_code_3 = models.CharField(db_column='DIE_3', max_length=3)
    dimension_type_code_4 = models.CharField(db_column='DIE_4', max_length=3)
    dimension_type_code_5 = models.CharField(db_column='DIE_5', max_length=3)
    dimension_type_code_6 = models.CharField(db_column='DIE_6', max_length=3)
    dimension_type_code_7 = models.CharField(db_column='DIE_7', max_length=3)
    dimension_type_code_8 = models.CharField(db_column='DIE_8', max_length=3)
    dimension_type_code_9 = models.CharField(db_column='DIE_9', max_length=3)
    dimension_type_code_10 = models.CharField(db_column='DIE_10', max_length=3)
    dimension_type_code_11 = models.CharField(db_column='DIE_11', max_length=3)
    dimension_type_code_12 = models.CharField(db_column='DIE_12', max_length=3)
    dimension_type_code_13 = models.CharField(db_column='DIE_13', max_length=3)
    dimension_type_code_14 = models.CharField(db_column='DIE_14', max_length=3)
    dimension_type_code_15 = models.CharField(db_column='DIE_15', max_length=3)
    dimension_type_code_16 = models.CharField(db_column='DIE_16', max_length=3)
    dimension_type_code_17 = models.CharField(db_column='DIE_17', max_length=3)
    dimension_type_code_18 = models.CharField(db_column='DIE_18', max_length=3)
    dimension_type_code_19 = models.CharField(db_column='DIE_19', max_length=3)
    dimension_0 = models.CharField(db_column='CCE_0', max_length=15)
    dimension_1 = models.CharField(db_column='CCE_1', max_length=15)
    dimension_2 = models.CharField(db_column='CCE_2', max_length=15)
    dimension_3 = models.CharField(db_column='CCE_3', max_length=15)
    dimension_4 = models.CharField(db_column='CCE_4', max_length=15)
    dimension_5 = models.CharField(db_column='CCE_5', max_length=15)
    dimension_6 = models.CharField(db_column='CCE_6', max_length=15)
    dimension_7 = models.CharField(db_column='CCE_7', max_length=15)
    dimension_8 = models.CharField(db_column='CCE_8', max_length=15)
    dimension_9 = models.CharField(db_column='CCE_9', max_length=15)
    dimension_10 = models.CharField(db_column='CCE_10', max_length=15)
    dimension_11 = models.CharField(db_column='CCE_11', max_length=15)
    dimension_12 = models.CharField(db_column='CCE_12', max_length=15)
    dimension_13 = models.CharField(db_column='CCE_13', max_length=15)
    dimension_14 = models.CharField(db_column='CCE_14', max_length=15)
    dimension_15 = models.CharField(db_column='CCE_15', max_length=15)
    dimension_16 = models.CharField(db_column='CCE_16', max_length=15)
    dimension_17 = models.CharField(db_column='CCE_17', max_length=15)
    dimension_18 = models.CharField(db_column='CCE_18', max_length=15)
    dimension_19 = models.CharField(db_column='CCE_19', max_length=15)
    matchable = models.SmallIntegerField(db_column='MTCFLG_0')
    order_text_0 = models.CharField(db_column='ORDTEX_0', max_length=17)
    invoice_text_0 = models.CharField(db_column='INVTEX_0', max_length=17)
    loan_authorized = models.SmallIntegerField(db_column='LNDAUZ_0')
    print_acknowledgment = models.SmallIntegerField(db_column='OCNFLG_0')
    invoice_period = models.SmallIntegerField(db_column='INVPER_0')
    due_date_origin = models.SmallIntegerField(db_column='DUDCLC_0')
    close_unfilled_lines = models.SmallIntegerField(db_column='ORDCLE_0')
    one_order_per_delivery = models.SmallIntegerField(db_column='ODL_0')
    partial_delivery = models.SmallIntegerField(db_column='DME_0')
    invoicing_mode = models.SmallIntegerField(db_column='IME_0')
    business = models.CharField(db_column='BUS_0', max_length=20)
    source = models.CharField(db_column='ORIPPT_0', max_length=20)
    token_credits = models.IntegerField(db_column='PITCDT_0')
    additional_info = models.IntegerField(db_column='PITCPT_0')
    total_credit = models.IntegerField(db_column='TOTPIT_0')
    service_contract = models.CharField(db_column='COTCHX_0', max_length=20)
    tokens_necessary = models.IntegerField(db_column='COTPITRQD_0')
    first_contact_date = models.DateTimeField(db_column='CNTFIRDAT_0')
    first_order_date = models.DateTimeField(db_column='ORDFIRDAT_0')
    last_quote_date = models.DateTimeField(db_column='QUOLASDAT_0')
    last_contact_date = models.DateTimeField(db_column='CNTLASDAT_0')
    next_contact_date = models.DateTimeField(db_column='CNTNEXDAT_0')
    last_contact_type = models.SmallIntegerField(db_column='CNTLASTYP_0')
    next_contact_type = models.SmallIntegerField(db_column='CNTNEXTYP_0')
    abc_class = models.SmallIntegerField(db_column='ABCCLS_0')
    vat_collection_agent = models.SmallIntegerField(db_column='AGTPCP_0')
    regional_taxes = models.SmallIntegerField(db_column='AGTSATTAX_0')
    provinces = models.CharField(db_column='SATTAX_0', max_length=1)
    regional_collection_agent = models.SmallIntegerField(db_column='FLGSATTAX_0')
    template_code = models.CharField(db_column='TPMCOD_0', max_length=5)
    account_structure = models.CharField(db_column='DIA_0', max_length=10)
    customer_since = models.DateTimeField(db_column='BPCSNCDAT_0')
    export_number = models.IntegerField(db_column='EXPNUM_0')
    create_user = models.CharField(db_column='CREUSR_0', max_length=5)
    create_date = models.DateTimeField(db_column='CREDAT_0')
    update_user = models.CharField(db_column='UPDUSR_0', max_length=5)
    update_date = models.DateTimeField(db_column='UPDDAT_0')
    create_datetime = models.DateTimeField(db_column='CREDATTIM_0')
    update_datetime = models.DateTimeField(db_column='UPDDATTIM_0')
    auuid = models.BinaryField(db_column='AUUID_0')
    day_of_month_0 = models.SmallIntegerField(db_column='DAYMON_0')
    day_of_month_1 = models.SmallIntegerField(db_column='DAYMON_1')
    day_of_month_2 = models.SmallIntegerField(db_column='DAYMON_2')
    day_of_month_3 = models.SmallIntegerField(db_column='DAYMON_3')
    day_of_month_4 = models.SmallIntegerField(db_column='DAYMON_4')
    day_of_month_5 = models.SmallIntegerField(db_column='DAYMON_5')
    unavailable_period = models.CharField(db_column='UVYCOD2_0', max_length=5)
    tax_rule_0 = models.SmallIntegerField(db_column='CSHVATRGM_0')
    tax_rule_1 = models.SmallIntegerField(db_column='CSHVATRGM_1')
    tax_rule_2 = models.SmallIntegerField(db_column='CSHVATRGM_2')
    tax_rule_3 = models.SmallIntegerField(db_column='CSHVATRGM_3')
    tax_rule_4 = models.SmallIntegerField(db_column='CSHVATRGM_4')
    tax_rule_5 = models.SmallIntegerField(db_column='CSHVATRGM_5')
    tax_rule_6 = models.SmallIntegerField(db_column='CSHVATRGM_6')
    tax_rule_7 = models.SmallIntegerField(db_column='CSHVATRGM_7')
    tax_rule_8 = models.SmallIntegerField(db_column='CSHVATRGM_8')
    vat_start_date_0 = models.DateTimeField(db_column='VATSTRDAT_0')
    vat_start_date_1 = models.DateTimeField(db_column='VATSTRDAT_1')
    vat_start_date_2 = models.DateTimeField(db_column='VATSTRDAT_2')
    vat_start_date_3 = models.DateTimeField(db_column='VATSTRDAT_3')
    vat_start_date_4 = models.DateTimeField(db_column='VATSTRDAT_4')
    vat_start_date_5 = models.DateTimeField(db_column='VATSTRDAT_5')
    vat_start_date_6 = models.DateTimeField(db_column='VATSTRDAT_6')
    vat_start_date_7 = models.DateTimeField(db_column='VATSTRDAT_7')
    vat_start_date_8 = models.DateTimeField(db_column='VATSTRDAT_8')
    vat_end_date_0 = models.DateTimeField(db_column='VATENDDAT_0')
    vat_end_date_1 = models.DateTimeField(db_column='VATENDDAT_1')
    vat_end_date_2 = models.DateTimeField(db_column='VATENDDAT_2')
    vat_end_date_3 = models.DateTimeField(db_column='VATENDDAT_3')
    vat_end_date_4 = models.DateTimeField(db_column='VATENDDAT_4')
    vat_end_date_5 = models.DateTimeField(db_column='VATENDDAT_5')
    vat_end_date_6 = models.DateTimeField(db_column='VATENDDAT_6')
    vat_end_date_7 = models.DateTimeField(db_column='VATENDDAT_7')
    vat_end_date_8 = models.DateTimeField(db_column='VATENDDAT_8')
    is_subject_to_tax = models.SmallIntegerField(db_column='BELVATSUB_0')
    invoice_term = models.CharField(db_column='INVCND_0', max_length=20)
    is_efat_invoice = models.SmallIntegerField(db_column='ELECTINV_0')
    contact = models.CharField(db_column='CNTEFAT_0', max_length=15)
    start_date = models.DateTimeField(db_column='STRDATEFAT_0')
    is_electronic_invoice = models.SmallIntegerField(db_column='AEIFLG_0')
    id = models.BigAutoField(db_column='ROWID', primary_key=True)

    class Meta:
        managed = False
        db_table = 'BPCUSTOMER'
        unique_together = (('company_name', 'customer'),)
