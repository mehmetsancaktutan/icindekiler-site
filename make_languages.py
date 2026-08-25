import os
import shutil

translations = {
    "en": {
        "Ürünün içinde ne var, saniyeler içinde gör.": "See what's inside in seconds.",
        "Uygulama ne yapar": "What the app does",
        "Gıda ve kozmetik ürünlerinin fotoğrafını çekersin": "Take photos of food and cosmetic products",
        "İçerik listesini analiz eder, anlaşılır bir puana dönüştürür": "Analyzes the ingredient list and converts it into a clear score",
        "Katkı maddelerini, şeker, tuz, yağ ve besin değerlerini sade bir dille açıklar": "Explains additives, sugar, salt, fat, and nutritional values simply",
        "Kaydettiğin alerjen ve diyet tercihlerine göre sana uygun olmayan üründe uyarır": "Warns you about unsuitable products based on your saved allergen and diet preferences",
        "Taradığın ürünleri geçmişte tutar, favorilerine ekleyebilirsin": "Keeps your scanned products in history, you can add to favorites",
        "Veri yaklaşımı": "Data approach",
        "Hesap yok.": "No account.",
        "Kayıt olmadan, giriş yapmadan kullanılır.": "Use without registering or logging in.",
        "Tercihlerin, geçmişin ve favorilerin <strong>cihazında</strong> saklanır.": "Your preferences, history, and favorites are stored <strong>on your device</strong>.",
        "Ürün analizi için fotoğraf ve ürün bilgisi analiz servisine gönderilir.": "Photos and product info are sent to the analysis service for product analysis.",
        "Reklam yok, kullanıcı takibi yok.": "No ads, no user tracking.",
        "Gizlilik politikasının tamamı →": "Full privacy policy →",
        "Yuppa tıbbi bir cihaz değildir; hastalık teşhis etmez, tedavi etmez, iyileştirmez": "Yuppa is not a medical device; it does not diagnose, treat, cure",
        "veya önlemez. Sağlığınızla ilgili kararlar için bir uzmana danışın.": "or prevent any disease. Consult a specialist for health decisions.",
        "Gizlilik Politikası": "Privacy Policy",
        "Kullanım Koşulları": "Terms of Use",
        "Destek": "Support",
        "Ürün Analizi": "Product Analysis",
        "lang=\"tr\"": "lang=\"en\"",
        "logo.png": "../logo.png"
    },
    "de": {
        "Ürünün içinde ne var, saniyeler içinde gör.": "Sieh in Sekunden, was drin ist.",
        "Uygulama ne yapar": "Was die App macht",
        "Gıda ve kozmetik ürünlerinin fotoğrafını çekersin": "Mache Fotos von Lebensmitteln und Kosmetika",
        "İçerik listesini analiz eder, anlaşılır bir puana dönüştürür": "Analysiert die Zutatenliste und wandelt sie in eine klare Bewertung um",
        "Katkı maddelerini, şeker, tuz, yağ ve besin değerlerini sade bir dille açıklar": "Erklärt Zusatzstoffe, Zucker, Salz, Fett und Nährwerte einfach",
        "Kaydettiğin alerjen ve diyet tercihlerine göre sana uygun olmayan üründe uyarır": "Warnt vor ungeeigneten Produkten basierend auf deinen Allergen- und Diät-Präferenzen",
        "Taradığın ürünleri geçmişte tutar, favorilerine ekleyebilirsin": "Speichert deine gescannten Produkte im Verlauf, du kannst sie zu Favoriten hinzufügen",
        "Veri yaklaşımı": "Datenschutz",
        "Hesap yok.": "Kein Account.",
        "Kayıt olmadan, giriş yapmadan kullanılır.": "Ohne Registrierung oder Login nutzen.",
        "Tercihlerin, geçmişin ve favorilerin <strong>cihazında</strong> saklanır.": "Deine Präferenzen, Verlauf und Favoriten werden <strong>auf dem Gerät</strong> gespeichert.",
        "Ürün analizi için fotoğraf ve ürün bilgisi analiz servisine gönderilir.": "Fotos und Produktinfos werden zur Analyse an den Dienst gesendet.",
        "Reklam yok, kullanıcı takibi yok.": "Keine Werbung, kein Tracking.",
        "Gizlilik politikasının tamamı →": "Vollständige Datenschutzerklärung →",
        "Yuppa tıbbi bir cihaz değildir; hastalık teşhis etmez, tedavi etmez, iyileştirmez": "Yuppa ist kein Medizinprodukt; es diagnostiziert, behandelt oder heilt",
        "veya önlemez. Sağlığınızla ilgili kararlar için bir uzmana danışın.": "keine Krankheiten. Konsultiere für Gesundheitsentscheidungen einen Experten.",
        "Gizlilik Politikası": "Datenschutzerklärung",
        "Kullanım Koşulları": "Nutzungsbedingungen",
        "Destek": "Support",
        "Ürün Analizi": "Produktanalyse",
        "lang=\"tr\"": "lang=\"de\"",
        "logo.png": "../logo.png"
    },
    "fr": {
        "Ürünün içinde ne var, saniyeler içinde gör.": "Découvrez ce qu'il y a à l'intérieur en quelques secondes.",
        "Uygulama ne yapar": "Ce que fait l'application",
        "Gıda ve kozmetik ürünlerinin fotoğrafını çekersin": "Prenez des photos de produits alimentaires et cosmétiques",
        "İçerik listesini analiz eder, anlaşılır bir puana dönüştürür": "Analyse la liste des ingrédients et la convertit en un score clair",
        "Katkı maddelerini, şeker, tuz, yağ ve besin değerlerini sade bir dille açıklar": "Explique simplement les additifs, le sucre, le sel, les graisses et les valeurs nutritionnelles",
        "Kaydettiğin alerjen ve diyet tercihlerine göre sana uygun olmayan üründe uyarır": "Vous avertit des produits inadaptés en fonction de vos préférences allergènes et alimentaires",
        "Taradığın ürünleri geçmişte tutar, favorilerine ekleyebilirsin": "Garde vos produits scannés dans l'historique, vous pouvez les ajouter aux favoris",
        "Veri yaklaşımı": "Approche des données",
        "Hesap yok.": "Pas de compte.",
        "Kayıt olmadan, giriş yapmadan kullanılır.": "Utilisez sans inscription ni connexion.",
        "Tercihlerin, geçmişin ve favorilerin <strong>cihazında</strong> saklanır.": "Vos préférences, historique et favoris sont stockés <strong>sur votre appareil</strong>.",
        "Ürün analizi için fotoğraf ve ürün bilgisi analiz servisine gönderilir.": "Les photos et informations sont envoyées au service d'analyse.",
        "Reklam yok, kullanıcı takibi yok.": "Pas de publicité, pas de suivi des utilisateurs.",
        "Gizlilik politikasının tamamı →": "Politique de confidentialité complète →",
        "Yuppa tıbbi bir cihaz değildir; hastalık teşhis etmez, tedavi etmez, iyileştirmez": "Yuppa n'est pas un dispositif médical ; il ne diagnostique, ne traite, ni ne guérit",
        "veya önlemez. Sağlığınızla ilgili kararlar için bir uzmana danışın.": "aucune maladie. Consultez un spécialiste pour vos décisions de santé.",
        "Gizlilik Politikası": "Politique de Confidentialité",
        "Kullanım Koşulları": "Conditions d'Utilisation",
        "Destek": "Support",
        "Ürün Analizi": "Analyse de Produit",
        "lang=\"tr\"": "lang=\"fr\"",
        "logo.png": "../logo.png"
    },
    "es": {
        "Ürünün içinde ne var, saniyeler içinde gör.": "Descubre qué hay dentro en segundos.",
        "Uygulama ne yapar": "Qué hace la aplicación",
        "Gıda ve kozmetik ürünlerinin fotoğrafını çekersin": "Toma fotos de productos alimenticios y cosméticos",
        "İçerik listesini analiz eder, anlaşılır bir puana dönüştürür": "Analiza la lista de ingredientes y la convierte en una puntuación clara",
        "Katkı maddelerini, şeker, tuz, yağ ve besin değerlerini sade bir dille açıklar": "Explica de forma sencilla los aditivos, el azúcar, la sal, las grasas y los valores nutricionales",
        "Kaydettiğin alerjen ve diyet tercihlerine göre sana uygun olmayan üründe uyarır": "Te advierte sobre productos no aptos según tus preferencias de alérgenos y dieta",
        "Taradığın ürünleri geçmişte tutar, favorilerine ekleyebilirsin": "Mantiene tus productos escaneados en el historial, puedes agregarlos a favoritos",
        "Veri yaklaşımı": "Privacidad de datos",
        "Hesap yok.": "Sin cuenta.",
        "Kayıt olmadan, giriş yapmadan kullanılır.": "Úsala sin registrarte ni iniciar sesión.",
        "Tercihlerin, geçmişin ve favorilerin <strong>cihazında</strong> saklanır.": "Tus preferencias, historial y favoritos se almacenan <strong>en tu dispositivo</strong>.",
        "Ürün analizi için fotoğraf ve ürün bilgisi analiz servisine gönderilir.": "Las fotos y la información se envían al servicio de análisis.",
        "Reklam yok, kullanıcı takibi yok.": "Sin anuncios, sin seguimiento de usuarios.",
        "Gizlilik politikasının tamamı →": "Política de privacidad completa →",
        "Yuppa tıbbi bir cihaz değildir; hastalık teşhis etmez, tedavi etmez, iyileştirmez": "Yuppa no es un dispositivo médico; no diagnostica, trata ni cura",
        "veya önlemez. Sağlığınızla ilgili kararlar için bir uzmana danışın.": "ninguna enfermedad. Consulta a un especialista para decisiones de salud.",
        "Gizlilik Politikası": "Política de Privacidad",
        "Kullanım Koşulları": "Términos de Uso",
        "Destek": "Soporte",
        "Ürün Analizi": "Análisis de Producto",
        "lang=\"tr\"": "lang=\"es\"",
        "logo.png": "../logo.png"
    }
}

for lang, trans in translations.items():
    os.makedirs(lang, exist_ok=True)
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Also adjust links to support/privacy/terms to stay in same directory if we translate them, or just point to root
    # For now, let's copy privacy, terms, support into the lang folder and translate basic terms
    
    for k, v in trans.items():
        content = content.replace(k, v)
        
    # Also fix hrefs inside index.html to be relative just in case, but they are already "privacy.html"
    with open(f"{lang}/index.html", "w", encoding="utf-8") as f:
        f.write(content)
        
    # Translate basic support/privacy/terms
    # For privacy/terms we just copy and replace TR title with EN title
    for page in ["privacy.html", "terms.html", "support.html"]:
        with open(page, "r", encoding="utf-8") as f:
            p_content = f.read()
        for k, v in trans.items():
            if k in ["Gizlilik Politikası", "Kullanım Koşulları", "Destek", "lang=\"tr\"", "logo.png"]:
                p_content = p_content.replace(k, v)
        # Fix back link
        p_content = p_content.replace('href="index.html"', 'href="index.html"')
        with open(f"{lang}/{page}", "w", encoding="utf-8") as f:
            f.write(p_content)

print("Language folders created.")
