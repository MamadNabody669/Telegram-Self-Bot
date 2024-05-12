from telethon import TelegramClient,events,types
from telethon.tl.custom.message import Message
import colorama
from colorama import Back , Fore
import time
import SetApi


colorama.init(autoreset=True)

RavaniMode = "OffMot"
ADsTab = "OffFel"
AdsMIKH = "KO0"
canNext11 = "kh"
cannext2 = "Bakhi"
FohshSpeed = "DOntValue"
shomareshFast = "DontGetValue"
Atacker = "MIDVALUE"
#print(Fore.YELLOW+"dar sorati ke api_id va api_hash khod ra Set nakardid ==>  python SetApi.py ra vard konid")

ChanellTabAds = "سلام رفیق ممنون میشم توی چنلم جوین بدی @orginalGifTelgram"
Client = TelegramClient('MamadNabody',api_hash=SetApi.apiHash ,  api_id= SetApi.apiid)

@Client.on(events.NewMessage())
async def main(event : Message):

        if(event.text == "info"):
         await event.respond("SalamRefigh\nYour id==>"+str(event.chat_id)+"\nYour peer id ==>"+str(event.peer_id)+"\nCoded By @MamadNabody6", reply_to=event.id)


@Client.on(events.NewMessage(outgoing=True))
async def main(event : Message):
     global RavaniMode
     Creator = "Coded By MamadNabody6"
     Fohsh = "کیر تو کص مادرت"
     if(event.text=="سازنده"):
      await event.edit("Coded")
      await event.edit("Coded by")
      await event.edit("Coded by @MamadNabody6")
     elif event.text == "1":
         await event.edit(Fohsh)
     elif event.text == "روانی":
         await event.edit("حالت روانی مود فعال شد\nCoded By @MamadNabody6")
         RavaniMode = "ok"
         print(Fore.GREEN+"Ravani Mode : "+str(RavaniMode))
          

     elif event.text=="off":
         await event.edit("روانی مود غیر فعال شد\nCoded By @MamadNabody6")
         RavaniMode = "no"
     elif event.text == "وضعیت روانی مود":
          await event.edit("RavaniMode = "+str(RavaniMode))

     elif RavaniMode == "ok" :
         @Client.on(events.NewMessage())
         async def main(event : Message):
             if(RavaniMode=="ok"):
              await event.respond("روانی شدم حروم زاده هاهاها", reply_to=event.id)
             else :
                 dontwork = "kosmos"
     elif  event.text =="help":
        await event.edit("به سلف تلگرام خوش آمدید این سلف آپدیت  خواهد شد\n"+"\n"+"برای فعال سازی حالت روانی مود کلمه روانی را وارد کنید\n\n"+"برای غیر فعال کردن روانی مود کلمه off را وارد کنید\n\n"+"برای افزودن لینک تبلیغات ابتدا کلبه تبلیغ جدید را وارد کنید سپس لینک خود را وارد کنید\n\n" + "برای فعال کردن اسپید فحش کلمه فحش اسپید را وارد کنید در صورت فعال بودن این قابلیت با ریپلای زدن روی تارگت و نوشتن عدد 0 ده فحش به اون ریپلای خواهد شد" +"\n\n"+"برای خاموش کردن فحش اسپید کلمه  offs وارد کنید"+"\n\n"+"برای تبدیل متن به استیکر ابتدا روی نتن مورد نظر ریپلای کرده سپس کلمه تبدیل متن به استیکر را وارد کنید"+"برای دیدن اسم سازنده کلمه سازنده را وارد کنید"+"\n\n"+"\n\n"+"هر مشکل یا ایده ای داشتید به ایدی زیر پیام دهید"+"\n\n"+"با نوشتن کلمه قلب  پبام شما ادیت میخورد و قلب نمایش داده میشود"+"\n\n"+"برای پین سریع ابتدا روی پیام مورد نظر ریپلای کنید سپس کلمه پ را بنویسید"+"\n\n"+"برای دیداس زدن به مدریت گروه کلمه اسپم مدریت را وارد کنید هشدار در حد امکان از این ثابلیت ساتفاده نکنید"+"\n\n\n"+"@MamadNabody6")
     elif event.text =="اسپم مدیریت":
         await event.edit("دیداس به گروه آغاز گشت")
         
         await event.edit("123🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos7rereretythgfds87it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it🌀2")
         await event.edit("12423🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀morereres787it3🚨")
         await event.edit("13🌀423🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀rereremos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos7867it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it564🚨3")
         await event.edit("13423🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mosre787it23🌀3💯4💥465re🌀mos787it23🌀3💯4💥re🌀mos7876it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it56u💥🚨6y")
         await event.edit("dt🌀23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥r64🌀mos78erererererer7it23🌀3💯4💥re🌀mos7867it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787itjygg🚨ed")
         await event.edit("dfg23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos7ere87it23🌀3💯4💥re🌀mos787werererereit23🌀3💯4💥re🌀mos7867it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787itjkjl🚨kioiu")
         await event.edit("rr23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mosrer787it23🌀3💯4💥rererereedfgyjhgfd4345we444343🌀mos787it23🌀3💯4💥re🌀mos7876it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it🌀gt87it")
         await event.edit("r4f23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787iterere23🌀3💯4erer💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787it23🌀3💯4💥re🌀mos787itdff🚨dfdf6787it")
         await event.edit("23🌀4we🚨3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀3🌀3💯4💥re🌀wewe🌀wew87it")
         await event.edit("r42v🚨3we💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435r7💥it")
         await event.edit("r456rr💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435g💥re🚨w7it")
         await event.edit("23🚨💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥34remos787it")
         await event.edit("2323kos🚨💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥12122🌀1212🌀4r3432e💯2324💥3435it")
         await event.edit("23m💯me💥7it")
         await event.edit("r4koooos7i💥💥12122🌀1212🌀4r3432e💯2324💥3435t")
         await event.edit("r45k💯iii🌀rit")
         await event.edit("r412💯💥💥12122🌀1212🌀4r3432e💯2324💥34351212123237it")
         await event.edit("23💥💥12122🌀1212🌀4r3432e💯2324💥34352re451223🌀237it")
         await event.edit("rgdw🌀ds💥dfdssdsd")
         await event.edit("dsds💥ds💥💥12122🌀1212🌀4r3432e💯2324💥3435dsdd💯45123237it")
         await event.edit("sdsds💯d💥💥12122🌀1212🌀4r3432e💯2324💥3435sds213237it")
         await event.edit("rrgt87it")
         await event.edit("r4f💯dffd💥💥12122🌀1212🌀4r3432e💯2324💥3435f💥df6787it")
         await event.edit("234w🌀ewewewew💯87it")
         await event.edit("r423we💥💥12122🌀1212🌀4r3432e💯2324💥3435r💥💥12122🌀1212🌀4r3432e💯2324💥34357💥it🌀")
         await event.edit("r45🌀6rr💥grew7it")
         await event.edit("2334💥re💯mos787it")
         await event.edit("2323kosit")
         await event.edit("23💥mame💥💥7it")
         await event.edit("r4k💯💥💥121💥💥12122🌀1212🌀4r3432e💯2324💥343522🌀1212🌀4r3432e💯2324💥3435oo💥💥oos7it")
         await event.edit("r45k🌀ii💥💥irit")
         await event.edit("rrgt87it")
         await event.edit("r4fd🌀ff💯dfdf67💯87it")
         await event.edit("234we💥💥💥wewewew87it")
         await event.edit("r42💯3wer💥7it")
         await event.edit("r456rr🌀grew7💯it💥")
         await event.edit("2🌀32🌀334rem💯os💥787it2🌀c4rem💯os💥787its💥787its💥787it")
         await event.edit("2323ko💯si💥t")
         await event.edit("r💯💯456r💥rgrew7it")
         await event.edit("2🌀34remo💥s💯787it")
         await event.edit("2323💯kosit")
         await event.edit("23💯💥m💥💥12122🌀1212🌀4r3432e💯2324💥3435ame💥7it")
         await event.edit("r4fdffdfd💥f6💯787it")
         await event.edit("234w💯ewe💥wewew87it")
         await event.edit("r423wer7💥it")
         await event.edit("r456💯r💯rgr🌀ew7it")
         await event.edit("23🌀3💯4💥re🌀mos787it")
         await event.edit("2323kos💥it")
         await event.edit("23m💯a💥m💯e7it")
         await event.edit("r4🌀kooo💥💥12122🌀1212🌀4r3432e💯2324💥3435💥os7it")
         await event.edit("r4🌀5kiiir💥it")
         await event.edit("2334💥re💯mos787it")
         await event.edit("2323kosit")
         await event.edit("23💥mame💥💥7it")
         await event.edit("r4k💯oo💥💥12122🌀1212🌀4r3432e💯2324💥3435💥💥oos7it")
         await event.edit("r45k🌀ii💥💥irit")
         await event.edit("rrgt87it")
         await event.edit("r4fd🌀ff💯dfdf67💯87it")
         await event.edit("234we💥💥💥💥12122🌀1212🌀4r3432e💯2324💥3435💥wewewew87it")
         await event.edit("r42💯3werv💥💥12122🌀1212🌀4r3432e💯2324💥3435💥7it")
         await event.edit("r456rr🌀💥💥12122🌀1212🌀4r3432e💯2324💥3435grew7💯it💥")
         await event.edit("2🌀334rem💯os💥787it")
         await event.edit("232💥💥12122🌀1212🌀4r3432e💯2324💥34353ko💯si💥t")
         await event.edit("r💥💥12122🌀1212🌀4r3432e💯2324💥3435💯💯456r💥rgrew7it")
         await event.edit("2🌀34remo💥s💯787it")
         await event.edit("2323💯kosit")
         await event.edit("23💯💥mame💥7it")
         await event.edit("r4fdffdfd💥f6💯787it")
         await event.edit("234w💯ewe💥wewew87it")
         await event.edit("r423wer7💥it")
         await event.edit("r456💯r💯rgr🌀ew7it")
         await event.edit("23🌀3💯4💥re🌀mos787it")
        
         await event.edit("2334💥💥💥12122🌀1212🌀4r3432e💯2324💥3435re💯mos787it")
         await event.edit("2323kosit")
         await event.edit("23💥mame💥💥7it")
         await event.edit("r4k💯oo💥💥oos7it")
         await event.edit("r45k🌀ii💥💥irit")
         await event.edit("rrgt87it")
         await event.edit("r4fd🌀ff💯dfdf67💯87it")
         await event.edit("234we💥💥💥wewewew87it")
         await event.edit("r42💯3wer💥7it")
         await event.edit("r456rr🌀grew7💯it💥")
         await event.edit("2🌀334rem💯os💥787it")
         await event.edit("2323ko💯si💥t")
         await event.edit("r💯💯456r💥rgrew7it")
         await event.edit("2🌀34remo💥s💯787it")
         await event.edit("2323💯kosit")
         await event.edit("23💯💥mame💥7it")
         await event.edit("r4fdffdfd💥f6💯787it")
         await event.edit("234w💯ewe💥wewew87it")
         await event.edit("r423wer7💥it")
         await event.edit("r456💯r💯rgr🌀ew7it")
         await event.edit("23🌀3💯4💥re🌀mos787it")

         



