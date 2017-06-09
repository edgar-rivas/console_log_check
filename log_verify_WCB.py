import sys
def main():
    file_name = sys.argv[1]
    file  = open(file_name, 'r').read()

    flash = 'flash image complete, ret=0'
    boot  = 'STRF'
    TRsuccess = 'TR69 transferComplete rv=0'
    TRfail1 = 'TR69 transferComplete rv=12'
    TRfail2 = 'send inform fail rv=28'
    TRfail3 = 'Fail to send inform pharse3'
    TRfail4 = 'tr69_retry_fail'
    flashfail = '..HELO'
    trloop = 'tr69_passive_state_func_initiation'
    soapfault = 'SOAP 1.1 fault'
    mocaseed = 'Switching MoCA bonded seed'
    flasherror = 'seqNumber -1'
    qtnreboot = '***qtn_status_monitor detect QTN card reboot and request download image, need reload QTN 5G***'
    fatalsignal = 'fatal signal'

    count1 = file.count(flash)
    count2 = file.count(boot)
    count3 = file.count(TRsuccess)
    count4 = file.count(TRfail1)
    count5 = file.count(TRfail2)
    count6 = file.count(TRfail3)
    count7 = file.count(TRfail4)
    count8 = file.count(flashfail)
    count9 = file.count(trloop)
    count10 = file.count(soapfault)
    count11 = file.count(mocaseed)
    count12 = file.count(flasherror)
    count13 = file.count(qtnreboot)
    count14 = file.count(fatalsignal)

    print 	file_name,'|','\n'			\
		'flash',count1,'|',			\
		'boot',count2,'|',			\
		'TRsuccess',count3,'|',			\
		'TRfail rv=12',count4,'|',		\
		'TRfail rv=28',count5,'|',		\
		'TRfail inform,6hr',count6,'|',		\
		'TR retry',count7,'|',			\
		'Flash fail',count8,'|',		\
		'TR loop',count9,'|',			\
		'Soap fault',count10,'|',		\
		'MoCA Seed switch',count11,'|'		\
		'Flash write error',count12,'|'		\
		'QTN reboot',count13,'\n','|',		\
		'Fatal Signal',count14,'\n'
main()
