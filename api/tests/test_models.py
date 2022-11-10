from django.test import TestCase
from api.models import OverheidsGebouw, Kamer, Artiest, Kunstwerk


class OverheidsGebouwTestCase(TestCase):
    def test_create_model_with_all_fields_only(self):
        record = OverheidsGebouw.objects.create(
            adres="Weesperstraat 113",
            postcode="1018 VN",
            stad="Amsterdam"
        )
        record.save()
        record_in_db = OverheidsGebouw.objects.get(adres="Weesperstraat 113")
        self.assertTrue(isinstance(record_in_db, OverheidsGebouw))


class KamerTestCase(TestCase):
    def setUp(self):
        building1 = OverheidsGebouw.objects.create(
            adres="Weesperstraat 113",
            postcode="1018 VN",
            stad="Amsterdam"
        )
        building1.save()

    def test_create_model_with_link_to_parent_model(self):
        building1 = OverheidsGebouw.objects.get(adres="Weesperstraat 113")
        record = Kamer.objects.create(
            verdieping=5,
            kamer_identificatie="mailteam",
            gebouw=building1
        )
        record.save()
        record_in_db = Kamer.objects.get(
            kamer_identificatie="mailteam"
        )
        self.assertTrue(isinstance(record_in_db, Kamer))
        self.assertTrue(record_in_db.gebouw, OverheidsGebouw)
        self.assertTrue(record_in_db.gebouw.id, 1)