@Client.on(events.NewMessage(outgoing=True))
async def main(event : Message):
    global ADsTab
    global ChanellTabAds
    global AdsMIKH
    if(event.text == "تبلیغ جدید" ):
        await event.edit("متن تبلیغ خود را وارد کنید")
        AdsMIKH = "can"
    elif(AdsMIKH == "can"):
        ChanellTabAds = event.text
        print(Fore.MAGENTA+"seted Description  : "+str(ChanellTabAds))
        AdsMIKH = "donCan"
        await event.edit("لینک جدید ست شد")

    elif(event.text == "تبلیغ"):
       
        
         await event.respond("حالت تبلیغ مود فعال شد\nCoded By @MamadNabody6")
         ADsTab = "ok"
         print(Fore.YELLOW+"TabloghMode : On ")
    elif(event.text == "offt"):
        await event.respond("حالت تبلیغ مود غیر فعال شد\nCoded By @MamadNabody6")
        ADsTab = "no"
        print(Fore.BLUE+"TablighMode : Off")
    
    elif event.text == "قلب":
        await event.edit("ممنون❤️")
        await event.edit("ممنون🧡❤️")
        await event.edit("ممنون❤️💛🧡")
        await event.edit("ممنون💚🧡💛❤️")
        await event.edit("ممنون💛💙🧡❤️")
        await event.edit("ممنون🧡💛❤️🖤💙")
        await event.edit("ممنون🤍🖤💙💛🧡❤️")
        heart = "🧡💛💚💙💙🖤🤍"
    elif event.text == "پ":
        rep = await event.get_reply_message()
        message = rep
        await Client.pin_message(event.chat_id, message, notify=True)
        
        await event.edit("پین شد")

