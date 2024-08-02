from django.shortcuts import render
from django.http import HttpResponse
from .models import Lugat

# List of translations
translations = [
    ("Book", "Kitob"), ("Table", "Stol"), ("Window", "Oyna"), ("Wall", "Devor"),
    ("Door", "Eshik"), ("City", "Shahar"), ("House", "Uy"), ("Car", "Mashina"),
    ("Teacher", "O'qituvchi"), ("Student", "O'quvchi"), ("School", "Maktab"),
    ("University", "Universitet"), ("Apartment", "Xonadon"), ("Clothes", "Kiyim"),
    ("Hand", "Qo'l"), ("Leg", "Oyoq"), ("Shirt", "Ko'ylak"), ("Hat", "Shapka"),
    ("Glove", "Qo'lqop"), ("Garden", "Bog'"), ("Tree", "Daraxt"), ("Flower", "Gul"),
    ("Fruit", "Meva"), ("Vegetable", "Sabzavot"), ("Meat", "Go'sht"), ("Fish", "Baliq"),
    ("Bread", "Non"), ("Water", "Suv"), ("Milk", "Sut"), ("Cheese", "Pishloq"),
    ("Butter", "Sariyog'"), ("Sugar", "Shakar"), ("Salt", "Tuz"), ("Pepper", "Murch"),
    ("Rice", "Guruch"), ("Soup", "Sho'rva"), ("Breakfast", "Nonushta"),
    ("Lunch", "Tushlik"), ("Dinner", "Kechki ovqat"), ("Coffee", "Qahva"),
    ("Tea", "Choy"), ("Juice", "Sharbat"), ("Friend", "Do'st"), ("Family", "Oila"),
    ("Child", "Bola"), ("Parent", "Ota-ona"), ("Sister", "Opa-singil"),
    ("Brother", "Aka-uka"), ("Grandmother", "Buvijon"), ("Grandfather", "Bobojon"),
    ("House", "Uy"), ("Room", "Xona"), ("Kitchen", "Oshxona"), ("Bathroom", "Vanna"),
    ("Bedroom", "Yotoqxona"), ("Living room", "Mehmonxona"), ("Garage", "Garaj"),
    ("Garden", "Bog'"), ("Library", "Kutubxona"), ("Office", "Ofis"),
    ("Market", "Bozor"), ("Hospital", "Kasalxona"), ("Doctor", "Shifokor"),
    ("Nurse", "Hamshira"), ("Firefighter", "O't o'chiruvchi"), ("Police", "Politsiya"),
    ("Soldier", "Askar"), ("Engineer", "Muhandis"), ("Pilot", "Uchuvchi"),
    ("Artist", "San'atkor"), ("Musician", "Musiqachi"), ("Singer", "Qo'shiqchi"),
    ("Actor", "Aktyor"), ("Writer", "Yozuvchi"), ("Poet", "Shoir"), ("Scientist", "Olim"),
    ("Farmer", "Dehqon"), ("Worker", "Ishchi"), ("Manager", "Menejer"),
    ("Boss", "Boshliq"), ("Cook", "Oshpaz"), ("Baker", "Nonvoy"), ("Tailor", "Tikuvchi"),
    ("Barber", "Soch o'rayotgan"), ("Driver", "Haydovchi"), ("Captain", "Kapitan"),
    ("President", "Prezident"), ("Minister", "Vazir"), ("Judge", "Sudya"),
    ("Lawyer", "Advokat"), ("Principal", "Direktor"), ("Janitor", "Farrosh"),
    ("Guard", "Qo'riqchi"), ("Salesperson", "Sotuvchi"), ("Shop", "Do'kon"),
    ("Customer", "Mijoz")
]

# Save the translations to the database
for english, uzbek in translations:
    Lugat.objects.create(inglizcha=english, uzbekcha=uzbek)

from django.shortcuts import render
from .models import Lugat


def index(request):
    soz = request.GET.get('q', None)
    natija = None

    if soz and soz != '':
        # Check for English to Uzbek translation
        natija_en_uz = Lugat.objects.filter(inglizcha__icontains=soz).all()[:1]
        # Check for Uzbek to English translation
        natija_uz_en = Lugat.objects.filter(uzbekcha__icontains=soz).all()[:1]

        # Combine the results
        if natija_en_uz or natija_uz_en:
            natija = list(natija_en_uz) + list(natija_uz_en)

    return render(request, 'index.html', {'natija': natija})
