import requests as jj_8t
import time as il
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي

print(X+'\n\n## اداة لستخراج الصفحات المؤرشفة ##' )
def rr1():
	try:
		i = input(F+'\n'+'‏‏‏‏‏‏ 𝐢𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 : @𝐣𝐣_𝟖𝐭\n\n{#} ادخل رابط الموقع {#} \n\n‏‏‏⠀')
		a = jj_8t.get(i)
		url = f'http://web.archive.org/cdx/search/cdx?url={i}%2F*&output=text&fl=original&collapse=urlkey&filter=statuscode%3A200'
		r = jj_8t.get(url).text
	except Exception:
		il.sleep(1)
		print(Z+'\n'+'\n[-] الرابط المدخل غير صحيح [-]')
	else:
		print('\n')
		print(A+r),'\n'
		print(F+'[1] حفض الروابط في ملف خارجي')
		print(C+'[2] اعادة تشغيل الاداة')
		print(Z+'[3] الخروج من الاداة')
		ii = input('‏‏‏⠀')
		if ii == '1':
			il.sleep(1)
			Aa = input(C+'\n'+'[~] ادخل اسم الملف [~]' )
			with open(Aa+'.txt','w') as rr:
				rr.write(r)
				il.sleep(1)
				print(F+'\n'+'\nتم حفظ الروابط في ملف :',Aa)
		elif ii == '2':
			il.sleep(1)
			rr1()
		elif ii == '3':
			il.sleep(1)
			print(B+'\n'+'اراك لاحقا')
		else:
			print(Z+'\n'+'[-] لا يوجد خيار هكذا [-]')
rr1()
