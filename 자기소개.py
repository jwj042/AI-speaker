# 인공지능 기사(TTS)
from datetime import datetime
import random

#아이엠 그라운드 자기소개 하기
name = input("당신의 이름은 무엇인가용? ")
age = input("당신의 나이는 몇살입니까? ")
favorite = input("당신이 가장 좋아하는것이 몹니까? ")
hobby = input("당신의 취미는 몹니까?")
dream = input("당신의 꿈은 무엇을 헝성하고있씁니까? ")
girlfriend = input("당신은 여자친구가 있습니까? ")
weight = input("혹시 몇 kg입니까? ")

#자기소개 하는 곳
news ="정상수의 자기소개를 하겠씁니다."
news = news + "저는  " + name + "그리고 "+ age +"입니다."
news = news + "저는 " + favorite + " 입니다."
news = news +"저의 취미는 " + hobby + "입니다."
news = news+ "저의 꿈은 "+ dream + "입니다."  
news = news+ "저는 여자친구가"+ girlfriend + "."
news = news+ " 저는 "+weight+"입니다"
    
 #음성으로 들려주는 곳
from gtts import gTTS
import playsound
import os #파일관리 함수
 
tts=gTTS(text=news,lang='ko')
tts.save("정상수의 자기소게.mp3") #기존에 같은 이름의 파일이 존재하면 에러가 생김
playsound.playsound("정상수의 자기소개.mp3",False) #True 멈춰서 해당 하나만 재생, False 밑에 코드랑 동시재생(배경음악)
playsound.playsound("THURSDAY MORNING CHILL JAZZ Sweet March Morning - Spring Jazz &amp Bossa Nova for Good Mood.mp3",True)
os.remove("정상수의 자기소개.mp3")
os.remove("THURSDAY MORNING CHILL JAZZ Sweet March Morning - Spring Jazz &amp Bossa Nova for Good Mood.mp3")
print(news)