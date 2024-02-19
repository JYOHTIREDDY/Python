"""
Module: queries.py

This module contains all the PostgreSQL 
database queries which are being used
in this project
"""


RECOVERY_SELECT_QRY="SELECT pmt_num, pmt_recovery_type, pmt_recovery_status, init_date, success_date, return_date, return_code, noc_date, noc_code, claim_num FROM public.payment_recovery where pmt_num = %s"
PAYMENT_UPDATE_R_QRY="UPDATE public.payments SET pmt_status = %s,reversal_sw = %s WHERE pmt_num = %s"
PAYMENT_UPDATE_RET_QRY="UPDATE public.payments SET pmt_status = %s,return_sw = %s WHERE pmt_num = %s"
PAYMENT_UPDATE_C_QRY="UPDATE public.payments SET pmt_status = %s WHERE pmt_num = %s"
RETURN_NOC_INSERT_QRY ="INSERT INTO public.return_noc(return_noc_code, pmt_num, correction_data, return_noc_timestamp) VALUES (%s, %s, %s, %s)"
RECOVERY_UPDATE_R_QRY ="UPDATE public.payment_recovery SET pmt_recovery_status = %s,return_date=%s,return_code=%s,success_date=null WHERE pmt_num=%s"
RECOVERY_UPDATE_C_QRY ="UPDATE public.payment_recovery SET return_date=%s,return_code=%s WHERE pmt_num=%s"
SELECT_RETURN_NOC_QRY ="SELECT * from public.return_noc where pmt_num=%s"


# queries for the application we are creating

FETCH_USER_CREDENTIALS = """SELECT username, password, active FROM users WHERE username = %s"""
FETCH_USER_PROFILE = """SELECT first_name, last_name, email FROM users WHERE username = %s"""
UPDATE_USER_PROFILE = """UPDATE users SET first_name = %s, last_name = %s, email = %s WHERE username = %s"""
INSERT_USER = """INSERT INTO users (username, email, password, active) VALUES (%s, %s, %s, %s)"""
