##프린트 서식##
print("안녕하세요?")#문자열

print("100")#문자열(숫자)
print("%d"%100)#서식-정수형#d
print('%f'%100)#서식-실수형#f
print('%d %f %x'%(100,100,100))#서식 갯수와 숫자의 갯수가 동일 해야 실행가능.

print("%d"%(100+100))

##서식출력 연습
print('%d'%123)
print('%5d'%123)#5자리로 출력,오른쪽에 붙여서 출력
print('%05d'%123)#5자리로 출력,빈칸을 0으로 채움

print('%f'%123.45)#소수점6자리까지 출력
print('%7.1f'%123.45)#소수점 첫째 자리만 출력(소수점 둘째자리에서 반올림)
print('%7.3f'%123.45)#소수점 셋째자리 까지 출력(빈칸은 0으로 채움)
print('%07.1f'%123.45)


print('%s'%"Python")#자리수만큼 출력
print('%10s'%"Python")#10자리 확보, 오른쪽 정렬

#format()함수의 사용
print('%d %f %x'%(100,100,100)) #''사이에 문자열 추가 가능
print('{0:d} {1:f} {2:x}'.format(100,100,100))

#이스케이프 문자
print('문장입니다. 다음 문장입니다')
print('문장입니다. \n 다음 문장입니다.')#새로운 줄로 이동

print('문장입니다. 다음 문장입니다')
print('문장입니다. \t 다음 문장입니다.')#tap을 누른 효과

print('문장입니다. 다음 문장입니다')
print('문장입니다. \b 다음 문장입니다.')#back space를 누른 효과

print('강조입니다. \"강조\" 문장입니다')#\"강조\"되는 효과 - \' > '를 출력
print('강조입니다. \'강조\' 문장입니다')#\'강조\'되는 효과   - \" > "를 출력

print("\\\\\\") #\\\가 출력
print(r' \n \t \' \\ 를 그대로 출력')#r - '안에 모든걸 문자(이스케이프문자 등)로 인식'
print(' \n \t \' \\ 를 그대로 출력')#비교.
print(r' \'\n\'보고싶습니다 ')
print("\'" r"\n\t보고싶습니다.""\'")

