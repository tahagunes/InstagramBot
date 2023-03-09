from time import sleep, time  ## Saniye bazlı geciktirme işlemi yapabilmemiz için gereken kütüphane
from selenium.common.exceptions import NoSuchElementException  ## Selenium hata ayıklamaları için gerekli kütüphane
from selenium.webdriver.common.keys import Keys  ## Selenium ile birlikte klavyeyi simüle etmemize yarayan kütüphane
from selenium import webdriver  ## Selenium web driver kütüphanesi

tarayiciDriverKonum = "C:\\Users\\TTahA\\PycharmProjects\\pythonProject\\chromedriver.exe"  ## Web driver konumu

"""
Özellikler
Takip Et
Takipten Çık
Takip Edenler
Takip Ettikleri
Takip Etmeyenler
Profil Analiz
"""


class Instagram:
    def __init__(self, tarayiciKonum, url="", kullaniciAdi="", sifre=""):
        self.tarayici = webdriver.Chrome(executable_path=tarayiciDriverKonum)
        self.url = url
        self.girisurl = "https://www.instagram.com/accounts/login/"
        self.kullaniciAdi = kullaniciAdi
        self.sifre = sifre
        self.girisYapilmismi = False
        self.takiptekiler = []
        self.takiptekilerim = []
        self.takipetmeyenler = []

    def TarayiciAc(self):
        try:
            self.tarayici.get(self.url)
            print("Tarayıcı açıldı.")
            self.tarayici.implicitly_wait(10)
        except:
            print("Tarayıcı açılırken bir sorun ile karşılaşıldı!")

    def TarayiciKapat(self):
        self.tarayici.close()

    def GirisYap(self, url):
        try:
            self.tarayici.get(url)
            self.tarayici.implicitly_wait(2)
            kullaniciAdiInput = self.tarayici.find_element_by_css_selector(
                "input[name='username']")
            sifreInput = self.tarayici.find_element_by_css_selector(
                "input[name='password']")
            girisButon = self.tarayici.find_element_by_xpath(
                "//button[@type='submit']")
            kullaniciAdiInput.send_keys(self.kullaniciAdi)
            sifreInput.send_keys(self.sifre)
            girisButon.click()
            print("Hesaba başarılı bir şekilde giriş yapıldı.")
            self.girisYapilmismi = True
            sleep(10)

        except:
            print("Hesaba giriş yapılırken bir sorun ile karşılaşıldı!")

    def TakipEt(self, kullaniciAdi):
        if self.girisYapilmismi == True:
            try:
                self.tarayici.get(self.url + kullaniciAdi)
                self.tarayici.implicitly_wait(2)
                takipEtButton = self.tarayici.find_element_by_tag_name("button")
                if (takipEtButton.text == "Follow") or (takipEtButton.text == "Takip et"):
                    takipEtButton.click()
                    print(kullaniciAdi + " Takip edildi")
                else:
                    print(kullaniciAdi + " Zaten takip ediliyor..")

            except:
                print(kullaniciAdi + " Takip edilirken bir hata ile karşılaşıldı!")
        else:
            print("Lütfen birini takip etmek için önce bir hesap ile giriş yapın!")

    def TakiptenCik(self, kullaniciAdi):
        self.tarayici.get("https://instagram.com/" + kullaniciAdi)
        self.tarayici.implicitly_wait(5)

        self.follow_button = self.tarayici.find_element_by_tag_name("button")
        if self.follow_button.text == "Following":
            self.follow_button.click()
            self.tarayici.implicitly_wait(5)

            self.tarayici.find_element_by_xpath('//button[text()="Unfollow"]').click()
            print(f"Artık {kullaniciAdi}'i takip etmiyorsunuz.")
        else:
            print("Zaten takip etmiyorsunuz.")
    def ProfilAnaliz(self, kullaniciAdi):
        try:
            self.tarayici.get(self.url + kullaniciAdi)
            self.tarayici.implicitly_wait(2)
            gonderiSayisi = self.tarayici.find_element_by_xpath(
                '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[1]/div/span')
            takipciSayisi = self.tarayici.find_element_by_xpath(
                '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/div/span')
            takipEdilenSayisi = self.tarayici.find_element_by_xpath(
                '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a/div/span')
            print(
                "Hesap : " + kullaniciAdi+"\nGönderi sayısı : " + gonderiSayisi.text + "\nTakipci sayısı : " + takipciSayisi.text + "\nTakip edilen sayısı : " + takipEdilenSayisi.text)
        except:
            print(kullaniciAdi +
                  " Profili analiz edilirken bir sorun ile karşılaşıldı!")

    def GTengel(self,kullaniciAdi):
        self.tarayici.get("https://www.instagram.com/" + kullaniciAdi)
        sleep(2)
        try:
            followbutton = self.tarayici.find_element_by_xpath(
                '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div/button').click()
            sleep(2)
            confirmbutton = self.tarayici.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[1]').click()
            sleep(2)
            lastconfirmbutton = self.tarayici.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[1]')
            if lastconfirmbutton.text == "Block" or lastconfirmbutton.text == "Engelle":
                lastconfirmbutton.click()
                sleep(2)
                print(kullaniciAdi+" başarıyla engellendi.")
            else:
                print("Kullanıcı zaten engelli.")
        except:
            print("Kullanıcı zaten engelli.")

    def GTengel2(self):
        for engellenecek in self.takipetmeyenler:
            self.tarayici.get("https://www.instagram.com/" + engellenecek)
            sleep(2)
            try:
                followbutton = self.tarayici.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div/button').click()
                sleep(2)
                confirmbutton = self.tarayici.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[1]').click()
                sleep(2)
                lastconfirmbutton = self.tarayici.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[1]')
                if lastconfirmbutton.text == "Block" or lastconfirmbutton.text == "Engelle":
                    lastconfirmbutton.click()
                    sleep(2)
                    print(engellenecek + " başarıyla engellendi.")
                else:
                    print("Kullanıcı zaten engelli.")
            except:
                print("Kullanıcı zaten engelli.")

    def HesapGizlimi(self, kullaniciAdi):
        try:
            self.tarayici.get(self.url + kullaniciAdi)
            self.tarayici.implicitly_wait(10)
            hesapGizlimi = self.tarayici.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/div/article/div/div/h2')
            if hesapGizlimi.text == "Bu Hesap Gizli":
                return True
            else:
                return False
        except NoSuchElementException:
            return False
        else:
            print("Hesap gizlimi kontrol edilirken bir sorun ile karşılaşıldı!")

    def TakipEdenleriGoster(self, kullaniciAdi, gosterGizle=False):

        if self.HesapGizlimi(kullaniciAdi):
            print("Hesap gizli olduğu için takip edenleri göremiyorum!")
        else:
            self.tarayici.get(self.url + kullaniciAdi)
            self.tarayici.implicitly_wait(2)
            takipEdenlerLink = self.tarayici.find_element_by_xpath(
                "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/div/span").click()
            sleep(5)

            jsKomut = """
            		sayfa = document.querySelector("._aano");
            		sayfa.scrollTo(0,sayfa.scrollHeight);
            		var sayfaSonu = sayfa.scrollHeight;
            		return sayfaSonu;
            		"""
            sayfaSonu = self.tarayici.execute_script(jsKomut)
            while True:
                son = sayfaSonu
                sleep(2)
                sayfaSonu = self.tarayici.execute_script(jsKomut)
                if son == sayfaSonu:
                    break

            pencere = self.tarayici.find_elements_by_css_selector(
                ".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.notranslate._a6hd")
            sayac = 0
            for takipci in pencere:
                sayac += 1
                self.takiptekiler.append(takipci.text)
            print("Şu anda " + str(sayac) + " takip edeniniz var.")

    def TakipEttikleriniGoster(self, kullaniciAdi, gosterGizle=False):

        if self.HesapGizlimi(kullaniciAdi):
            print("Hesap gizli olduğu için takip edenleri göremiyorum!")
        else:
            self.tarayici.get(self.url + kullaniciAdi)
            self.tarayici.implicitly_wait(2)
            takipEdilenlerLink = self.tarayici.find_element_by_xpath(
                "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a/div/span").click()
            sleep(5)

            jsKomut = """
            		sayfa = document.querySelector("._aano");
            		sayfa.scrollTo(0,sayfa.scrollHeight);
            		var sayfaSonu = sayfa.scrollHeight;
            		return sayfaSonu;
            		"""
            sayfaSonu = self.tarayici.execute_script(jsKomut)
            while True:
                son = sayfaSonu
                sleep(2)
                sayfaSonu = self.tarayici.execute_script(jsKomut)
                if son == sayfaSonu:
                    break

            pencere = self.tarayici.find_elements_by_css_selector(
                ".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.notranslate._a6hd")
            sayac = 0
            for takipci in pencere:
                sayac += 1
                self.takiptekilerim.append(takipci.text)
            print("Şu anda " + str(sayac) + " takip ettiğiniz var.")

    def TakipEtmeyenler(self):
        sayac = 0
        if len(self.takiptekilerim) != 0 and len(self.takiptekiler) != 0:
            print("Geri Takip Etmeyenler")
            for takipEdilenler in self.takiptekilerim:
                if takipEdilenler not in self.takiptekiler:
                    sayac += 1
                    print(str(sayac) + " " + takipEdilenler)
                    self.takipetmeyenler.append(takipEdilenler)
        else:
            print("Lütfen ilk olarak takipcileri ve takip edilenleri gösterin!")


Ins = Instagram(tarayiciDriverKonum, "https://instagram.com/", "yldrmrve35", "1234qwer")
Ins.TarayiciAc()
Ins.GirisYap("https://www.instagram.com/accounts/login/")
#Ins.ProfilAnaliz("yldrmrve35")
Ins.TakipEdenleriGoster("selcansacilik", True)
Ins.TakipEttikleriniGoster("selcansacilik", True)
Ins.TakipEtmeyenler()
#Ins.TakipEt("tahaguunes")
#Ins.TakiptenCik("tahaguunes")
#Ins.GTengel("tahaguunes")
#Ins.GTengel2()
print("mutlu son")
#Ins.TarayiciKapat()
print(input())