@Client.on(events.NewMessage())
async def main(event : Message):
    global ADsTab
    if(ADsTab=="ok"):
        await event.respond(str(ChanellTabAds),reply_to=event.id)
        if(ADsTab=="no"):
            print(Fore.LIGHTBLUE_EX+"offTB")
    
    if(event.text=="تبدیل متن به استیکر"):
     chat = await event.get_chat()
     reply_11 = await event.get_reply_message()
     forwardiSe = await reply_11.forward_to('@QuotLyBot')
     async with Client.conversation('@QuotLyBot') as conv:
      xx = await conv.get_response(reply_11.id)
      await Client.send_message(chat,xx)
@Client.on(events.NewMessage(outgoing=True))
async def main(event : Message):
    global canNext11
    global cannext2
    if(event.text == "گیف ساز"):
        chat1 = await event.get_chat()
        reply_111 = await event.get_reply_message()
        forwardiSe = await reply_111.forward_to('@itgifbot')
        async with Client.conversation('@itgifbot') as conv:
            xxx = await conv.get_response(reply_111.id)
            await Client.send_message(chat1,xxx)
            event.edit("متن خود را  وارد کنید")
            canNext11="ok"
    elif canNext11 == "ok":
        event.edit("روی متن خود ریپلای کنید")
        
        chat1 = await event.get_chat()
        reply_111 = await event.get_reply_message()
        forwardiSe = await reply_111.forward_to('@itgifbot')
        async with Client.conversation('@itgifbot') as conv:
            xxx = await conv.get_response(reply_111.id)
            await Client.send_message(chat1,xxx)
            await Client.send_message(chat1,message="بروید @itgifbot  گیف شما ساخته شد جها مشاهده گیف به ")
        
            canNext11 = "klll"

    

