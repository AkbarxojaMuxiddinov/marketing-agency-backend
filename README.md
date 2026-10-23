# con. marketing agency website

Telefon, planshet va kompyuter ekranlariga mos, UZ/RU/EN tilli bir sahifali sayt. Frontend dizayni va JavaScript bitta HTML faylida. Django orqali ishlaydigan nusxa `agency/templates/agency/home.html` faylida; alohida HTML nusxasi `con-agency-website.html` deb berilgan.

## Ishga tushirish

Loyiha papkasida quyidagi buyruqlarni bajaring:

```bash
docker compose up --build -d
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

Sayt: `http://localhost:8000/`

Admin panel: `http://localhost:8000/admin/`

## Portfolio, mijozlar va ijtimoiy tarmoqlar

Admin panelga superuser hisobidan kiring.

- **Portfolio** bo‘limida loyiha nomi, rasm va havolani kiriting. Loyihalar “G‘oyadan natijagacha” bo‘limida ko‘rinadi.
- **Mijozlar** bo‘limida mijoz nomi, logotip va sayt havolasini kiriting. “Saytda ko‘rsatilsin” tanlansa, mijoz “Bizga ishonishadi” bo‘limida chiqadi.
- **Ijtimoiy tarmoq havolalari** bo‘limida Instagram yoki Telegram’ni tanlab, profilning to‘liq `https://` havolasini kiriting. Faol havolalar sayt pastidagi footerda chiqadi. Har bir platforma uchun bittadan havola saqlanadi.

## API manzillari

- Xizmatlar: `GET /api/v1/services/`
- Portfolio: `GET /api/v1/portfolio/`
- Mijozlar: `GET /api/v1/clients/`
- Instagram va Telegram: `GET /api/v1/social-links/`
- Murojaat yuborish: `POST /api/v1/leads/create/` (`name`, `phone`, `message`)

Forma yuborgan email va tanlangan xizmat murojaatning `message` maydoniga qo‘shilib, admin panelda saqlanadi.

## Kontakt ma’lumotlari

Email va telefon raqamlari hozircha namuna. Ularni `agency/templates/agency/home.html` va `con-agency-website.html` fayllarida almashtiring. Instagram va Telegram manzillari admin paneldan boshqariladi.

Admin paneldan yuklangan rasm va ijtimoiy havolalar Django serveri orqali ishlaydi. Alohida HTML faylini bevosita (`file://`) ochganda admin API ulanishi bo‘lmaydi; dinamik ma’lumotlar uchun saytni Django orqali oching.
