from django.test import TestCase


class SmsClassifierTests(TestCase):
    def test_classify(self):
        r = self.client.get("/api/sms/id/classify", {"sms_text": "Mama minta pulsa 50rb ke nomor ini dulu ya, nanti mama ganti"})
        self.assertEqual(r.status_code, 200)
        self.assertIn(r.content.decode(), {"normal", "promo", "spam"})

    def test_missing_text(self):
        self.assertEqual(self.client.get("/api/sms/id/classify").status_code, 400)


class PageTests(TestCase):
    def test_pages_render(self):
        for url in ["/", "/home", "/api/", "/api/sms/id", "/api/fakenews/en", "/api/fakenews/id", "/blog/"]:
            with self.subTest(url=url):
                self.assertEqual(self.client.get(url).status_code, 200)