@Client.on(events.NewMessage())
async def main(event : Message):      
    if(event.text == "ویکی"):
        chat1 = await event.get_chat()
        reply_111 = await event.get_reply_message()
        forwardiSe = await reply_111.forward_to('@GPT4Telegrambot')
        async with Client.conversation('@GPT4Telegrambot') as conv:
            xxx = await conv.get_response(reply_111.id)
            await Client.send_message(chat1,xxx)
            time.sleep(10)
            xxx1 = await conv.get_response()
            await Client.send_message(chat1,xxx)
    

@Client.on(events.NewMessage())
async def main(event : Message):
    global FohshSpeed
    if(event.text == "فحش سریع"):
        await event.edit("فحش سریع فعال شد"+"\n\n"+"با فعال شدن این فابلیت  با هر ریپلای شما روی تارگت ده فحش به  او ریپلای خواهد شد"+"\n\n"+"Coded By @MamadNabody6")
        FohshSpeed = "ok"
        print(Fore.GREEN+"FoshSpeed : on")
    elif(event.text == "offs"):
        await event.edit("فحش سریع خاموش شد"+"\n\n\n\n\n"+"Coded By @MamadNabody6")
        FohshSpeed = "no"
        print(Fore.RED+"FoshSpeed : off")
@Client.on(events.NewMessage(outgoing=True))
async def main(event : Message):
    global FohshSpeed
    
    if(FohshSpeed=="ok" and event.text=="0"):
        replyMSG = await event.get_reply_message()
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="کیر بر کص دالگت")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="مادر جنده")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="حروم زاده")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="پام تو کون مادرت")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="کون باباتو کردم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="خارتو گاییدم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="آب کص مادرتو خوردم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="پدرت شدم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="مادرتو حامله کردم")
        if(FohshSpeed == "no"):
            print("dead shodom!")
    
