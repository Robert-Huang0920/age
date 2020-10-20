driving = input('請問您有無開過車？')
if driving != '有' and driving != '沒有' and driving != 'yes' and driving != 'no':
	print('請輸入 有 / 沒有')
	raise SystemExit
age = input('請問您的年齡？')
age = int(age)
if driving == '有' or driving == 'yes':
	if age >= 18:
		print('恭喜您通過測驗')
	else:
		print('奇怪 你怎麼會開過車Ｏ。Ｏ')
elif driving == '沒有' or driving == 'no':
	if age >= 18:
		print('請去學開車')	
	else:
		print('等你長大就可以開惹')