@Client.on(events.NewMessage())
async def main(event : Message):
    global shomareshFast
    if(event.text == "شمارش"):
        await event.edit("شمارش فعال شد"+"\n\n"+"با فعال کردن این قابلیت با هر ریپلای تارگت ریپلای خواهد خورد"+"\n\n"+"Coded By @MamadNabody6")
        shomareshFast = "ok"
        print(Fore.CYAN+"Shomaresh Speed : on")
    elif(event.text == "offshh"):
        await event.edit("فحش سریع خاموش شد"+"\n\n\n\n\n"+"Coded By @MamadNabody6")
        shomareshFast = "no"
        print(Fore.LIGHTYELLOW_EX+"Shomaresh Speed : off")
@Client.on(events.NewMessage(outgoing=True))
async def main(event : Message):
    global FohshSpeed
    if(shomareshFast=="ok" and event.text=="2"):
        replyMSG = await event.get_reply_message()
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="0")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="1")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="2")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="3")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="4")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="5")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="6")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="7")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="8")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="9")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="10")
       

        if(shomareshFast == "no"):
            print("dead shodom!")

#Attacker
@Client.on(events.NewMessage())
async def main(event : Message):
    global Atacker
    if(event.text == "ران اتکر"):
        await event.edit("اتکر روشن شد"+"\n\n"+"Coded By @MamadNabody6")
        Atacker = "ok"
        print(Fore.LIGHTBLACK_EX+"attacker : on")
    elif(event.text == "offa"):
        await event.edit("اتکر خاموش شد"+"\n\n\n\n\n"+"Coded By @MamadNabody6")
        Atacker = "no"
        print(Fore.MAGENTA+"attacker : off")
@Client.on(events.NewMessage(outgoing=True))
async def main(event : Message):
    global Atacker
    if(Atacker=="ok" and event.text=="00"):
        replyMSG = await event.get_reply_message()
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="کیر بر کص دالگت")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="مادر جنده")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="حروم زاده")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="پام تو کون مادرت")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="کون باباتو کردم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="خارتو گاییدم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="آب کص مادرتو خوردم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="پدرت شدم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="مادرتو حامله کردم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="ببین مادر جنده هر جای دنیا که باشی پیدات میکنم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="برج میلاد توی کص مادرت")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="حروم زاده")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="پام تو کون مادرت")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="کون باباتو کردم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="خارتو گاییدم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="آب کص مادرتو خوردم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="شاشیدم دهن مادرت")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="برج میلاد توی کص مادرت")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="حروم زاده")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="پام تو کون مادرت")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="کون باباتو کردم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="خارتو گاییدم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="آب کص مادرتو خوردم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="با کیر مادرتو کشتم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="کیر بر کص دالگت")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="مادر جنده")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="حروم زاده")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="پام تو کون مادرت")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="کون باباتو کردم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="خارتو گاییدم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="آب کص مادرتو خوردم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="پدرت شدم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="مادرتو حامله کردم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="ببین مادر جنده هر جای دنیا که باشی پیدات میکنم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="برج میلاد توی کص مادرت")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="حروم زاده")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="پام تو کون مادرت")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="کون باباتو کردم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="خارتو گاییدم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="آب کص مادرتو خوردم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="شاشیدم دهن مادرت")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="برج میلاد توی کص مادرت")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="حروم زاده")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="پام تو کون مادرت")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="کون باباتو کردم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="خارتو گاییدم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="آب کص مادرتو خوردم")
        await Client.send_message(entity=event.chat_id,reply_to=replyMSG,message="با کیر مادرتو کشتم")
        if(Atacker == "no"):
            print("dead shodom!")






#------------------------------|+|            
#Coded-By-MamadNabody6---------|+|
#Telegram ID-=>-@Mamadnabody6--|+|
print(Fore.GREEN+"Self Is Runned!\n")
time.sleep(1)
print(Fore.GREEN+"Trun On Your Vpn\n")
time.sleep(1)
print(Fore.GREEN+"type/help in save message\n")
time.sleep(1)
print(Fore.GREEN+"Telegram ID -> @MamadNabody6\n")



Client.start()
Client.run_until_disconnected()
